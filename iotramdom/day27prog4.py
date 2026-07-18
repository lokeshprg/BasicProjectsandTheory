import cv2
import numpy as np

frame_width = 640
frame_height = 480

cap = cv2.VideoCapture(0)
cap.set(3, frame_width)
cap.set(4, frame_height)

def empty(a):
    pass

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameter", 640, 240)
cv2.createTrackbar("Threshold1", "Parameter", 23, 255, empty)
cv2.createTrackbar("Threshold2", "Parameter", 20, 255, empty)
cv2.createTrackbar("Area", "Parameter", 5000, 30000, empty)

def stackImages(scale, imgArray):
    row = len(imgArray)
    col = len(imgArray[0])
    rows_availaible = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rows_availaible:
        for x in range(0, row):
            for y in range(0, col):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale)
                else:
                    imgArray[x][y]=cv2.resize(imgArray[x][y], imgArray[0][0].shape[0], None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*row
        hor_con = [imageBlank]*row
        for x in range(0, row):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, row):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                cv2.resize(imgArray[x], (0, 0), None, scale, scale)

                cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)