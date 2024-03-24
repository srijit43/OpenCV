import cv2 as cv 

# img = cv.imread('Photos/cat_large.img') #resizing means decreasing height and width ( downsize)

# cv.imshow('Cat_large',img)

# resized_img = rescale_frame(img)

# cv.imshow('Cat_resized',resized_img)

def changeres(width, height): #only works for live video
    capt.set(3, width)
    capt.set(4, height)

def rescale_frame(frame, scale = 0.75):
    width = int(frame.shape[1] * 0.75)
    height = int(frame.shape[0] * 0.75)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capt = cv.VideoCapture('Videos/dog.mp4')

while True:  #reads the data frame by frame  until no more frames are available.
    isTrue, frame = capt.read()
    
    frame_resized = rescale_frame(frame, scale = 0.20)
    

    cv.imshow('Video',frame)
    cv.imshow('Video_resized', frame_resized)
    
    if cv.waitKey(20) & 0xFF == ord('d'):  #if the letter d is pressed
        break
    
capt.release()  #releases the video capture object from taking control
cv.destroyAllWindows()

cv.waitKey(0)