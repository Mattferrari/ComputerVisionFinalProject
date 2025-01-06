import cv2
import numpy as np
from picamera2 import Picamera2
import time

# Función para detectar objetos de colores específicos en un fotograma
def detectar_colores(frame, color_ranges):
    """
    Detecta objetos de colores específicos en un fotograma.

    Args:
        frame (numpy.ndarray): Fotograma en formato BGR.
        color_ranges (dict): Diccionario con rangos HSV para los colores.

    Returns:
        dict: Diccionario con máscaras y contornos por color.
    """
    resultados = {}
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convertir a HSV

    for color, color_range in color_ranges.items():
        # Crear máscara para el color
        color_mask = cv2.inRange(frame_hsv, np.array(color_range[0]), np.array(color_range[1]))

        # Encontrar contornos
        contornos, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        resultados[color] = {
            'mascara': color_mask,
            'contornos': contornos
        }
    return resultados

# Función para detectar y verificar la línea de meta
def detectar_meta(frame):
    """
    Detecta la línea de meta negra en el fotograma.

    Args:
        frame (numpy.ndarray): Fotograma en formato BGR.

    Returns:
        tuple: Coordenadas de la línea de meta (x1, y1, x2, y2), o None si no se detecta.
    """
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    light_black = np.array([0, 0, 0])
    dark_black = np.array([179, 50, 50])

    mask = cv2.inRange(frame_hsv, light_black, dark_black)
    contornos, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contorno in contornos:
        if cv2.contourArea(contorno) > 2000:  # Filtrar contornos pequeños
            x, y, w, h = cv2.boundingRect(contorno)
            return (x, y, x + w, y + h)

    return None

# Función para seguir objetos detectados
def seguir_objetos(frame, resultados, meta_coords, contadores, tiempos_vuelta, dicc_tiempos):
    """
    Dibuja los contornos, sigue los objetos detectados en el fotograma y cuenta coches al pasar la línea de meta.

    Args:
        frame (numpy.ndarray): Fotograma original.
        resultados (dict): Resultados de la detección por color.
        meta_coords (tuple): Coordenadas de la línea de meta (x1, y1, x2, y2).
        contadores (dict): Contadores de coches por color.
        tiempos_vuelta (dict): Diccionario con tiempos de vuelta por color.
        dicc_tiempos (dict): Diccionario con el último tiempo de paso por color.

    Returns:
        numpy.ndarray: Fotograma con los objetos seguidos.
    """
    colores = {
        'verde': (0, 255, 0),
        'azul': (255, 0, 0)
    }
    tiempo_min = 0.5

    if meta_coords:
        x1, y1, x2, y2 = meta_coords
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 2)  # Dibujar la línea de meta

        for color, data in resultados.items():
            for contorno in data['contornos']:
                if cv2.contourArea(contorno) > 500:  # Filtrar objetos pequeños
                    x, y, w, h = cv2.boundingRect(contorno)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), colores[color], 2)
                    cv2.putText(frame, color, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, colores[color], 2)

                    # Verificar si el objeto cruza la línea de meta
                    centro_x, centro_y = x + w // 2, y + h // 2
                    if y1 <= centro_y <= y2 and x1 <= centro_x <= x2:
                        tiempo_actual = time.time()
                        if tiempo_actual - dicc_tiempos[color] >= tiempo_min:
                            contadores[color] += 1
                            tiempos_vuelta[color][contadores[color]] = tiempo_actual - dicc_tiempos[color]
                            dicc_tiempos[color] = tiempo_actual

                            print(f"{color} cruzó la línea. Total: {contadores[color]}.")

    # Mostrar el contador en la parte superior izquierda y los tiempos de vuelta
    y_offset = 30
    for color, count in contadores.items():
        cv2.putText(frame, f"{color}: {count}", (10, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.8, colores[color], 2)
        if count > 0:
            tiempo_vuelta = tiempos_vuelta[color].get(count, 0)
            cv2.putText(frame, f"Ult. Vuelta: {tiempo_vuelta:.2f}s", (150, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.6, colores[color], 2)
        y_offset += 30

    return frame