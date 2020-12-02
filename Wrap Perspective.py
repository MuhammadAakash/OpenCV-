import cv2
import numpy as np
print("Imported Successfully")

width , height = 250, 350
img = cv2.imread("Resources/cards.jpg")

pts1 = np.float32([[145,297],[145,887],[524,297],[524,887]])
pts2 = np.float32([[0, 0], [0, height], [width, 0], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))


cv2.imshow("output",img)
cv2.imshow("Wrap Output" , imgOutput)
cv2.waitKey(0)