import cv2
import numpy as np
from picamera2 import Picamera2
import time

# Funciones de deteccion y análisis de esquinas
def shi_tomasi_corner_detection(image: np.array, maxCorners: int, qualityLevel: float, minDistance: int, corner_color: tuple, radius: int):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, maxCorners, qualityLevel, minDistance)
    corners = np.intp(corners)
    corners_list = []
    for corner in corners:
        x, y = corner.ravel()
        corners_list.append([x, y])
        cv2.circle(image, (x, y), radius, corner_color, -1)
    return image, corners_list

def ordenar_puntos(puntos):
    puntos = np.array(puntos)
    origen = puntos[np.argmin(puntos[:, 0] + puntos[:, 1])]
    def calcular_angulo(p):
        return np.arctan2(p[1] - origen[1], p[0] - origen[0])
    return sorted(puntos, key=calcular_angulo)

def calcular_angulos(puntos_ordenados):
    angulos = []
    n = len(puntos_ordenados)
    for i in range(n):
        p1 = puntos_ordenados[i] - puntos_ordenados[i - 1]
        p2 = puntos_ordenados[(i + 1) % n] - puntos_ordenados[i]
        cos_theta = np.dot(p1, p2) / (np.linalg.norm(p1) * np.linalg.norm(p2))
        angulo = np.arccos(np.clip(cos_theta, -1, 1))
        angulos.append(np.degrees(angulo))
    return angulos

def clasificar_poligono(puntos):
    puntos_ordenados = ordenar_puntos(puntos)
    n = len(puntos_ordenados)
    if n == 3:
        return "Triangulo"
    elif n == 4:
        angulos = calcular_angulos(puntos_ordenados)
        if all(65 < ang < 105 for ang in angulos):
            return "Cuadrado"
        else:
            return "Cuadrado"
    elif n == 5:
        return "Pentagono"
    else:
        return "Otro"