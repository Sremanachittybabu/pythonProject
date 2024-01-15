import cv2
import time
import pandas
from datetime import datetime


first_frame = None
status_list = [None,None]
times = []
df5 = pandas.DataFrame(columns=["start","end"])
video = cv2.VideoCapture(0)
while True:

    check , frame = video.read()
    status = 0
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
        if cv2.contourArea(countour) < 10000:
            continue
        status = 1
        (x,y,w,h) = cv2.boundingRect(countour)
        cv2.rectangle(frame,(x,y),(x+w , y+h),(0,255,0),3)
    status_list.append(status)
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())

    cv2.imshow("greyframe",grey)
    cv2.imshow("deltaframe",delta_frame)
    cv2.imshow("thresholdframe",thresh_frame)
    cv2.imshow("coloringfrsme",frame)
    key = cv2.waitKey(1)

    if key==ord('q'):
        if status==1:
            times.append(datetime.now())
        break

for i in range(0,len(times),2): 
    #df = df.append({"Start":times[i],"End":times[i+1]}, ignore_index = True)
     df5 = df5.add(1)
    
df5.to_csv("times.csv")    
video.release()
cv2.destroyAllWindows()
