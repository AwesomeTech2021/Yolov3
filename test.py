import cv2
import numpy as np
import time

img = cv2.imread('image.jpg')
cv2.imshow('asda',img)
font1 = cv2.FONT_HERSHEY_SIMPLEX

while 1:
	copied = img.copy()
	t = time.strftime('%H:%M:%S')
	copied = cv2.rectangle(copied,(0,480), (400,400), (0,255,0),-1)
	copied = cv2.putText(copied,t,(0,480),font1,2,(255,255,255),5)
	cv2.imshow('frame',copied)
	k = cv2.waitKey(10)
	if k == 27:
		break

cv2.destroyAllWindows()
