from typing import List
import numpy as np
import imageio
import cv2
import copy
import glob
import os 
from os.path import dirname, join

def load_images(filenames: List) -> List:
    return [imageio.imread(filename) for filename in filenames]


def show_image(img: np.array, title: str = "Image"):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def write_image(img: np.array, path: str):
    cv2.imwrite(path, img)

# TODO Design the method. It should return a np.array with np.float32 elements
def get_chessboard_points(chessboard_shape, dx, dy):
    long = chessboard_shape[0]
    short = chessboard_shape[1]

    points = []
    for dim1 in range(short):
        for dim2 in range(long):
            point = [dim1 * dx, dim2 * dy, 0]
            points.append(point)
    return np.array(points, dtype=np.float32)

# TODO Homework

path = "imagenes_chess/"
print(path)
imgs_path = [join(path, f"{img_path}") for img_path in os.listdir(path)]

imgs = load_images(imgs_path)

corners = []
for img in imgs:
    corner = cv2.findChessboardCorners(img, (7, 7))
    corners.append(corner)

corners_copy = copy.deepcopy(corners)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.01)

imgs_gray = [cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in imgs] 

corners_refined = [cv2.cornerSubPix(i, cor[1], (7, 7), (-1, -1), criteria) if cor[0] else [] for i, cor in zip(imgs_gray, corners_copy)]

imgs_copy = copy.deepcopy(imgs)

imgs_with_point = []
for img, corner in zip(imgs_copy, corners):
    imgs_with_point.append(cv2.drawChessboardCorners(img, (7, 7), corner[1], corner[0]))

# TODO Show images and save when needed

def show_image(img: np.array, title: str = "Image"):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def write_image(img: np.array, path: str):
    cv2.imwrite(path, img)

for img in imgs_with_point:
    show_image(img, "Image")

chessboard_points = [get_chessboard_points((7, 7), 30, 30) for corner in corners if corner[0]]
print(len(chessboard_points))

# Filter data and get only those with adequate detections
valid_corners = [cor[1] for cor in corners if cor[0]]
# Convert list to numpy array
valid_corners = np.asarray(valid_corners, dtype=np.float32)

# TODO
rms, intrinsics, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(chessboard_points, valid_corners, (8,6), np.zeros((3,3)), None)

# Obtain extrinsics
extrinsics = list(map(lambda rvec, tvec: np.hstack((cv2.Rodrigues(rvec)[0], tvec)), rvecs, tvecs))

# Print outputs
print("Intrinsics:\n", intrinsics)
print("Distortion coefficients:\n", dist_coeffs)
print("Root mean squared reprojection error:\n", rms)