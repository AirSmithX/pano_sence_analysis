__author__ = 'Air'

import cv2

image = cv2.imread("F:\pano256x128\indoor\living_room\pano_aswzkvlbskeqzz.jpg")
cv2.imshow("show", image)
cv2.waitKey(0)

for x in range(100, 200):
    patch = image[40:90, x:x+60]
    cv2.imshow("show2", patch)
    cv2.waitKey(0)
