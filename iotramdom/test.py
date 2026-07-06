# import matplotlib.pyplot as plt
# import numpy as np

# x1 = np.array([5.2, 10.2, 15.2])
# y1 = np.array([10, 20, 30])

# x2 = np.array([6, 11, 16])
# y2 = np.array([12, 56, 78])

# plt.bar(x1, x2)
# plt.bar(x2, y2)
# plt.show()
# -----------------------------------------------------

# import matplotlib.pyplot as plt
# sizes = [100, 30, 20, 10]
# labels = ['A', 'B', 'C', 'D']
# plt.pie(sizes, labels=labels)
# plt.show ()
# -----------------------------------------------------

# import matplotlib.pyplot as plt
# import numpy as np

# x1 = np.array([10, 20, 45])
# x2 = np.array([10, 20 , 30])

# plt.scatter(x1, x2, color='r')
# plt.plot(x1, x2, color='b')
# plt.show()
# # ------------------------------------------------
# import matplotlib.pyplot as plt
# marks = [55, 60, 65, 70, 72, 75, 80, 85, 90, 95]
# plt.hist(marks, bins=3)
# plt.show()
# ---------------------------------------
# import matplotlib.pyplot as plt
# plt.subplot(1, 2, 1); plt.plot([1, 2, 3], [2, 4, 6])
# plt.subplot(1, 2, 2); plt.bar(["A","B"], [5, 7])
# plt.show()
# --------------------------------------------------
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.lineplot(x=[1,2,3],y=[10,20,15])
# plt.show()
# ---------------------------------------------------
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.barplot(x=['A', 'B', 'C'], y=[5,8,3])
# plt.show()
# ------------------------------------------------
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.scatterplot(x=[1,2,3,4],y=[10,20,15,20])
# plt.show()
# ---------------------------------
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.histplot([1,2,2,3,4,4,5])
# plt.show()
# -----------------------------
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.boxplot(y=[10,20,30,40])
# plt.show()
# ---------------------------------------
# import cv2
# import numpy as np

# # initialize the camera feed (0 is usually the default built-in camera)
# cap = cv2.VideoCapture(0)
# while True:
#     # capture frame by frame
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Convert BGR image to HSV color space
#     hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#     # Define the precise HSV threshold range for the color blue
#     # OpenCV HSV ranges: H(0-179), S(0-255), V(0-255)
#     lower_blue = np.array([90, 50, 50])
#     upper_blue = np.array([130, 255, 255])

#     # Create a binary mask where blue pixels are white, others are black
#     mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)

#     # Optional: clean up noise using morphological dilation
#     kernel = np.ones((5, 5), np.uint8)
#     mask = cv2.dilate(mask, kernel, iterations=1)

#     # Bitwise AND mask and original image to isolate the colored object
#     detected_output = cv2.bitwise_and(frame, frame, mask=mask)

#     # Display the results in separate windows
#     cv2.imshow('Original Camera Feed', frame)
#     cv2.imshow('Binary Mask Only', mask)
#     cv2.imshow('Isolated Color Output', detected_output)

#     # break the loop when the 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # clean up the windows and release camera source
# cap.release()
# cv2.destroyAllWindows()\

# ----------------------------------------------
# import cv2
# src = cv2.imread("download.png")
# gray_image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Grayscale Image", gray_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# ------------------------------
# import cv2
# image = cv2.imread('download.png')
# cv2.rectangle(image, (5, 5), (220, 220), (255, 0, 0), 2)
# cv2.imshow('Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# ----------------------------------------------------------
# import cv2
# img = cv2.imread('download.png')
# resized_fixed = cv2.resize(img, (400,300))
# res = cv2.resize(img, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
# cv2.imshow("resized & rotated", res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# -------------------------------------------------------------
import cv2
img = cv2.imread('download.png')
rot_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
rot_180 = cv2.rotate(img, cv2.ROTATE_180)
rot = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Resized & Rotated', rot)
cv2.waitKey()
cv2.destroyAllWindows()