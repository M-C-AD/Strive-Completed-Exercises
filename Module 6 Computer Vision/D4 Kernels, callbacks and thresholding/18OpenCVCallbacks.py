import cv2
import numpy as np
import matplotlib.pyplot as plt

image1 = cv2.imread('img/sarah.jpg')
lady = image1.copy()
cv2.imshow('Original image', lady)
char_typed = 0
print(chr(27))

while True:
    char_typed = cv2.waitKey(0)
    if char_typed == ord('g') or char_typed == ord('G'):
        # print('g was hit')
        cv2.destroyAllWindows()
        grey = cv2.cvtColor(lady, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Gray lady', grey)
    elif char_typed == ord('c') or char_typed == ord('C'):
        # print('c was hit')
        cv2.destroyAllWindows()
        cv2.imshow('Colour Lady', lady)
    elif char_typed == ord('t') or char_typed == ord('T'):
        cv2.destroyAllWindows()
        thres = cv2.cvtColor(lady, cv2.COLOR_BGR2GRAY)
        ret, thres_pic = cv2.threshold(thres, 127, 255, cv2.THRESH_BINARY)
        # thres_pic = cv2.threshold(lady, 127, 255, cv2.THRESH_BINARY)
        cv2.imshow('thres pic', thres_pic)
    # elif char_typed == ord(27):
    elif char_typed == 27:
        break



