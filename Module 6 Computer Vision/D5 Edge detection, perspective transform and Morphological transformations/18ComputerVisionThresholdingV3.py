import cv2
import numpy as np
import matplotlib.pyplot as plt

text = cv2.imread('img/t1.png')
text_gray = text.copy()
text_gray = cv2.cvtColor(text_gray, cv2.COLOR_BGR2GRAY)
plt.figure(figsize=(12, 10))
plt.imshow(text, cmap='gray')
plt.show()

text_2 = cv2.imread('img/t2.png')
plt.imshow(text_2, cmap='gray')
plt.show()

ret, thresh1 = cv2.threshold(text, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('new text 1', thresh1)

th = 0
max_val = 255

gau_blur = cv2.GaussianBlur(text_gray, (7, 7), 0)

ret, thresh2 = cv2.threshold(gau_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
plt.imshow(thresh2, cmap='gray')
plt.show()
# cv2.imshow('new text 2', thresh2)

cv2.waitKey(0)
cv2.destroyAllWindows()


