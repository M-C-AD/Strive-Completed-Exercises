import cv2
import numpy as np

image1 = cv2.imread('img/SuperMan.jpg')
image2 = cv2.imread('img/TennisBall.jpg')
image3 = cv2.imread('img/noisy.png')
image4 = cv2.imread('img/SpiderMan.jpg')


super_m = image1.copy()
tennis = image2.copy()
copy_sup = super_m.copy()
copy_ten = tennis.copy()

blur_ker = np.ones((3, 3), np.float32)/9
blur_ker2 = np.ones((5, 5), np.float32)/25  # increasing the size of the kernel increases the blur
blur_ker3 = np.ones((7, 7), np.float32)/49

blur_sup = cv2.filter2D(copy_sup, -1, blur_ker2)
blur_ten = cv2.filter2D(copy_ten, -1, blur_ker2)
cv2.imshow('Original Super', super_m)
cv2.imshow('Original Tennis', tennis)
cv2.imshow('Blur Sup', blur_sup)
cv2.imshow('Blur Tennis', blur_ten)

copy_sup2 = super_m.copy()
copy_ten2 = tennis.copy()
gau_blur1 = cv2.GaussianBlur(copy_sup2, (7, 7), 0)
gau_blur2 = cv2.GaussianBlur(copy_ten2, (7, 7), 0)
cv2.imshow('Blur2 Sup', gau_blur1)
cv2.imshow('Blur2 Tennis', gau_blur2)

blurV2 = cv2.blur(copy_sup2, (3, 3))
medianBl = cv2.medianBlur(copy_sup2, 5)
bLat = cv2.bilateralFilter(copy_sup2, 9, 75, 100)
noiblur = cv2.bilateralFilter(image3, 9, 75, 100)

cv2.imshow('Averaging Blur', blurV2)
cv2.imshow('Median Blur', medianBl)
cv2.imshow('Bilateral Blur', bLat)

cv2.imshow('Original noisy', image3)

cv2.waitKey(0)
cv2.destroyAllWindows()

shNoisy = image4.copy()
sharpen_matrix = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

dress_sharp = cv2.filter2D(shNoisy, -1, sharpen_matrix)

cv2.imshow('Original Noisy', shNoisy)
cv2.imshow('Sharp Noisy', dress_sharp)


edge_matrix = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
noisyEdge = cv2.filter2D(image4, -1, edge_matrix)
cv2.imshow('Edges Noisy', noisyEdge)

# gray_dress = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)

sobel_ed_x = cv2.Sobel(image4, cv2.CV_64F, 0, 1, ksize= 5)
sobel_ed_y = cv2.Sobel(image4, cv2.CV_64F, 1, 0, ksize= 5)
combined_sob = cv2.bitwise_or(sobel_ed_x, sobel_ed_y)
cv2.imshow('Sob X', sobel_ed_x)
cv2.imshow('Sob Y', sobel_ed_y)
cv2.imshow('Sob combined', combined_sob)

laplacian_edg = cv2.Laplacian(image4, cv2.CV_64F)
cv2.imshow('Laplacian Edge', laplacian_edg)

canny_edg = cv2.Canny(image4, 60, 180)
cv2.imshow('Canny Edge', canny_edg)

cv2.waitKey(0)
cv2.destroyAllWindows()


