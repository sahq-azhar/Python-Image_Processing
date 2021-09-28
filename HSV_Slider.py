import cv2
import numpy as np

#empty function
def callback(x):
    pass

cap = cv2.VideoCapture(0);

#creating a window named HSV_Slider
cv2.namedWindow("HSV_Slider")

#creating trackbars
cv2.createTrackbar("Hue_Low", "HSV_Slider", 0, 255, callback)
cv2.createTrackbar("Hue_High", "HSV_Slider", 255, 255, callback)

cv2.createTrackbar("Saturation_Low", "HSV_Slider", 0, 255, callback)
cv2.createTrackbar("Saturation_High", "HSV_Slider", 255, 255, callback)

cv2.createTrackbar("Value_Low", "HSV_Slider", 0, 255, callback)
cv2.createTrackbar("Value_High", "HSV_Slider", 255, 255, callback)

while(cap.isOpened()):
    #capturing frames
    _, frame = cap.read()
    
    #converting to hsv image
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #getting track bar values
    hue_low = cv2.getTrackbarPos("Hue_Low", "HSV_Slider")
    hue_high= cv2.getTrackbarPos("Hue_High", "HSV_Slider")
    
    saturation_low = cv2.getTrackbarPos("Saturation_Low", "HSV_Slider")
    saturation_high = cv2.getTrackbarPos("Saturation_High", "HSV_Slider")
    
    value_low = cv2.getTrackbarPos("Value_Low", "HSV_Slider")
    value_high = cv2.getTrackbarPos("Value_High", "HSV_Slider")

    low = np.array([hue_low, saturation_low, value_low])
    high = np.array([hue_high, saturation_high, value_high])

    masked_image = cv2.inRange(hsv_image, low, high)

    #Display
    cv2.imshow("Camera Input", frame)
    cv2.imshow("Masked Output", masked_image)

    #keyboard interrupt
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
cap.release()
