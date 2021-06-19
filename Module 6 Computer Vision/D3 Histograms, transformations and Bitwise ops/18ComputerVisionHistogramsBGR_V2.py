import cv2
import matplotlib.pyplot as plt
import numpy as np

image1 = cv2.imread('img/TennisBall.jpg')
tennis_copy = image1.copy()
tennis_copy = cv2.cvtColor(tennis_copy, cv2.COLOR_BGR2RGB)
print(tennis_copy.shape)
plt.figure(figsize=(30, 20))

R_hist = cv2.calcHist([tennis_copy], [0], None, [255], [0, 255])
plt.plot(R_hist, color = 'r')
plt.show()

G_hist = cv2.calcHist([tennis_copy], [1], None, [255], [0, 255])
plt.plot(G_hist, color = 'g')
plt.show()

B_hist = cv2.calcHist([tennis_copy], [2], None, [255], [0, 255])
plt.plot(B_hist, color = 'b')
plt.show()

colours = ['r', 'g', 'b']
for i, colours in enumerate(colours):
    histogram = cv2.calcHist([tennis_copy], [i], None, [255], [0, 255])
    plt.plot(histogram, color= colours)
    plt.xlim(0, 255)
plt.show()

tennis_copy_HSV = image1.copy()
tennis_copy_HSV = cv2.cvtColor(tennis_copy_HSV, cv2.COLOR_BGR2HSV)
print(tennis_copy_HSV.shape)
plt.figure(figsize=(30, 20))

H_hist = cv2.calcHist([tennis_copy_HSV], [0], None, [180], [0, 180])
plt.plot(H_hist, color = 'r')
plt.show()

S_hist = cv2.calcHist([tennis_copy_HSV], [1], None, [255], [0, 255])
plt.plot(S_hist, color = 'g')
plt.show()

V_hist = cv2.calcHist([tennis_copy_HSV], [2], None, [255], [0, 255])
plt.plot(V_hist, color = 'b')
plt.show()

colours = ['r', 'g', 'b']
for i, colours in enumerate(colours):
    histogram = cv2.calcHist([tennis_copy_HSV], [i], None, [255], [0, 255])
    plt.plot(histogram, color= colours)
    plt.xlim(0, 255)
plt.show()


