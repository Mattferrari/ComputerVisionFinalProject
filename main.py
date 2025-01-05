import cv2
import numpy as np
from picamera2 import Picamera2
import time
from password import *
from carDetection import *

def main():
    contraseña = ["Triangulo", "Cuadrado", "Pentagono"]
    rangos_colores = {
        'verde': ([0, 182, 0], [74, 255, 185]),
        'azul': ([98, 174, 52], [130, 255, 255])
    }
    contadores = {color: 0 for color in rangos_colores.keys()}
    tiempos_vuelta = {color: {} for color in rangos_colores.keys()}
    dicc_tiempos = {color: time.time() for color in rangos_colores.keys()}
    purple_color = (255, 0, 255)
    index = 0
    correcto = False
    mensaje = ""
    ultimo_tiempo_mensaje = time.time()
    tiempo_mostrar_mensaje = 2  # Segundos para mostrar mensajes en pantalla
    contrasena_correcta = False

    # Configuración de la cámara
    picam = Picamera2()
    picam.preview_configuration.main.size = (1280, 720)
    picam.preview_configuration.main.format = "RGB888"
    picam.preview_configuration.align()
    picam.configure("preview")
    picam.start()

    # Configuración para grabar el video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output_video_2.avi', fourcc, 20.0, (1280, 720))  # 20 FPS de grabación

    print("Muestra las figuras en el orden correcto: Triangulo, Cuadrado, Pentagono.")
    time.sleep(2)

    while True:
        start_time = time.time()
        frame = picam.capture_array()
        procesado = frame.copy()

        if not contrasena_correcta:
            # Detección de figuras para la contraseña
            procesado, esquinas = shi_tomasi_corner_detection(procesado, maxCorners=5, qualityLevel=0.1, minDistance=20, corner_color=purple_color, radius=4)
            figura_detectada = clasificar_poligono(esquinas)

            # Mostrar mensaje en la pantalla

            # Confirmar figura actual
            if cv2.waitKey(1) & 0xFF == ord('f'):  # Confirmar figura actual
                if figura_detectada == contraseña[index]:
                    correcto = True
                    mensaje = f"Figura correcta: {figura_detectada}"
                    index += 1
                    if index == len(contraseña):
                        mensaje = "Todo correcto. Acceso permitido."
                        contrasena_correcta = True
                else:
                    correcto = False
                    mensaje = "Figura incorrecta. Reinicia la secuencia."
                    index = 0
                ultimo_tiempo_mensaje = time.time()
            
            if mensaje and time.time() - ultimo_tiempo_mensaje < tiempo_mostrar_mensaje:
                color_mensaje = (0, 255, 0) if correcto else (0, 0, 255)
                cv2.putText(procesado, mensaje, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color_mensaje, 2)

        if contrasena_correcta:
            # Detección de coches
            meta_coords = detectar_meta(procesado)
            resultados = detectar_colores(procesado, rangos_colores)
            procesado = seguir_objetos(procesado, resultados, meta_coords, contadores, tiempos_vuelta, dicc_tiempos)

        # Mostrar FPS en la pantalla
        end_time = time.time()
        fps = 1 / (end_time - start_time)
        cv2.putText(procesado, f'FPS: {fps:.2f}', (1080, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        # Escribir el frame procesado al archivo de video
        out.write(procesado)

        # Mostrar la imagen en la ventana
        cv2.imshow("Deteccion de formas", procesado)

        # Detener la grabación si se presiona 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar el objeto VideoWriter y detener la cámara
    out.release()
    cv2.destroyAllWindows()
    picam.stop()

if __name__ == "__main__":
    main()