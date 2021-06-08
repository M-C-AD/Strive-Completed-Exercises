import cv2
import numpy as np
import matplotlib.pyplot as plt

print(cv2.__version__)

blue1 = cv2.imread('blue-flowers.jpg')
blue1_copy = blue1.copy()
cv2.imshow("Blue 1 Copy", blue1_copy)
cv2.waitKey(0)
# cv2.destroyWindow("blue 1")
# blue1_copy = cv2.cvtColor(blue1_copy, cv2.COLOR_BGR2RGB)
cv2.circle(blue1_copy, (134, 85), 20, (23, 99, 168), -1)
cv2.line(blue1_copy,(98,74),(225,125),(0,0,255),2)

cv2.imshow('Pic line', blue1_copy)
cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.circle(blue1_copy, (134, 85), 20, (23, 99, 168), -1)
cv2.imshow('Pic Circle', blue1_copy)
cv2.waitKey(0)
# cv2.destroyAllWindows()

poly_points = np.array([[[61, 58], [179, 139], [277, 66], [97,13]]])
# cv2.polylines(blue1_copy, poly_points, False, (255, 255, 255))
cv2.polylines(blue1_copy, poly_points, True, (255, 255, 255), 4)
cv2.imshow('Pic Polygon', blue1_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()

Sharbat = cv2.imread('Sharbat-Gula.jpg')
overlay = Sharbat.copy()
cv2.imshow('Sharbat', overlay)
cv2.waitKey(0)
poly_points = np.array([[[102, 75], [102, 238], [209, 238], [209, 75]]])

# cv2.destroyAllWindows()

# cv2.polylines(overlay, poly_points, True, (127, 127, 127))
cv2.rectangle(overlay, (90,88), (210,237), (127, 127, 127), -1)
# cv2.imshow('Sharbat overlay', overlay)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
opacity = 0.5
Sharbat2 = cv2.addWeighted(Sharbat, opacity, overlay, 1 - opacity, 0)
cv2.imshow('Sharbat overlay 2', Sharbat2)
cv2.putText(Sharbat2, 'Timeless', (90, 88), fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale= 0.5, color= (0, 0, 255)
            , thickness= 1)
cv2.imshow('Sharbat overlay 2', Sharbat2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# B, G, R = cv2.split(Sharbat)
#
# plt.figure(figsize=(300, 380))
# plt.imshow(B, cmap= 'gray')
#
# merge_img = cv2.merge([B, G, R])













