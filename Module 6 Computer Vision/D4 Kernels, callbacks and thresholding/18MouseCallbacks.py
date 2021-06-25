import cv2


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

cv2.imshow('Original Super', sup_man)
cv2.setMouseCallback('Original Super', roi)

cv2.waitKey(0)
cv2.destroyAllWindows()




