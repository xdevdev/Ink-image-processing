import cv2
import numpy as np

#cap = cv2.imread('C:/Users/Admin/Documents/dew/testblackink1.jpg')
cap = cv2.imread('C:/Users/Admin/Downloads/249427.jpg')


# Convert BGR to HSV
hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([0,0,0])
upper_blue = np.array([100,100,100])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(cap, lower_blue, upper_blue)

cv2.imshow('frame',cap)
cv2.imwrite('blackmask.png',mask)

img2 = cv2.imread('C:/Users/Admin/Documents/dew/blackmask.png')
dst = cv2.addWeighted(cap,1,img2,1,0)

cv2.imshow('img_blended' , dst)
cv2.imwrite('img_blended.jpg' , dst)
