import cv2 as cv 

#img = cv.imread('Photos/cat_large.jpg')  #takes path of an image and returns it as a matrix of pixels

#cv.imshow('Cat',img)   #commnad to show the image read  by 'imread' in a window named 'Cat'.

#cv.waitKey(0)  #keyboard binding function, waits for a key to be pressed

#open cv does not have a way to mitigate the issue where the image exceeds monitor size

#reading videos in openCV

capt = cv.VideoCapture('Videos/dog.mp4')  #this takes a path or an integer like 0,1,2 ( if we are using webcam or camera)

while True:  #reads the data frame by frame  until no more frames are available.
    isTrue, frame = capt.read() #returns two values, one boolean value indicating if any frames were read from the video file, and another containing the    #this loop will run until any key is pressed
    cv.imshow('Video',frame)
    
    if cv.waitKey(20) & 0xFF == ord('d'):  #if the letter d is pressed
        break
    
capt.release()  #releases the video capture object from taking control
cv.destroyAllWindows()

#cv.waitKey(0)

    
    
    


