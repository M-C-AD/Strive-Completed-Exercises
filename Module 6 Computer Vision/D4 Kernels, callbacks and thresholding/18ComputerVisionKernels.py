import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('img/Sharbat-Gula.jpg')
Shar_img = img1.copy()
cv2.imshow('Original', Shar_img)
cv2.waitKey(0)

blur_kernal = np.ones((3,3), np.float32)/9


# blur_Shar = cv2.filter2D(Shar_img, -1, blur_kernal)
blur_Shar = cv2.medianBlur(Shar_img, 27)
# blur_Shar = cv2.bilateralFilter(Shar_img,)
cv2.imshow('Blur 2nd', blur_Shar)
cv2.waitKey(0)
# cv2.destroyAllWindows()

blur_kernal = np.ones((5, 5), np.float32)/25


blur_Shar = cv2.filter2D(Shar_img, -1, blur_kernal)
cv2.imshow('Blur 3rd', blur_Shar)
cv2.waitKey(0)
# cv2.destroyAllWindows()

blur_kernal = np.ones((7, 7), np.float32)/49


blur_Shar = cv2.filter2D(Shar_img, -1, blur_kernal)
cv2.imshow('Blur 4th', blur_Shar)
cv2.waitKey(0)
# cv2.destroyAllWindows()

Sharp_kernal = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
SharImag_Shar = cv2.filter2D(blur_Shar, -1, Sharp_kernal)
cv2.imshow('sharpen image', SharImag_Shar)
cv2.waitKey(0)
cv2.destroyAllWindows()

