import cv2
import numpy as np
print("Imported Successfully")

#            # Convert image to  Gray Scale Image and Blured Image
img = cv2.imread("Resources/Aakash.PNG")
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray ,(7,7) , 0)
imgCanny = cv2.Canny(img , 150,200)
imgDialat = cv2.dilate(imgCanny,kernel , iterations=1) # for Thinkness
imgEroded = cv2.erode(imgDialat , kernel, iterations=1) # for thinness

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blured Image", imgBlur)
cv2.imshow("Edges ", imgCanny)
cv2.imshow("Dialation Image ", imgDialat)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)


