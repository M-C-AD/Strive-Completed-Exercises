import cv2

image1 = cv2.imread('img/m.jpg')
mnm = image1.copy()
cv2.imshow('original', mnm)
mnm_hsv = cv2.cvtColor(mnm, cv2.COLOR_BGR2HSV)


h, s, v = cv2.split(mnm_hsv)
copy_s = s.copy()
copy_s[:] = 100

new_image = cv2.merge([copy_s, copy_s, v])
new_RGB = cv2.cvtColor(new_image, cv2.COLOR_HSV2RGB)
back_2_color = cv2.merge([h, s, v])
back_2_color = cv2.cvtColor(back_2_color, cv2.COLOR_HSV2BGR)


cv2.imshow('augmented HSV', new_image)
cv2.imshow('Gray', new_RGB)
cv2.imshow('back to gray', back_2_color)

cv2.waitKey(0)
cv2.destroyAllWindows()



