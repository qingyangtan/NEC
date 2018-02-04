import numpy as np
import cv2
from cv2 import *
import pyaudio
import wave
import time
import stopWatch

ss_path = "/Users/home/Documents/NEC/screenshots"
video_path = "/Users/home/Documents/NEC/video"

cap = cv2.VideoCapture(0) 
cv2.namedWindow("pitch")
cv2.moveWindow("pitch",80,80)

# Get the width and height of frame
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
#print(width)
#print(height)

fourcc = cv2.VideoWriter_fourcc(*"mp4v") 
out = cv2.VideoWriter(video_path+"/output.mp4", fourcc, 20.0, (width, height))
start = time.time()
count = 0

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        out.write(frame)
        cv2.imshow('pitch',frame)

        end = time.time()
        secs = stopWatch.stopWatch(end-start)[1]
        if (secs % 30 == 0):
            imshow("pitch",frame)
            imwrite(ss_path+"/sreenshot"+str(count)+".jpeg",frame)
            count+=1
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
    else:
        break

end = time.time()         
#print(stopWatch.stopWatch(end-start))

out.release()
cap.release()
cv2.destroyAllWindows()
