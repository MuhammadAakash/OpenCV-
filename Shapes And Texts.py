import cv2
import numpy as np
print("Imported Succeessfully")

img = np.zeros((512,512,3),np.uint8)

print(img)

# img[:] =(255 ,0,0)

# cv2.line(img , (0,0),(300,300) , (0,0,255),3)
cv2.line(img , (0,0),(img.shape[1] , img.shape[0]) , (0,0,255),3)
cv2.rectangle(img,(150,100),(200,200) , (255,0,0),3)
cv2.circle(img,(50,300),50,(0,255,0),5)
cv2.putText(img,"Aakash",(300,450),cv2.FONT_ITALIC , 1,(0,0,200),1)
cv2.imshow("image", img)
cv2.waitKey(0)