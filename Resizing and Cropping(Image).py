import cv2
print("Imported Successfully")

img = cv2.imread("Resources/Aakash.PNG")

imgResize = cv2.resize(img ,(300,250))

imgCropped = img[0:450, 0:350]

cv2.imshow("image",img)
# cv2.imshow("Resize Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)
