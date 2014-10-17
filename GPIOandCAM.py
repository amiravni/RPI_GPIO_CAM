import RPi.GPIO as GPIO
import time
import os.path
from cv2 import *
import numpy as np
cap = VideoCapture(0)
fourcc = cv.CV_FOURCC(*'XVID')
fps=5
second2record=5
fileName = "./TurnOn.txt"
filecount=0
while True:
	if os.path.isfile(fileName):
		vidName = "output" + str(filecount) + ".avi"
		out = VideoWriter(vidName,fourcc, fps, (640,480))
		filecount=filecount+1
		count=0		
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(24, GPIO.OUT)
		HighFlag=False
		while(cap.isOpened() and count <= fps*second2record ):
			ret, frame = cap.read()
			count = count + 1
			if ret==True:	
				out.write(frame)			
			else:
					break
			if HighFlag==False:
				os.remove(fileName) 
				GPIO.output(24,True)
				HighFlag=True
				print("24 is HIGH")

		GPIO.output(24,False)
		print("24 is LOW")
		GPIO.cleanup()
		out.release()

cap.release()
