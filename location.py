import cv2
import numpy as np
import RPi.GPIO as GPIO

cl = [23,24,25]
GPIO.setmode(GPIO.BCM)
GPIO.setup(cl,GPIO.OUT)
GPIO.setup([12,16],GPIO.IN)

cap = cv2.VideoCapture(0)
while(True):
    print 'light hai masla'
    if (GPIO.input(12) == GPIO.HIGH):

        while(cap.isOpened()):

            ret,frame = cap.read()

            hsv_image = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

            lower = np.array([102,58,123])
            upper = np.array([117,197,240])

            binary_image = cv2.inRange(hsv_image,lower,upper)

            contours,heirarchy = cv2.findContours(binary_image,1,2)

            x = len(contours)
            if x>=1:
                largest = contours[0]
                if(x!=1):
                    i=1
                    for i in range(x-1):
                        cnt = contours[i]
                        a = cv2.contourArea(cnt)
                        b = cv2.contourArea(largest)
                        if a>b :
                            largest = cnt

                x,y,w,h = cv2.boundingRect(largest)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
                cx = (x+w)/2
                cy = (y+h)/2

                if cv2.contourArea(largest)>7000:
                    if cx<160:
                        print 'left'
                        GPIO.output(cl,(1,0,0))
                    elif cx>280:
                        print 'right'
                        GPIO.output(cl,(0,1,0))
                    elif 160<cx and cx<280:
                        print 'middle'
                        GPIO.output(cl,(0,0,1))
                    else:
                        print 'no where to be found'
                        GPIO.output(cl,(0,0,0))
                else:
                    print 'Not large enough'
            else:
                print 'no contour found'

            cv2.imshow('binary',binary_image)
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & GPIO.input(16) == (GPIO.HIGH):
                break
    elif (GPIO.input(16) == GPIO.HIGH):
        break
    else:
        print 'hmmm, aaai c'
    #set all the GPIO pins to zero (i.e. 23,24 & 25) is it holds the output as true even after quitting the loop

cv2.destroyAllWindows()
cap.release()
GPIO.cleanup()

