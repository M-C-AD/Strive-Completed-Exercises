import cv2
import numpy as np
import matplotlib.pyplot as plt

image1 = cv2.imread('img/text.png', 0)
# image1 = cv2.imread('img/noisy.png', 0)
image2 = cv2.imread('img/notes.png', 0)

text = image1.copy()
# text = cv2.cvtColor(text, cv2.COLOR_BGR2GRAY)
cv2.imshow('Origianl Image', text)


ret, thresh_binary = cv2.threshold(text, 75, 255, cv2.THRESH_BINARY)
ret, thresh_trunc = cv2.threshold(text, 127, 255, cv2.THRESH_TRUNC)
ret, thresh_tozero = cv2.threshold(text, 127, 255, cv2.THRESH_TOZERO)
ret, thresh_binary_inv = cv2.threshold(text, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh_tozero_inv = cv2.threshold(text, 127, 255, cv2.THRESH_TOZERO_INV)
# print('RET :', ret, '\n')
# print('Thresh :', thresh_tozero_inv, '\n')

cv2.imshow('thresh_binary', thresh_binary)
cv2.imshow('thresh_trunc', thresh_trunc)
cv2.imshow('thresh_tozero', thresh_tozero)
cv2.imshow('thresh_binary_inv', thresh_binary_inv)
cv2.imshow('thresh_tozero_inv', thresh_tozero_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()

notes = image2.copy()

intensity_matrix = np.ones(notes.shape, dtype='uint8') * 20
brighter_notes = (notes + intensity_matrix)
cv2.imshow('Bright Notes', brighter_notes)

cv2.waitKey(0)
cv2.destroyAllWindows()

