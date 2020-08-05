import cv2
import numpy as np

#cap = cv2.imread('C:/Users/Admin/Documents/dew/inktest.jpg')
#cap = cv2.imread('C:/Users/Admin/Documents/dew/download.jpg')
#cap = cv2.imread('C:/Users/Admin/Documents/dew/newtest_perceptron.jpg')
cap = cv2.imread('C:/Users/Admin/Downloads/249427.jpg')

# Convert BGR to HSV
hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([0,0,0])
upper_blue = np.array([20,20,20])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(cap, lower_blue, upper_blue)

#cv2.imshow('frame',cap)
cv2.imwrite('mask.png',mask)

img2 = cv2.imread('C:/Users/Admin/Documents/dew/mask.png')

dst = cv2.addWeighted(cap,1,img2,1,0)

cv2.imshow('img_blended' , dst)




    
