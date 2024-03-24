import cv2 as cv
import numpy as  np

blank = np.zeros((500,500,3),dtype='uint8') #creates a blank image of 500 by 500 and number of color channels
# cv.imshow('Blank',blank)                   #displays the blank image in window named 'Blank'

# # Paint the image a certain color lets start with the basics

# # blank[:] = 0,0,255                #This will turn the whole image green  (BGR format)

# blank[200:300, 300:400]  = 0,0,255           # This is how you can select parts of an array using slicing to paint a part of the image

# cv.imshow('Red', blank)


# img = cv.imshow('Photos/cat.jpg')
# cv.imshow('Cat',img)


# Draw a rectangle

cv.rectangle(blank,(0,0),(250,500),(0,0,255),thickness=-1) #Draws a blue rectangle from point (0,0) to point (250,250) with color red and thickness of pencil = 2

#cv.imshow('Rectangle', blank)


cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),70 ,(0,255,0),thickness=1) #takes in the centre, radius, color, thickness when thickness is -1 it fills the circle
#cv.imshow('Circle',blank)

cv.line(blank,(100,250),(blank.shape[1]//2, blank.shape[0]//2),(255,255,255),thickness = 3)
cv.imshow('My drawing',blank)


cv.waitKey(0)
