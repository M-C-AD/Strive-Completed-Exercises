import cv2
import numpy as np
import matplotlib.pyplot as plt

imag1 = cv2.imread('img/m2.jpg')
copy_m2 = imag1.copy()

B, G, R = cv2.split(copy_m2)

cv2.imshow('Blue', B)
cv2.imshow('Green', G)
cv2.imshow('Red', R)
cv2.waitKey(0)

R = cv2.add(R, 255)
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
# cv2.destroyAllWindows()

# Use the image below and convert it from BGR to HSV
# img = cv2.imread('img/m.jpg')
# plt.figure(figsize = (20,15))
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.show()

copy_img2 = imag1.copy()
img2_HSV = cv2.cvtColor(copy_img2, cv2.COLOR_BGR2HSV)
copy_img2_HSV = img2_HSV.copy()
h, s, v = cv2.split(img2_HSV)

# cv2.imshow('Hue', h)
# cv2.imshow('Saturation', s)
# cv2.imshow('value', v)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

lower_green = np.array([40, 50, 50])
upper_green = np.array([80, 255, 255])

lower_blue = np.array([90, 50, 50])
upper_blue = np.array([150, 255, 255])
mask_gr_bl = cv2.inRange(copy_img2_HSV, lower_green, upper_blue)

mask_blue = cv2.inRange(copy_img2_HSV, lower_blue, upper_blue)
mask_green = cv2.inRange(copy_img2_HSV, lower_green, upper_green)

mask_image = copy_m2.copy() # alternative approach
mask_image[mask_gr_bl == 0] = [0, 0, 0] # alternative approach

result_gr_bl = cv2.bitwise_and(copy_m2, copy_m2, mask= mask_gr_bl)


result_green = cv2.bitwise_and(copy_m2, copy_m2, mask= mask_green)
result_blue = cv2.bitwise_and(copy_m2, copy_m2, mask= mask_blue)
blue_green_result = cv2.bitwise_or(result_green, result_blue)
cv2.imshow('blue mask', mask_blue)
cv2.imshow('Green mask', mask_green)
cv2.imshow('Result blue', result_blue)
cv2.imshow('Result green', result_green)
cv2.imshow('Next Orig', copy_m2)
cv2.imshow('Combined Result', blue_green_result)
cv2.imshow('Combined Result green blue', result_gr_bl)
cv2.imshow('Combined alternative result green blue', mask_image)


cv2.waitKey(0)
cv2.destroyAllWindows()

opacity = 0.5
all_sweets = cv2.addWeighted(copy_m2, opacity, mask_image, 1 - opacity, 0)
cv2.imshow('Opaque', all_sweets) 
cv2.imshow('Combined alternative result green blue', mask_image)
cv2.imshow('Next Orig', copy_m2)
cv2.waitKey(0)
cv2.destroyAllWindows()


#convert your own colours
# BGR_colour = np.array([[[255, 0, 0]]])
# X = cv2.cvtColor(BGR_colour, cv2.COLOR_BGR2HSV)
#
# print(X[0][0])


