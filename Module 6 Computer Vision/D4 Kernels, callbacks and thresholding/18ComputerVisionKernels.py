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


blur_Shar2 = cv2.filter2D(Shar_img, -1, blur_kernal)
cv2.imshow('Blur 4th', blur_Shar2)
cv2.waitKey(0)
# cv2.destroyAllWindows()

Sharp_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
SharImag_Shar = cv2.filter2D(blur_Shar, -1, Sharp_kernel)
cv2.imshow('sharpen image', SharImag_Shar)
cv2.waitKey(0)
# cv2.destroyAllWindows()

edge_kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
# Edge_Shar = cv2.filter2D(SharImag_Shar, -1, edge_kernel)
Edge_Shar = cv2.filter2D(img1, -1, edge_kernel)
cv2.imshow('Edges of Shar', Edge_Shar)
cv2.waitKey(0)
# cv2.destroyAllWindows()

Gray_shar = img1.copy()
# Gray_shar = cv2.cvtColor(Gray_shar, cv2.COLOR_BGR2GRAY)
Gray_shar = cv2.cvtColor(blur_Shar2, cv2.COLOR_BGR2GRAY)
sob_ed_x = cv2.Sobel(Gray_shar, cv2.CV_64F, 1, 0, )
sob_ed_y = cv2.Sobel(Gray_shar, cv2.CV_64F, 0, 1, )

cv2.imshow('Edge X', sob_ed_x)
cv2.imshow('Egde Y', sob_ed_x)

Shar_or = cv2.bitwise_or(sob_ed_x, sob_ed_y)
cv2.imshow('Or picture', Shar_or)

canny_shar = cv2.Canny(img1, 30, 180)
cv2.imshow('Canny Shar', canny_shar)

cv2.waitKey(0)
cv2.destroyAllWindows()
