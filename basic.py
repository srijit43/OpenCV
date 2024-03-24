#converting an image to greyscale

import cv2 as cv 

img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  #grayscale  conversion
# cv.imshow('Gray',gray)

#blurring an image

blur = cv.GaussianBlur(img, (5,5),cv.BORDER_DEFAULT)   #kernel size and sigma value ( kernel has to be an odd numer) , you can increase blur by increasing kernel size
# cv.imshow('Blurry', blur)

#How to find an edge cascade

edge = cv.Canny(img, 125, 175) # threshold values
# cv.imshow("Edge", edge)

# How to dilate an image using a structural  element (kernel)

dilate = cv.dilate(edge, (3,3),iterations=3)
cv.imshow('Dilated', dilate)


#resize

resized = cv.resize(img,(400,600), interpolation=cv.INTER_AREA)  #resizes without considering aspect ratio
cv.imshow('Resized',resized)

cv.waitKey(0)
