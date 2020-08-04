
import cv2
import numpy as np

image = cv2.imread('C:/Users/Admin/Documents/dew/inktest.jpg')

lower_blue = np.array([110,50,50])
upper_blue = np.array([220,255,255])

color = cv2.inRange(image, lower_blue, upper_blue)

image[np.where((image== list(range(lower_blue , upper_blue))).all(axis=2))]=[255,255,255]
cv2.imshow('imgfinish.png',image)
    
