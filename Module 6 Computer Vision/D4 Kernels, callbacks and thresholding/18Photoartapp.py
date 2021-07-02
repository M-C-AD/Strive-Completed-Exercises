import cv2
import numpy

image1 = cv2.imread('img/MrKrabs.jpg')
krab = image1.copy()


def sketch(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.Canny(image, 30, 180)
    cv2.imshow('Image sketch', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


sketch(krab)

