import cv2
import numpy as np
import matplotlib.pyplot as plt

color_coins = cv2.imread('img/coins5.jpg', cv2.IMREAD_COLOR)
rgb_coins = cv2.cvtColor(color_coins,cv2.COLOR_BGR2RGB)

# plt.figure(figsize = (12,8))
# plt.imshow(rgb_coins)
# plt.show()

gray_coins = cv2.cvtColor(rgb_coins, cv2.COLOR_RGB2GRAY)

coin_blur = cv2.GaussianBlur(gray_coins, (15, 15), 0)

cv2.imshow('Blur Coin', coin_blur)


edges_coin = cv2.Canny(coin_blur, 85, 255)
edges_copy = edges_coin.copy()
cv2.imshow("Edges", edges_coin)
cv2.waitKey(0)
cv2.destroyAllWindows()

contours2 = cv2.findContours(edges_copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

coins_with_contours = cv2.drawContours(edges_copy, contours2, -1, (0, 255, 0), 2)
cv2.imshow("First Contour", coins_with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()




