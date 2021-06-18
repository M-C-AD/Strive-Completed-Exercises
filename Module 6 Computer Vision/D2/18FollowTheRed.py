import cv2
import numpy as np

video = cv2.VideoCapture('img/Tennis5261.mp4')

lower_red = (0, 150, 50)
upper_red = (20, 255, 255)
lower_blue = (95, 150, 20)
upper_blue = (105, 200, 200)


while(video.isOpened()):
    check, frame = video.read()
    if frame is not None:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask_red = cv2.inRange(img, lower_red, upper_red)
        mask_blue = cv2.inRange(img, lower_blue, upper_blue)
        rd_blu_mask = cv2.bitwise_or(mask_red, mask_blue)
        rdbl_2 = cv2.bitwise_and(frame, frame, mask=rd_blu_mask)
        no_red = cv2.bitwise_and(frame, frame, mask=mask_red)
        #img = frame
        cv2.imshow('frame', no_red)
        cv2.imshow('Both', rdbl_2)
        # cv2.imshow('Mask', mask_blue)
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break
    else:
        break


video.release()
cv2.destroyAllWindows()
cv2.waitKey(1)