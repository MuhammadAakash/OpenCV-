import cv2
print("Imported Successfully")


# Reading and Showing Image in OpenCV
img = cv2.imread("Resources/Aakash.PNG")
cv2.imshow("output" , img)
cv2.waitKey(0)

# Reading and Showing Video in OpenCV
cap = cv2.VideoCapture('Resources/video.mp4')

while True:
    success,img = cap.read()
    cv2.imshow("output", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# Open Webcam using OpenCV

cap = cv2.VideoCapture(0)
cap.set(3,648)
cap.set(4,480)
cap.set(10,100)
while True:
    success,img = cap.read()
    cv2.imshow("output", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


