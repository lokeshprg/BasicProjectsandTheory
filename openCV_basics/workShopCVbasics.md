# Introduction to OpenCV
OpenCV is one of the most popular computer vision library.

## Reading an Image
```
import cv2
image = cv2.imread("roadTraffic.jpg")
h, w = image.shape[:2]
print("Height={}, width={}".format(h, w))
```

## Extracting the RGB value of pixel
```
(B, G, R) = image[100, 100]
print("R={}, G={}, B={}".format(R, G, B))
# To pass the specific channel
B = image[100, 100, 0]
print("B={}".format(B))
```

## Extracting the region of interest
```
roi = image[100:500, 200:700]
cv2.imshow("ROI", roi)
cv2.waitKey(0)
```

## Resizing the Image
```
resize = cv2.resize(img, (500, 500))
cv2.imshow("Resize", resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
In this method the aspect ratio of the image is not maintained, so we have to do some extra work in order to mainatain the aspect ratio.
```
ratio = 800/w
dim = (800, int(h*ratio))
resize_aspect = cv2.resize(img, dim)
cv2.imshow("Resized", resize_aspect)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## Drawing a rectangle
We can draw rectangle on the image using rectangle() method. 
It takes in 5 arguments:
- Image
- Top-left corner co-ordinates
- Bottom-right corner co-ordinates
- color in BGR format
- Line Width

```
# We are copying the original image as it is an in-place operation.
output = img.copy()
rectangle = cv2.rectangle(output, (1500, 900), (600, 400), (0, 0, 255), 4)
```

## Displaying text
We can also display the text on the image using putText() method of openCV module, It is an in-place operation.
It takes 7 arguments:
- Image
- Text to be displayed
- Bottom Left-Corner Coordinates, from where the text should start
- Font
- Font Size
- Color (in BGR format)
- Line Width

```
output = image.copy()
text = cv2.putText(img, 'OpenCV demo', (500, 500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0),2)
```

# Color Spaces
A color space is a method that tells the computer how to store, organize, and understand colors. Just as different maps are designed for different purposes (road maps, weather maps, political maps), different color spaces are designed to make different image-processing tasks easier.
OpenCV provides several color spaces that are that are used in image processing:
## 1. RGB (Red, Green , Blue)
RGB coor model represents the colors using three primary colors red, green and blue. This is the standard color space used to display images on the screen and working with digital images.
## 2. BGR (Blue, Green, Red)
OpenCv uses BGR instead of RGB as its default color space.
## 3. HSV (Hue, Stauration, Value)
HSV is another color space used in OpenCV. It splits color information in to three components:
1. Hue: Represents the color itself.
2. Saturation: shows the vibrancy of the color.
3.Value: defines the brightness of the color.
The *hue value ranges from 1 to 179*, while *the saturation and value range from 0 to 255.*
It is useful for *color segmentation and object detection* as it easily isolates the colors in an image.
## 5.CMYK (Cyan, Magneta, Yellow, Black)
CMYK color model is used for color printing. it's a subtractive color model, means colors are created by subtracting light usnig different combination of cyan, magneta, yellow, black inks
## 6.Grayscale
A grayscale image contains only shades of gray, with each pixel representing the different intensity level from black to white. It is used when color information is not needed such as in edge detection and thresholding task.
```
import cv2
img = cv2.imread("img.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

cv2.imshow("Original Image", img)
cv2.imshow("RGB", img_rgb)
cv2.imshow("HSV", img_hsv)
cv2.imshow("GRAY", img_gray)
cv2.imshow("LAB", img_lab)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

***Detecting red color in an image using HSV***
The HSV color space is often preffered over the RGB color space for the tasks like color detection and color segmentation because it seperates the color from the brightness.
mask = cv2.inRange(img_hv, lower_red, upper_red): cv2.inRange() creates a mask that isolates the red area of the image based on the defined range.
result = cv2.bitwise_and(img, img, mask=mask): The mask is applied to the mask is applied to the original image using cv2.bitwise_and() to keep only the red regions.
```
import cv2
import numpy as np

img = cv2.imread('img.jpg')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

mask = cv2.inRange(img_hsv, lower_red, upper_red)
result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Red", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

***Visualizing different color channels in the image***
Now we will break down an RGB image into its individual color channels; Reg, Blue, Green and display each channel seperately.
```
import cv2
img = cv2.imread("img.jpg")

B, G, R = cv2.split(img)
cv2.imshow(img)
cv2.waitKey(0)

cv2.imshow(B)
cv2.waitKey(0)

cv2.imshow(G)
cv2.waitKey(0)

cv2.imshow(R)
cv2.waitKey(0)

cv2.destroyAllWindows()
```

# Image blurring using OpenCV
Image processing is the technique used in image processing to reduce the sharpness and detail making an image appear smoother. This is done by filters also known as low-pass filters that reduce-high frequency noise and smooth finer details.
It works by averaging the pixel value around each pixel, softening the image in the process.

# Important Functions in OpenCV
***cv2.imread() method***
*Syntax*: cv2.imread(filename, flag)

*where,*
1. Filename: specifies the path of the image file
2. Flag: specifies the wy how the image should be read which can be:
    - **cv2.IMREAD_COLOR**: It specifies to load color image. It is default flag. Alternatively we can pass integer value 1 for this flag.
    - **cv2.IMREAD_GRAYSCALE**: It specifies to load an image in grayscale mode. Alyernatively we can pass interger value 0 for this flag.
    -**cv2.IMREAD_UNCHANGED**: It specifies to load an image such as including alpha channel. Alternatively we can pass integer value -1 for this flag

The cv2.imread() return an numpy array if the image is loaded successfully.

***cv2.imshow()***
It is used to display image in the window. It creates a window with a specified name and shows the given image.
In the below example the sampe image is loaded and displayed in the window:
```
import cv2

img = cv2.imread("logo.png")
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
*Syntax*: cv2.imshow(window_name, image)

**Example 1:**:
In this exmaple, an image is loaded in grayscale mode and displayed.
```
import cv2

img = cv2.imread("logo.png", 0)
cv2.imshow("Gray Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

***cv2.imwrite()***
cv2.imwrite() is an function used to save an image in storage in any supported format such as JPG, PNG or BMP.
Loading an image and saving with the new name in the same directory.
```
import cv2
img = cv2.imread("logo.png")
cv2.imwrite("NEW_NAME.png", img)
```

*Syntax*: cv2.imwrite(filename, image)
Parameters
- filename: Output file name using extension
- image: image array to save

***cv2.resize()***
OpenCV provides the cv2.resize() function, that allows you to resize the images efficiently. By selecting different interpolation methods, you can control the balance between image quality and resizing speed.

*Syntax*: cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation[, ]]]]])
Parameters
- src: Source/input image.
- dsize: desired size (width, height)
- dst(optional): Output image, rarely used explicitly.
- fx(optional): Scale factor along the horizontal axis.
- fy(optional): scale factor along the vertical axis.
- interpolation: interpolation method to use.

*Use either dsize or fx/fy for scaling,*
*dsize: when you know exact width/height*
*fx/fy: When you want to scale by a factor.*
*Never set both together (unless dize=None)*

**Interpolation Methods**
Interpolation is used to decide the pixel color when a image u=is resized.
|Method|When to use|Description|   
|------|-----------|-----------|
|cv2.INTER_AREA|Shrinking|Minimizes distortion while downscaling|
|cv2.INTER_LINEAR|General Resizing|Balances speed and quality|
|cv2.INTER_CUBIC|Enlarging|Higher quality for upscaling|
|cv2.INTER_NEAREST|Fast resizing|Quick but lower quality|

*Example of resizing images in OpenCV*
```
import cv2
import matplotlib.pyplot as plt

image = cv2.read("image.jpg")

small = cv2.resize(image, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_AREA)

large = cv2.resize(image, (1050, 1610), interpolation=cv2.INTER_CUBIC)
medium = cv2.resize(imagem, (780, 540), interpolation=cv2.INTER_LINEAR)

titles = ["Original", "10% (INTER AREA)", "1050x1610 (INTER CUBIC)", 780x540 (INTER LINEAR)]
images = [image, small, large, medium]

plt.figure(figsize=(10, 8))
for i in range(4):
    plt.subpolt(2, 2, i+1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))

    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()
```