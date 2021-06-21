import cv2
import numpy as np
import matplotlib.pyplot as plt

image1 = cv2.imread('img/scan.jpg')
doc1 = image1.copy()

doc_shape = doc1.shape
print(doc_shape)

height, width = doc1.shape[:2]
height_fourth, width_fourth = height/4, width/4
T = np.float32([[1, 0, height_fourth], [0, 1, width_fourth]])
print(T)
translation = cv2.warpAffine(doc1, T, (width, height))
cv2.imshow('Original Document', doc1)
cv2.imshow('Translation Image', translation)

image2 = cv2.imread('img/MarvinTheMartian.jpg')
MTM = image2.copy()

height, width = MTM.shape[:2]
half_width, half_height = width/2, height/2

centre_rotation = cv2.getRotationMatrix2D((half_width, half_height), -35, 2)
rotated_MTM = cv2.warpAffine(MTM, centre_rotation, (width, height))
cv2.imshow('Original MARVIN', MTM)
cv2.imshow('Twisted Marv', rotated_MTM)

image3 = cv2.imread('img/day1.jpg')
day1 = image3.copy()
height, width = day1.shape[:2]

x_scale = width // 2
y_scale = height // 2
day_scale = cv2.resize(day1, (x_scale, y_scale), interpolation= cv2.INTER_LANCZOS4)
cv2.imshow('Original Day', day1)
cv2.imshow('Down Day1', day_scale)

x_scale = width * 2
y_scale = height * 2
day_scale = cv2.resize(day1, (x_scale, y_scale), interpolation= cv2.INTER_LANCZOS4)
cv2.imshow('Up Day1', day_scale)

cv2.waitKey(0)
cv2.destroyAllWindows()





