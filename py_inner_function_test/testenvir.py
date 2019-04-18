import cv2

videocapture = cv2.VideoCapture(0)

frame,grab = videocapture.read()
frame,grab = videocapture.read()

cv2.imshow('test',frame)
cv2.waitKey(10000)
