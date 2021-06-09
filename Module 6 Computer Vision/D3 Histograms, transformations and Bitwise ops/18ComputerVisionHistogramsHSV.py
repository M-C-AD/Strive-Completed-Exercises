import cv2
import numpy as np
import matplotlib.pyplot as plt

# image1 = cv2.imread(('img/MarvinTheMartian.jpg'))
# image1 = cv2.imread(('img/MrKrabs.jpg'))
# image1 = cv2.imread(('img/SpiderMan.jpg'))
image1 = cv2.imread(('img/SuperMan.jpg'))
MTM = image1.copy()

MTM = cv2.cvtColor(MTM,cv2.COLOR_BGR2HSV)

hist_MTMB = cv2.calcHist(MTM, [0], None, [255], [0, 255])
plt.figure(figsize=(20,30))
plt.plot(hist_MTMB,color = 'b')
# plt.show()

hist_MTMG = cv2.calcHist(MTM, [1], None, [255], [0, 255])
plt.figure(figsize=(20,30))
plt.plot(hist_MTMG,color = 'g')
# plt.show()

hist_MTMG = cv2.calcHist(MTM, [2], None, [255], [0, 255])
plt.figure(figsize=(20,30))
plt.plot(hist_MTMG,color = 'r')
plt.show()

colour = ['b','g','r']

for i, colour in enumerate(colour):
    hist = cv2.calcHist(MTM, [i], None, [255], [0, 255])
    plt.plot(hist, color = colour)
    plt.xlim(0, 256)
plt.show()

# cv2.imshow('test', image1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

