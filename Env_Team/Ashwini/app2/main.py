import cv2
import time

first_frame = None
video = cv2.VideoCapture(0)
while True:

    check , frame = video.read()
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    grey = cv2.GaussianBlur(grey,(21,21),0)

    if first_frame is None:
        first_frame = grey
        continue

    delta_frame = cv2.absdiff(first_frame,grey)
    threshold_frame =  cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh_frame =  cv2.dilate(threshold_frame,None,iterations=2)

    (cnts,_) =  cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for countour in cnts:
        if cv2.contourArea(countour) > 1000:
            continue

        (x,y,w,h) = cv2.boundingRect(countour)
        cv2.rectangle(frame,(x,y),(x+w , y+h),(0,255,0),3)

    cv2.imshow("greyframe",grey)
    cv2.imshow("deltaframe",delta_frame)
    cv2.imshow("thresholdframe",thresh_frame)
    cv2.imshow("coloringfrsme",frame)
    key = cv2.waitKey(1)

    if key==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
