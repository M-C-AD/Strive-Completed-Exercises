import cv2
import numpy as np
import matplotlib.pyplot as plt

imag1 = cv2.imread('m2.jpg')
copy_m2 = imag1.copy()

B, G, R = cv2.split(copy_m2)

cv2.imshow('Blue', B)
cv2.imshow('Green', G)
cv2.imshow('Red', R)
cv2.waitKey(0)

R = cv2.add(R, 100)
merge_copy_R_plus= cv2.merge([B, G, R])
cv2.imshow('Merged image red Plus', merge_copy_R_plus)
cv2.waitKey(0)

zeros = np.zeros(imag1.shape[:2], dtype='uint8')
cv2.imshow('black Back', zeros)

cv2.imshow('Red', cv2.merge([zeros, zeros, R]))
cv2.imshow('Green', cv2.merge([zeros, G, zeros]))
cv2.imshow('Blue', cv2.merge([B, zeros, zeros]))
# cv2.waitKey(0)
# cv2.destroyAllWindows()

merge_copy_m2 = cv2.merge([B, G, R])
cv2.imshow('Merged image 2', merge_copy_m2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.destroyAllWindows()

# Use the image below and convert it from BGR to HSV
img = cv2.imread('img/m.jpg')
plt.figure(figsize = (20,15));
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
# plt.show()

copy_img2 = img.copy()
copy_img2 = cv2.cvtColor(copy_img2, cv2.COLOR_RGB2HSV)
h, s, v = cv2.split(copy_m2)

