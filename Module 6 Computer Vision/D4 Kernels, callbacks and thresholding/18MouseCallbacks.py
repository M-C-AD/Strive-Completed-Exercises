import cv2
import numpy as np


prevX, prevY = -1, -1
def roi(event, x, y, flags, parms):
    print(x, ',', y)
    global prevX, prevY
    if event == cv2.EVENT_LBUTTONDOWN:
        if prevX == -1 and prevY == -1:
            prevX, prevY = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.rectangle(sup_man, (prevX, prevY), (x, y), (255, 255, 255), 3)
        prevX, prevY = -1, -1
    cv2.imshow('Original Super', sup_man)


image1 = cv2.imread('img/SuperMan.jpg')
sup_man = image1.copy()
image2 = cv2.imread('img/Sharbat-Gula.jpg')
lady = image2.copy()



cv2.imshow('Original Super', sup_man)
cv2.setMouseCallback('Original Super', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()


threshold_value = 128
threshold_type = cv2.THRESH_BINARY


window_name = 'threshold'

gray_lady = cv2.cvtColor(lady, cv2.COLOR_BGR2GRAY)

cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

def change_T_value(val):
    threshold_value = val
    ret, thresh = cv2.threshold(gray_lady, threshold_value, 255, threshold_type)
    cv2.imshow(window_name, thresh)


cv2.createTrackbar('Threshold name', window_name, threshold_value, 255, change_T_value)


cv2.imshow(window_name, gray_lady)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.waitKey(1)




