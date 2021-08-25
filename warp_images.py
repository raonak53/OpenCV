import cv2
import numpy as np

img = cv2.imread("Resources/card.jpg")

width,height = 250,350
pts1 = np.float32([[2,50],[280,180],[154,450],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

#cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)