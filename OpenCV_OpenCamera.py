'''
OpenCamera for Python using opencv2
''' 

import cv
import cv2 
import sys
import copy
''' comment Windows rotation code first
IplImage* transposeImage(IplImage* image) {
 
	IplImage *rotated = cvCreateImage(cvSize(image->height, image->width),
		IPL_DEPTH_8U, image->nChannels);
	CvPoint2D32f center;
	float center_val = (float)((image->width) - 1) / 2;
	center.x = center_val;
	center.y = center_val;
	CvMat *mapMatrix = cvCreateMat(2, 3, CV_32FC1);
	cv2DRotationMatrix(center, 90, 1.0, mapMatrix);
	cvWarpAffine(image, rotated, mapMatrix,
		CV_INTER_LINEAR + CV_WARP_FILL_OUTLIERS,
		cvScalarAll(0));
	cvReleaseMat(&mapMatrix);
 
	return rotated;
}
 
IplImage *rotate_image(IplImage *image, int _90_degrees_steps_anti_clockwise)
{
	IplImage *rotated;
 
	if (_90_degrees_steps_anti_clockwise != 2)
		rotated = cvCreateImage(cvSize(image->height, image->width), image->depth, image->nChannels);
	else
		rotated = cvCloneImage(image);
 
	if (_90_degrees_steps_anti_clockwise != 2)
		cvTranspose(image, rotated);
 
	if (_90_degrees_steps_anti_clockwise == 3)
		cvFlip(rotated, NULL, 1);
	else if (_90_degrees_steps_anti_clockwise == 1)
		cvFlip(rotated, NULL, 0);
	else if (_90_degrees_steps_anti_clockwise == 2)
		cvFlip(rotated, NULL, -1);
 
	return rotated;
}
''' 
camera_index = -1 
capture = cv.CaptureFromCAM(camera_index)

isRunning = True
firstImage = copy.deepcopy(cv.QueryFrame(capture)) #drop first frame which might empty
cv.NamedWindow("Webcam",  cv.CV_WINDOW_AUTOSIZE);


def repeat():
	global capture #declare as globals since we are assigning to them now
	global camera_index
	global isRunning
	global firstImage
	c = cv.WaitKey(100)
	currImage = cv.QueryFrame(capture) 
	cv.ShowImage("Webcam",currImage)
	if(c==27):
		isRunning = False

while isRunning:
	repeat()
