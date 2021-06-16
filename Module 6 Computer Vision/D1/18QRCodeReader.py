import cv2
import numpy as np



image = cv2.imread('img/QR1.png')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
QR1 = image_gray.copy()

qrCodeDetector = cv2.QRCodeDetector()

decodedText, points, _ = qrCodeDetector.detectAndDecode(QR1)
# print(points)
# print(type(points))

if points is not None:
    # QR Code detected handling code
    nrOfPoints = len(points)
    print("QR Code detected")
    for i in range(nrOfPoints):
        nextPointIndex = (i + 1) % nrOfPoints
        check_tuple = tuple(points[i][0])
        print(type(check_tuple))
        print(points[i][0])
        cv2.line(QR1, tuple(points[i][0]), tuple(points[nextPointIndex][0]), (255, 0, 0), 5)
        # cv2.line(QR1,)
    print(decodedText)
    cv2.imshow("QR Code", QR1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("QR code not detected")

# image = cv2.imread('img/QR1.png')
#
# qrCodeDetector = cv2.QRCodeDetector()
#
# decodedText, points, _ = qrCodeDetector.detectAndDecode(image)
#
# if points is not None:
#
#     nrOfPoints = len(points)
#
#     for i in range(nrOfPoints):
#         # nextPointIndex = (i + 1) % nrOfPoints
#         # cv2.line(image, tuple(points[i][0]), tuple(points[nextPointIndex][0]), (255, 0, 0), thickness=5)
#
#         point1 = tuple(points[i][0])
#         point2 = tuple(int(points[(i + 1) % nrOfPoints][0]))
#         cv2.line(image, point1, point2, color=(255, 0, 0), thickness=2)
#
#     print(decodedText)
#
#     cv2.imshow("Image", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
#
# else:
#     print("QR code not detected")
#
# cv2.line(image, (16, 16), (20, 20), color=(255, 0, 0), thickness=20)
# cv2.imshow("Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
