import cv2
import numpy as np

img1 = cv2.imread("C:/Users/Admin/Documents/dew/inktest.jpg")
img2 = cv2.imread("C:/Users/Admin/Documents/dew/mask.png")

dst = cv2.addWeighted(img1,1,img2,1,0)

cv2.imshow('img_blended' , dst)

