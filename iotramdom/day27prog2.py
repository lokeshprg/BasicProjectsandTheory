# Day 27: Program 2

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\lokes\OneDrive\Desktop\RandomElecTheory\iotramdom\shapes.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for i, contour in enumerate(contours):
    if i==0:
        continue

    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)

    cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)

    M = cv2.moments(contour)
    if M['m00'] != 0:
        x = int(M['m10']/ M['m00'])
        y = int(M['m01']/ M['m00'])

sides = len(approx)
if sides ==3:
    label="triangle"
elif sides==4:
    label="Quadrilateral"
elif sides==5:
    label = "Pentagon"
elif sides==6:
    label = "Hexagon"
else:
    label = "Circle"

    cv2.putText(img, label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
