import cv2
import matplotlib.pyplot as plt
from scipy.stats import skew
import numpy as np

image1 = cv2.imread('img/day3.jpg')
# image1 = cv2.imread('img/night4.jpg')

day3_HSV = image1.copy()
day3_HSV = cv2.cvtColor(day3_HSV, cv2.COLOR_BGR2HSV)
# print(day3_HSV.shape)
plt.figure(figsize=(30, 20))

# H_hist = cv2.calcHist([day3_HSV], [0], None, [180], [0, 180])
# plt.plot(H_hist, color = 'r')
# plt.show()
#
# S_hist = cv2.calcHist([day3_HSV], [1], None, [255], [0, 255])
# plt.plot(S_hist, color = 'g')
# plt.show()

V_day_hist = cv2.calcHist([day3_HSV], [2], None, [255], [0, 255])
plt.plot(V_day_hist, color = 'b')
# plt.show()

# colours = ['r', 'g', 'b']
# for i, colours in enumerate(colours):
#     histogram = cv2.calcHist([day3_HSV], [i], None, [255], [0, 255])
#     plt.plot(histogram, color= colours)
#     plt.xlim(0, 255)
# plt.show()

################################################### NIGHT

image3 = cv2.imread('img/night2.jpg')

night2_HSV = image3.copy()
night2_HSV = cv2.cvtColor(night2_HSV, cv2.COLOR_BGR2HSV)
# print(night2_HSV.shape)
# plt.figure(figsize=(30, 20))

# H_hist = cv2.calcHist([night2_HSV], [0], None, [180], [0, 180])
# plt.plot(H_hist, color = 'r')
# plt.show()
#
# S_hist = cv2.calcHist([night2_HSV], [1], None, [255], [0, 255])
# plt.plot(S_hist, color = 'g')
# plt.show()

V_night_hist = cv2.calcHist([night2_HSV], [2], None, [255], [0, 255])
plt.plot(V_night_hist, color = 'b')
# plt.show()

# colours = ['r', 'g', 'b']
# for i, colours in enumerate(colours):
#     histogram = cv2.calcHist([night2_HSV], [i], None, [255], [0, 255])
#     plt.plot(histogram, color= colours)
#     plt.xlim(0, 255)
# plt.show()


# print(V_day_hist.shape)
# print('****************************************')
# print(V_night_hist.shape)

# print(V_day_hist)

sum_day = V_day_hist.sum()
# day_mean = sum_day / 255
day_mean = np.mean(V_day_hist)
day_std = np.std(V_day_hist)
day_median = np.median(V_day_hist)

day_skew =3 *(day_mean - day_median)/day_std

sum_night = V_night_hist.sum()
# night_mean = sum_night / 255
night_mean = np.mean(V_night_hist)
night_std = np.std(V_night_hist)
night_median = np.median(V_night_hist)
night_skew =3 *(night_mean - night_median)/night_std

if day_skew < 1:
    print('DAY')
else:
    print('NIGHT')

print(day_mean)
print(day_std)
print(night_mean)
print(night_std)
print(day_skew)
print(night_skew)


# Test of another idea
if skew(V_day_hist) < 2:
    value = True
    print(skew(V_day_hist))
else:
    value = False
    print(skew(V_day_hist))
print(value)
#above is a test of another idea


# day_skew = skew(V_day_hist, 0, bias= False)
# night_skew = skew(V_night_hist, 0, bias= True)
# print(day_skew)
# print(night_skew)


