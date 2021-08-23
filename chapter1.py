import cv2
print("completed")

img = cv2.imread("Resources/lena.jpg")
cv2.imshow("Output",img)
cv2.waitKey(0)