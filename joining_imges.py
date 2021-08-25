import cv2
import numpy as np
img = cv2.imread("Resources/lena.jpg")

#imghor = np.hstack((img,img))
imgVer = np.vstack((img,img))

#cv2.imshow("Horizontal",imghor)
cv2.imshow("Vertical",imgVer)

cv2.waitKey(0)