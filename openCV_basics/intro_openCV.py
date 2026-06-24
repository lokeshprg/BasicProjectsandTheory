# to install openCV : pip install opencv-python
# (Reading an image)------------->>>
# importing openCV library
import cv2

# reading the image
image = cv2.imread("openCV_basics/roadTraffic.jpg")

# saving the dimensions of the image in the h ,w variables
h, w = image.shape[:2]
cv2.imshow("Original Image", image)
print("height={}, width={}".format(h, w))

# Extracting the RGB value of pixel, Here we have chosen random value of an pixel by passing the 100, 100 for height and width
(G, B, R) = image[100, 100]
print("G={}, B={}, R={}".format(G, B, R))

# Extracting the region of interest (ROI)
# Slicing the pixels of the image
roi = image[100:400, 300:500]
# Creating the window to display the image
cv2.imshow("ROI", roi)
# The window will remain open until you press any key
cv2.waitKey(0)
a, b = roi.shape[:2]
print("height={}, width={}".format(a, b))

# Resize an image, resize() function takes two paremeters, the image and the dimensions
resize = cv2.resize(image, (100, 500))
cv2.imshow("resized Image", resize)
cv2.waitKey(0)

# To maintain the aspect ratio of the image while resizing
# Calculating the ratio
ratio = 800/w
# Creating a tuple containing width and height
dim = (800, int(h*ratio))
# Resizing the tuple
resize_aspect = cv2.resize(image, dim)
cv2.imshow("Resize Aspect", resize_aspect)
cv2.waitKey(0)

# Drawing the rectangle using rectangle() function, it takes 5 arguments
# 1.Image
# 2.Top-Left corner coordinates
# 3.Bottom-Right corner coordinates
# 4.Color (in BGR format)
# 5.Line width

# Copying the original image
rectangle_copy = image.copy()
rectangle = cv2.rectangle(rectangle_copy, (100, 200), (400, 500), (0, 0 ,255), 5)
cv2.imshow("Rectangle", rectangle)
cv2.waitKey(0)

# Displaying text on the image, using putText() function, It takes 7 arguments
'''1. image
2. Text to be displayed
3. Bottom left corner, from where the text should start
4. font 
5. font size 
6. color (in BGR format)
7. line width'''

# Copying the original image
text_copy = image.copy()
text = cv2.putText(text_copy, "Hello World!", (500, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
cv2.imshow("Text", text)
cv2.waitKey(0)