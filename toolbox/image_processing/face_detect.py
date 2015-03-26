""" Experiment with face detection and image filtering using OpenCV """

import cv
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/home/caz/haarcascade_frontalface_alt.xml')
kernel = np.ones((40,40),'uint8')

while(True):
	#capture frame by frame
	#ret, frame = cap.read()


	ret, frame = cap.read()
	faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize = (20,20))
	for (x,y,w,h) in faces:
		frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
		cv2.ellipse(frame,(x+w/2, y+2*h/3), (w/3, h/8), 0, 180, 0, (0, 0, 0), 5)
		cv.Circle(cv.fromarray(frame), (x+w/4, y+h/3), 10, (255,255,255), 5)
		cv.Circle(cv.fromarray(frame), (x+3*w/4, y+h/3), 10, (255,255,255), 5)
		cv.Circle(cv.fromarray(frame), (x+w/4, y+h/3), 3, (0,0,0), 5)
		cv.Circle(cv.fromarray(frame), (x+3*w/4, y+h/3), 3, (0,0,0), 5)
		#cv2.rectangle(frame,(x,y),(x+w, y+h),(0,0,255))

	#display the frame
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


#release the capture
cap.release()
cv2.destroyAllWindows()