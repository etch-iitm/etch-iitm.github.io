import cv2
import numpy as np 
import glob

for image_name in glob.glob('*.jpg') :
	image = cv2.imread(image_name)
	resized = cv2.resize(image,(500,300))
	cv2.imwrite(image_name[:-4] + '_resized' + '.jpg',resized)
	print('resized ' + image_name)