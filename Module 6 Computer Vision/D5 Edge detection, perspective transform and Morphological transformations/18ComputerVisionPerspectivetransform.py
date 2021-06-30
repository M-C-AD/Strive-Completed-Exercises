import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('img/scan.jpg')
scan = image.copy()
plt.figure(figsize=(12, 18))
plt.imshow(scan)
plt.show()


original_coordinates = np.float32([[326, 14], [697, 210], [85, 617], [530, 778]])
height,  width = 603, 371
new_coordinates = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

M = cv2.getPerspectiveTransform(original_coordinates, new_coordinates)

warped_scan = cv2.warpPerspective(image, M, (width, height))

cv2.imshow('Warped Image', warped_scan)

cv2.waitKey(0)
cv2.destroyAllWindows()
