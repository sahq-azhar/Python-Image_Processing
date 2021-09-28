import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):

    #capturing frames
    ret, frame = cap.read()
    
    #Display
    cv2.imshow('frame',frame)

    #keyboard interrupt
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()
cap.release()
