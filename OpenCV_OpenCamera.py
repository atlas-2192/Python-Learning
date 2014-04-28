'''
OpenCamera for Python using opencv2
For install OpenCV for Python Check this in Mac
http://www.jeffreythompson.org/blog/2013/08/22/update-installing-opencv-on-mac-mountain-lion/
''' 

import cv2.cv as cv
import cv2
import sys
import copy
'''
def rotate_camera(currImage, _90_degrees_steps_anti_clockwise):
	if (_90_degrees_steps_anti_clockwise != 2):
		rotatedImage = cv.CreateImage(cv.cvGetSize(cvSize(currImage), 8, 3)
		# YUV: 8, 3
		# GRAY: 8,1
	else
		rotatedImage = cv.CloneImage(currImage)
 
	if (_90_degrees_steps_anti_clockwise != 2):
		cvTranspose(currImage, rotatedImage);
 
	if (_90_degrees_steps_anti_clockwise == 3):
		cv.cvFlip(rotatedImage, null, 1)
	else if (_90_degrees_steps_anti_clockwise == 1):
		cv.cvFlip(rotated, NULL, 0)
	else if (_90_degrees_steps_anti_clockwise == 2):
		cv.cvFlip(rotated, NULL, -1);
	return rotatedImage
'''
def repeat():
	global capture #declare as globals since we are assigning to them now
	global camera_index
	global isRunning
	global firstImage
	global rotation_angle
	currImage = cv.QueryFrame(capture) 
	cv.ShowImage("Webcam",currImage)
	'''
	Note:
		WaitKey only receive key from the windows you create not python command line windows :)
	'''
	c = cv.WaitKey(10) 

	if(c==27):
		isRunning = False
	if (c!=-1):
		print str(c)
	if (c==63235): # "->" key
		rotation_angle = (rotation_angle + 90) % 360
		print "rotation angle = "+ str(rotation_angle)
	elif (c==63234): # "<-" key
		rotation_angle = (rotation_angle +270) % 360
		print "rotation angle = "+ str(rotation_angle)
		#rotate_camera(currImage, 1)


#Main
camera_index = -1 
rotation_angle = 0
capture = cv.CaptureFromCAM(camera_index)

isRunning = True
firstImage = copy.deepcopy(cv.QueryFrame(capture)) #drop first frame which might empty
cv.NamedWindow("Webcam",  cv.CV_WINDOW_AUTOSIZE);

while isRunning:
	repeat()

#Release resource
cv2.VideoCapture.release() 
cv.DestroyWindow("Webcam")