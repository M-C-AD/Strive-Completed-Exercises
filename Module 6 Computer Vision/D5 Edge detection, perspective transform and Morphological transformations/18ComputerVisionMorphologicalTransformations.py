import cv2
import numpy as np
import matplotlib.pyplot as plt

image1 = cv2.imread('img/noisy.png')
noisy = image1.copy()
cv2.imshow('Original noisy', noisy)
kernel = np.ones((13, 13), dtype=np.uint8)

ret, thresh1 = cv2.threshold(noisy, 127, 255, cv2.THRESH_BINARY_INV)
di_noisy = cv2.dilate(thresh1, kernel, iterations= 1)
cv2.imshow('dilation', di_noisy)

# er_noisy = cv2.erode(noisy, kernel, 1)
# cv2.imshow('erosion', er_noisy)


cv2.waitKey(0)
cv2.destroyAllWindows()


