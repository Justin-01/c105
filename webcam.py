import cv2
link = cv2.VideoCapture(0)
while True:
    status, frame = link.read()
    cv2.imshow('WebCam', frame)
    if(cv2.waitKey(30) == 32):
        break








