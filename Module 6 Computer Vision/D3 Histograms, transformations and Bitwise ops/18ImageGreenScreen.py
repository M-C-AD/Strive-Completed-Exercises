import cv2
import numpy as np

image1 = cv2.imread('img/GreenScreen.jpg')
image2 = cv2.imread('img/NightShift.jpg')

screen_copy = image1.copy()
night_copy = image2.copy()

HSV_screen = cv2.cvtColor(screen_copy, cv2.COLOR_BGR2HSV)
lower_green = np.array([40, 50, 50])
upper_green = np.array([70, 255, 255])

green_mask = cv2.inRange(HSV_screen, lower_green, upper_green)# this creates the monochrome mask of the background
inv_green = cv2.bitwise_not(green_mask) #this creates the monochrome mask of the girl
screen_mask = cv2.bitwise_not(screen_copy, screen_copy, mask= green_mask)
lady_mask = cv2.bitwise_not(screen_copy, screen_copy, mask= inv_green)


night_no_lady = cv2.bitwise_and(night_copy, night_copy, mask= green_mask)# night image and lady cut out
lady_no_night = cv2.bitwise_and(image1, image1, mask= inv_green)# Lady alone
lady_and_night = cv2.bitwise_or(night_no_lady, lady_no_night)

cv2.imshow('Original Screen', image1)
cv2.imshow('Screen Mask', green_mask)
cv2.imshow('Lady Mask', inv_green)
cv2.imshow('Combo Lady and Night', lady_and_night)

cv2.waitKey(0)
cv2.destroyAllWindows()

