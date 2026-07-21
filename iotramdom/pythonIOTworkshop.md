# Python
- Open source general purpose language.
- object oriented, Procedural, Functional.
- Easy to interface with C/ObjC/Java.
- Great interactive environment.
- No compilation needed i.e. interpreted.

## Softwares
- Visual Studio Code.
- Python (from python.org).

## Extensions
- Python (VS Code extension from microsoft).
- CodeRunner (VS Code extension).

# Feature
1. Readable
2. Easy to learn
3. Cross Platform
4. Open Source
5. Large Standard Library
6. Free
7. Automatic Memory management

# Python Advance Level Topics
1. Python & Web Framework
2. Python & Machine Learning
3. Python & Deep Learning
4. Python & Artificial Intelligence
5. Python & Relational Database

# Comments in python
There are two types in python.
- Single-line comments (# This is single-line)
- Multi-line comments (""" this is multi-line """)

# Python Variables
Variables are used to store data, they take memory space based on the types of the value we assigning to them
``` num = 110 ``` (num is of int type)
``` str = "ram" ``` (str is string)

## Data types
A data types defines the type of data. The data types in python are divided into two parts:- 
1. Immutable Data Types - values cannot be changed.
2. Muttables Data Types - Values can be changed.

Immutable data types in Python are:
- Numbers
- String
- Tuple

Mutable data types in Python are:
- List
- Dictionaries
- Sets

*tuples are defined using parentheses (and commas)*
*lists are defined using square bracket*
*Strings are define using "" or ''*

***The * operator produces a new tuple, list, or string that "repeats" the original content***
***The + operator produces a new tuple, list, or string  whose value is the concatenation of its arguments.***

# Slicing
[start index :ending index]
*ending value not included*

li = [10, 30, 100.5, 11, 50]
print(li[0:3])
**OUTPUT**
10, 30, 100.5

li = [10, 30, 100.5, 11, 50]
print(li[2:])
**OUTPUT**
100.5, 11, 50

- li.append('a') to add the element at last of list
- li.insert(2, 'i') to add the element at the the index 2

# Python Libraries
1. NumPy - math/array clac.
2. Pandas - data manipulation
3. Matplotlib - data visualize
4. Seaborn - data high
5. Keras - neural network
6. Tensorflow - neural network
7. OpenCV - video/image processing
8. PySerial - connect python to IOT
9. Pipeline - Movement

## Program
*program 1*
```import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()
```

*program 2*
```import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.bar(xpoints, ypoints)
plt.show()
```

*program 3*
```import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0,50, 100,150, 250])

plt.bar(xpoints, ypoints)
plt.show()
```

*program 4*
```
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6, 10])
ypoints = np.array([0,150,250])

plt.barh(xpoints, ypoints)
plt.show()
```

*program 4*
```
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6, 10])
ypoints = np.array([0,150,250])

plt.barh(xpoints, ypoints)
plt.bar(xpoints, ypoints)
plt.show()
```

*program 5*
```
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6, 10])
ypoints = np.array([0,150,250])

plt.scatter(xpoints, ypoints)
plt.show()
```

*program 6*
```
import matplotlib.pyplot as plt
sizes = [40, 30, 20, 10]
labels = ['A', 'B', 'C', 'D']
plt.pie(sizes, labels=labels)
plt.show ()
```

*program 7*
```
import matplotlib.pyplot as plt
marks = [55, 60, 65, 70, 72, 75, 80, 85, 90, 95]
plt.hist(marks, bins=5)
plt.show()
```

*program 8*
```
import matplotlib.pyplot as plt
plt.subplot(1, 2, 1); plt.plot([1, 2, 3], [2, 4, 6])
plt.subplot(1, 2, 2); plt.bar(["A","B"], [5, 7])
plt.show()
```

*program 9*
```
import matplotlib.pyplot as plt
import seaborn as sns
sns.lineplot(x=[1,2,3],y=[10,20,15])
plt.show()
```

*program 10*
```
import seaborn as sns 
import matplotlib.pyplot as plt
sns.barplot(x=['A', 'B', 'C'], y=[5,8,3])
plt.show()
```

*program 11*
```
import seaborn as sns
import matplotlib.pyplot as plt
sns.scatterplot(x=[1,2,3,4],y=[10,20,15])
plt.show()
```

*program 12*
```
import seaborn as sns
import matplotlib.pyplot as plt
sns.histplot([1,2,2,3,4,4,5])
plt.show()
```

*program 13*
```
import seaborn as sns
import matplotlib.pyplot as plt
sns.boxplot(y=[10,20,30,40])
plt.show()
```

*program 14*
```
import seaborn as sns
import matplotlib.pyplot as plt
flights = sns.load_dataset("flights").pivot(index="month", columns="year",values="passengers")
sns.heatmap(flights, cmap="viridis")
plt.show()
```

*program 15*

### Load image in python
```
from PIL import image
img = Image.open('image.png')
img.show()
# To display the image information
print(f"Format: {img.format}")
print(f"Mode: {img.mode}")
print(f"Size: {img.size}")
```

### GUI in python
```
import tkinter as tk
root = tk.TK()
root.title("My first tkinter app")
root.geometry("300x200")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

root.mainloop()
```

# Python Pandas
```
import pandas as pd
p1 = pd.read_csv("")
print(p1)
```

# OpenCV
To perform color detection in OpenCV, you should convert your image from the default BGR color space to the HSV (Hue, Satauration , Value) color space and apply a pixel intensity threshold using *cv2.inrange()*. The HSV space is highly preferred over BGR/RGB because it seperates color information (Hue) from lightning intensity and brightness, making your detection resilient to shadows and lightning changes.

## The color detection pipeline 
1. **Read the Frame**: Load your image or stream frames from a webcam.
2. **Convert to HSV**: Use *cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
3. **Apply a range mask** : Define the upper and lower HSV threshold for your target color.
4. **Isoltae the color**: Use *cv2.inrange()* to generate a binary mask where the target color appears white(255) and everything else appears black(0).

*program 1*
```
import cv2
import numpy as np
#intialize the camera feed (0 is usually the default built-in camera)
cap=cv2.videoCapture(0)
while true:
# capture frame by frame
ret, frame = cap.read()
if not ret:
break

#Convert BGR imaege from BGR to HSV color space
hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#Define the precise HSV threshold range for the color Blue OpenCV HSV ranges: H(0-179), S(0-255), V(0-255)
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

#Create a binary mask where blue pixels are white , other are black
mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)

#Optional: Clean up noise using Morphological Dilation 
kernel = np.ines((5, 5), np.unit8)
mask=cv2.dilate(mask, kernel, iterations=1)

#Bitwise_AND mask and original image to isolate the colored object
detect_output = cv2.bitwise_and(frame, frame, mask=mask)
#Display the results in the seperate windows frames
cv2.imshow('Original Camera Feed', frame)
cv2.imshow("Binary Mask Only', mask)
cv2.imshow('Isolated Color Output', detected_output)

#break the loop when the 'q' key is pressed
if cv2.waitKey(1) & 0xFF == ord('q'):
break

#clean up the windows and release camera source
cap.release()
cv2.destroyAllWindows()

```

*program 2*
```
import cv2
img = cv2.imread("download.jpg", cv2.IMREAD_COLOR)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

*program 3*
```
import cv2
src = cv2.imread(r"downlaod.img")
gray_image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray_image)
cv2.waitkey(0)
cv2.destroyAllWindows()
```

*program 4*
```
import cv2
image = cv2.imread('downlo.jpg')
cv2.rectangle(image, (5, 5), (220, 220), (255, 0, 0), 2)
cv2.imshow('Image', image)
cv2.waitkey(0)
cv2.destroyAllWindows()
```

***Syntax: cv2.line(image, start_point, end_point, color, thickness)*** 
*** cv2.line(img, (50,50), (250,50),(255,0,0),3) draws line from (50,50) to (250,50) in blue with thickness 3.***

***Syntax: cv2.circle(img, center, radius, color, thickness=None, lineType=None, shift=None)***
***cv2.circle(img, center=(100,100), radius=50, color=(0,255,0), thickness=12)***

***Syntax: cv2.putText(image, text, org, font, fontscale, color, thickness=1, lineType=cv2.LINE_8, bottomLeftOrigin=False)***

***cv2.polylines(image, [pts], isClosed, color, thickness)***
*** pts: Array of polygonal curves.***
*** npts: Array of polygon vertex counters.***
*** contours: Number of curves ***
*** isClosed: Flag indicating whether the drawn polylines are closed or not. ***

*Image resizing refers to the scaling of the images. It helps in reducing the number of pixels from an image and that has several advantages.*
**Methods of Resinzing**
*- cv2.INTER_AREA: This is used when we shrink an image.*
*- cv2.INTER_CUBIC: This is slow but more efficient.*
*- cv2.INTER_LINEAR: This is primarily used when zooming is required.*
***cv2.resize(image, (0,0), fx=0.1, fy=0.1)***
***bigger= cv2.resize(image, (1050, 1610))***

*Program*
```
import cv2
img = cv2.imread('sv.jpd')
resized_fixed = cv2.resize(img, (400,300))
res = cv2.resize(img, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
cv2.imshow("resized & rotated", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

*Program*
```
import cv2
img = cv2.imread('sv.jpg')
rot_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
rot_180 = cv2.roate(img, cv2.ROTATE_180)
rot = cv2.rotate(img, cv2.ROATE_90_CLOCKWISE)
cv2.ishow('Resized & Rotated', rot)
cv2.waitKey()
cv2.destroyAllWindows()
```

*Program*
```
import cv2
image = cv2.imread('img.jpg')
blur1 = cv2.blur(image, (5,5))
cv2.imshow("Avergin blur', blur1)
cv2.waitkey(0)
```

*Program*
```
import cv2
impory numpy as np
image = cv2.imread('sv.jpg', cv2.IMREAD_GRAYSCALE)
blurred_image = cv2.GaussianBlur(image, (5,5), 0)
edges = cv2.canny(blurred_image, threshold1=50, threshold2=150)
cv2.imshow('Canny Edges', edges)
cv2.waitKey()
cv2.destroyAllWindows()
```

*Program*
```
import cv2
img=cv2.imread('god.jpg')
img = cv2.putText(img, "Hello", (40,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
cv2.imshow('image', img)
cv2.waitkey(0)
cv2.destroyAllWindows()
```

# Simple Thresholding using OpenCV
Thresholding is a foundational technique in computer vision and image processing used to segment objects from the background. It works by comparing each pixel value of a grayscale image against a specified threshold value. Based on this comaparision, Pixels are assigned new values, usulaly 0(black) or 255(white). In openCV with Python, the function cv2.threshold is used for thresholding.
in thresholding, for every pixel at position (x.y) with an intensity value f(x,y):
- If f(x,y) < T, set the pixel to 0(black)
- If f(x,y) >= T, set it to the maximum value (typically 255, white)
- Here, T is threshold value.

|Technique|Description|
|---------|-----------|
|cv2.THRESH_BINARY|Above threshold-> 255, Below->0|
|cv2.THRESH_binary_INV|Above threshold->0, Below->255(inverse in binary)|
|cv2.THRESH_TRUNC|Above threshold->set to threshold, below->unchanged|
|cv2.THRESH_TOZERO|Below threshold->0, above->unchanged|
|cv2.THRESH_TOZERO_INV|Above threshold->0, below->unchanged(inverse to zero)|

***Step1: Import library and image preparation***
```
import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('input.jpg')
gray_image = cv2.cvtColor(image, cv2.BOLOR_BGR2GRAY)
```

***Step2: Helper Function***
```
def show_image(img, title):
plt.imshow(img, cmap='gray')
plt.title(title)
plt.axis('off')
plt.show()
```

***Step3: Display the original Image***
show_image(gray_image, 'Original Grayscale Image')

***Step4: Binary threshold***
- If a pixel intensity is above the threshold, it is assigned  the maximum value - otherwise, it becomes 0(black).
- Useful for seperating bright objects from a dark background.
```
_, thresh_binary = cv2.threshold(gray_image, 120, 255, cv2.THRESH_BINARY)show_image(thresh_binary, 'Binary threshold')
```

# Noise Reduction
OpenCv provides several distinct methods for image noise reduction, ranging from basic blurring techniques to advanced aptch-matching algorithims . The best method depends entirely on the type of noise in your image.

**1. Advance Denoising (Best for Graysclae & Color Noise)**
The Non-Local Means (NLM) algoorithm is OpenCV's most powerful built-in tool for general denoising. Instead of looking only at the neighbouring pixels, it searches the entire image for similar patches to average out noise while preserving sharp edges.
- For Grayscale images: cv2.fastNIMeansDenoising()
- for Colored images: cv2.fastNIMeansDenoisingColored()
```
import cv2
img = cv2.imread('photo.jpg')
denoised_img = cv2.fastNlMeansDenoisingColored(img, None, h=10, hColor=10, templeateWindowSize=7, searchWindowSize=21)
cv2.imwrite('cleaned_photo.jpg', denoised_img)
```

# Contour
```
import cv2
img = cv2.imread('images.jpg')
bilat = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)
cv2.imwrite('cleaned_bilateral.jpg',bilat)
```
## Find and draw contours using OpenCV - Python
Contours are edges or outline of a objects in a image and is used in image processing to identify shapes, detect objects or measure their size. We use Opencv's *findContours()* function that works best for binary images.
There are three important arguments to this function:
- **Source image**: This is the image from which we want to find the contours.
- **Contour retrieval methods**: This determines how contours are retreieved.
- **Contour Aprroximation Method**: This decides how much detail to keep when storing the contours.

Lets implement it in python:
*** 1. Importing necessary libraries ***
First, we need to import libraries like numpy and OpenCV that help us process image.
```
import cv2
import numpy as np
```

*** 2. Reading image ***
Now, we load the image we want to work with. We use cv2.imread() to read the image and cv2.waitkey()
pauses the program until you press a key.
```
image = cv2.imread('image.png')
cv2.waitKey(0)
```

*** 3. Converting image to GrayScale ***
To make it easier to process the image, we convert it from color (BGR) to grayscale.
GrayScale images are simpler to work with for tasks like detecting edges.
```
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

*** 4. Edge Detection Using Canny ***
```
edged = cv2.canny(gray, 30, 200)
```
*** 5. Finding Contour ***
```
contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
```
*** 6. Displaying Canny Edges After Contouring ***
```
cv2.imshow('Canny Edges After Contouring`, edged)
cv2.waitkey(0)
```
*** 7.Printing Number of Contours Found ***
```
print("Number of Contours Found = " + str(len(contours)))
```
*** 8. Drawing Contours on the Original Image ***
```
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
cv2.imshow('Contours', image)
cv2.waitkey(0)
cv2.destroyAllWindows()
```
# Dilation & Erosion
Erosion and dilation are two fundamentals techniques used to modify
object boundaries, remove noise, fill gaps, and refine shapes in binary and grayscale images.
- Boundary Refinement: Modify object size and shape by shrinking or expanding regions.
- Noise Reduction: Removes small unwanted regions and improve image quality.

## Erosion
Erosion shrinks foreground regions by removing pixels from object boundaries. It is commonly used to eliminate small white noise, seperate connected image, and reduce the size of foreground features in an image.

## Dilation
Dilation expnds foreground regions by adding pixels to object boundaries. It is commonly used to fill small gaps, connect nearby objects, and enhance the visibility of foreground features.

Difference between Erosion and Dilation
|Feature|Erosion|Dilation|
|-------|------|--------|
|Main Purpose| Shrinks foreground objects|Expands foreground objects|
|Visual Effect| Objects appear smaller and thinner| Objects appear larger and thicker|
|Edge Behavior|Removes pixels from object boundaries| Adds pixels to object boundaries|

```
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images.png',0)

kernel = np.ones((5,5), np.unit8)

img_dilation = cv2.dilate(img, kernel, iternations=1)
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.tight_layout()
plt.show()
```

```
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img.png', )
kernel = np.ones((5, 5), np.unit8)
img_erosion = cv2.erode(img, kernel, iterations=1)
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(1,2,1)
plt.imshow(img_erosion, cmap='gray')
plt.title("After erosion")
plt.axis('off')
```

*Smile Detection Program*
```
import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbrs=5)

    for(x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x+w), (y+h), (255, 0, 0), 2)

    roi_gray = gray[y:y + h, x:x + w]

    smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1, minNeighbors=20, minSize=(25,25))

    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(frame, (x+sx, y+sy), (x+sx+sw, y+sy+sh), (0, 255, 0), 2)

cv2.imshow('Smile Detection', frame)

if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
```

# OpenCV Video Processing
```
import cv2
cap = cv2.VideoCapture("video.mp4")
if not cap.isOpened():
    print("Error: Counld not Open Video File.")
    exit()

while True:
    ret, frame = cap.read()
    cv2.imshow("Video", frame)
    if cv2.waitKey(100) &  0xFF = ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

*Display the date of the video*
```
import cv2
import datetime
vid = cv2.VideoCapture('video.mp4')
while vid.isOpened():
    ret, frame = vid.read()
    if not ret:
        break
    font = cv2.FONT_HERSEY_SCRIPT_COMPLEX
    dt = str(datetime.datetime.now())
    frame = cv2.putText(frame, dt, (10, 100), font, 3, (255,0,0), 2, cv2.LINE_8)

    cv2.imshow('Video with Date & Tie', frame)
    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:
        break
vid.release()
cv2.destroyAllWindows()
```

```
import cv2
import time

haar_cascade = 'cars.xml'
car_caascade = cv2.CascadeClassifier(haar_cascade)
if car_cascade.empty():
    raise Exception("Error loading haar cascade file.")

video = 'car-video.mp4'
cap = cv2.VideoCapture(video)

if not cap.isOpened():
    raise Exception("Error opening video file.")

    car_detected = False
    detection_time = None

    while cap.isOpened();
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1m minNeighbors=3)
        
        if len(cars)>0 and not car_detected:
            car_detected = True
            detection_time = time.time()
            print("Car detected!")

        if car_detected and time.time() - detection_time>5:
            break
        
        for (x, y, w, h) in cars:
            cv2.rectangle(frames, (x, y), (x+w, y+h), (0,0,255), 2)
        
        cv2.imshow('video', frames)

        if cv2.waitKey(33) == 27:
            break
        
        cap.release()
        cv2.destroyAllWindows()
```
# What is object tracking
Object tracking in computer vision is following and keeping a record of the position of any object upon its changein movement in the video. Multiple objects can also be tracked simultaneously . The main goal of object is to maintain the identity and positioning of the object.

## Applications of object tracking
Below are the applications of object tracking using openCV:
- Tracking enemy military's movement.
- Precision aiming in military weapons (eg. headshot aiming)
- Surveillance cameras
- keeping count of people/vehicles/animals/objects

## Visual Implementation
<p text-align:"center">
1. import Depeandency and set up camera
2. Initialize Tracker
3. Detect the object
4. Track and Update objects in each Frame
5. Draw the updated position of object
</p>

# ESP 32 Cam Module
The ESP32 Based Camera Module developed by AI-Thinker. The controller is based on 32-bit CPU & has a combined Wi-Fi + Bluetoth/BLE chip. It has a built-in 520kb SRAM with an external 4M PSRAD GPIO pins have support like UART, SPI, I2C, PWM, ADC and DAC. 
The module has resolution 1600x1200. The board supports upto 4GB memory card. The camera connects using 24 pins gold plated connected.

# Color Detection
Color Detection in OpenCV (python) is acheived by converting an image from the default BGR color space to HSV color space, defining upper ans lower thresholds for the targetcolor, and creating a binary mask to isoltae those specific pixels.

[Load BGR Image] -> [Convert to HSV] -> [Apply cv2.inRange(Mask)] -> [Bitwise AND with original]

*** QR Code Program ***
```
import cv2 

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
print("Press 'q' to exit the live scanner loop.")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    data, bbox, _ = detector.detectAndDecode(frame)
    if bbox is not None:
        bbox = bbox.astype(int)
        n = len(bbox[0])
        for i in range(n):
            cv2.line(frame, tuple(bbox[0][i]), tuple(bbox[0][i+1]) % n, (0,255,0), 2)

        if data:
            print(f"Decoded: {data}")
            cv2.putText(frame, data, (box[0][0][0], bbox[0][0][1] - 10), cv2.FONT_HERSEY_SIMPLEX, 1.5, (255, 0, 0), 2)

    cv2.imshow("Live QR Scanner", frame)

    if cv2.waitKey(1) & 0xFF == ord('q')
        break

cap.release()
cap.destroyAllWindows()
```

# DataScience
Software needed for DataScience:
1. Jupyter
2. Anaconda
3. Conda
4. Spider
5. VS Code

*Program 1*
```
import pandas as pd
d1=pd.read_csv("hospital data analysis.csv")
print(d1)
```
Data Science is about data gathering , analysis and decision-making.
Data Science is about finding patterns in data, through analysis, and make future predictions.
By using Data Science, companies are able to make:
- Better decisions (should we choose A or B)
- Predictive analysis (What will happen next?)
- Pattern discoveries (find pattern, or maybe hidden information in the data)

## Where is Data Science Needed?
Data Science is used in many industries in the world today, e.g. banking, healthcare, and manufacturing.
Examples of where Data Science is needed:
- For route planning
- To create promotional offers
- To predict who will win the elections
- Industry 
- Stock Market
- Politics

Data can be categorized into two groups:
- Structured data
- Unstructures data

## Unstructured Data
Unstructured data is not organized. We must organize the data for analysis purposes.

## Structured Data
Structured data is organized and easier to work with.

## Key Components
The discipline is typically mapped across three intersecting areas:
- **Mathematics and Statistics**
- **Computer science and engineering**
- **Domain Knowledge**

## Data Science Life Cycle
1. Data Collection/Obtain/Gather
2. Data Clean
3. Explore/analyze
4. Model
5. Interpret/Communicate/deploy

## Core Programming Functions (Python & Pandas)
Data Scientists spend most of their time using python libraries like Pandas and NumPy. Workflow stage:
**Data Collection**
*read_csv()/read_excel()*: Imports raw data files into a usable DataFrame structures layout.
*head()/tail()*: Display first or last few rows.
*info()*: Outlines structural details like total memory usage, columns, and data types.
*describe()*: Generates rapid descriptive statistics for all numeric columns.

**Data Cleaning and & Transformation**
*dropna()*: Drops missing or null (NaN) values from a dataset.
*fillna()*:Substitutes mising entries with specified placeholders or calculated metrics.
*drop_duplicates()*
*astype()*: Change datatype of a column
*apply()*: Maps custom lambda opertions or functions across every row or column.

**Preprocess/Aggregation & Analysis**
*groupby()*
*merge()/join()*
*value_counts()*
*pivot_table()*

***Mathematical and Statistical Function***
*mean()*
*median()*
*std()*
*corr()*
***Probability & Optimization***
Probability Density Function (PDF): Maps out the likelihood of continous variables.
Cumulative Distribution Function (CDF): Tracks cumulative probability up to specific value  



## Create Dataframe with Pandas
A data frame is the structures representation of data.

```
import pandas as pd
d= {'col3': [1,2,3,4,5], 'col2': [2,3,5,4,6], 'col3': [9,5,6,7,5]}
df = pd.DataFrame(data=d)
print(df)
```

*Project 1*
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Step 1: Create & Load Dataset
data = {
    'Size_sqft':[1500, 1800, 2400, np.nan, 3000, 1200, 2100, 1900, 2800, 1600],
    'Bedrooms': [3, 4, 3, 4, 5, 2, 3, 3, 4, 3],
    'Price_USD':[300000, 360000, 470000, 410000, 590000, 240000, 400000, 380000, 540000, 320000]
}

df = pd.DataFrame(data)
print("---Raw Dataset---")
print(df.head(), '\n')

# Step 2: Data Cleaning
print("Missing values per column:\n", df.isnull().sum())
df['Size_sqft'] = df['Size_sqft'].fillna(df['Size_sqft'].mean())
print("Cleaned Data")
print(df.head(), '\n')

# Step 3: Exploratory Data Analysis (EDA)
print("---Summary Statistics---")
print(df.describe(), "\n")

# Step 4: Data Visualization
plt.scatter(df['Size_sqft'], df['Price_USD'], color='blue', label='Data Points')
plt.title("House Price vs Size")
plt.xlabel('Size(sqft)')
plt.ylabel('Price($)')
plt.grid(True)
plt.show()
```

# Machine Learning
- Machine learning is the method of data analysis that automates analytical model building.
- It is a brach of artificial intelligence based on the idea that systems can learn from data.
- Idenetify patterns and make decisions with minimal human intervention.

## Steps of Machine Learning
The Machine Learning Processes:
**Step 1:**
Data Acquisition
**Step 2:**
Data Preprocessing
**Step 3:**
Feature Extraction
**Step 4:**
Fitting Model
**Step 5:**
Model Evaluation

## Types of Machine Learning
1. *Supervised Learning*: Label
2. *Unsupervised*: Unlabel
3. *Reinforcement*

## Supervised Learning 
- Basically supervised learning is when we teach or train the machine using data that is well labelled.
- Which means some data is already tagged with the correct answer.
- After that, the machine is provided with a new set of examples(data) so that the supervised learning algorithm analyses the training data(set of training examples) and produces a correct outcome from labeled data.

  ## K-Nearest Neighbors (KNN)
  - K-Nearest  Neighbors is one of the most basic yet essential classification algorithms in machine learning.
  - It belongs to the supervised learning domain and finds intense application in pattern recognition, data mining, and intrusion detection.
  - In this algorithm, we identify category based on neighbors.

  ## Support Vectors Machines (SVM)
  - The main idea behind SVMs is to find a hyperlpane that maximally seperates the different classes in the training data.
  - This is done by finding the hyperplane that has the largest margin, which is defined as the distance between the hyperplane and the closest data points from each class.
  - Once the hyperplane is determined, new data can be classified by determining on which side of the hyperplane it falls.
  - SVMs are particularly useful when the data has many featres, and/or when there is a clear margin of seperation in the data.

```
X = df[['Size]]
y= df['Price_USD']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state = 42)

# Initialize and train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predicitons using the test data
predictions = model.predict(X_test)

# Evaluate model performance using Mean Squred Error
mse = mean_squared_error(y_test, predictions)
print(f"Model training complete.")
print("Mean Squared error on Test Set: {mse:.2f}")

# Predict the price of a new house (2000 sqft, 3 bedrooms)
new_house = pd.DataFrame([[2000, 3]], columns=['Size_sqft, 'Bedrooms'])
predicted_price = model.predict(new_house)
print(f"Predicted price for 2000 sqft 3-bed house : ${predicted_price[0]:,.2f}")
```

# Head Movement Controlled Servo Motor Using AI + Arduino
This project demonstrates hands-free control of a servo metro using head movements, combining Python, Mediapipe, OpenCV and Arduino. The servo rotates left, right, or centers based on your head direction, showcasing a simple Human_Computer Interaction (HCI) sytsem.
## Features
- Real-time head tracking using MediaPipe face Mesh
- Left, Right and Center head detection
- Serial communication between Python and Arduino
- Smooth servo motor control
- Low cost and easy to build project
- ideal for robotics, assistive technology, and gesture controled devices
## Hardware Requirements
- Arduino Uno/Nano/Compatible board
- SG90 Servo Motor
- USB Cable 
- Jumper Wire
## Software Requirements 
- Python 3.x
- OpenCV
- MediaPipe
- PySerial
- Arduino IDE
## How it Works
1. Webcam captures your face in real time.
2. Python + Mediapipe detects facial landmarks and calcultes head direction.
3. Python sends a serial command (L,R,C) to Arduino
4. Arduino rotates the servo based on the command:
    L -> Servo rotates left
    R -> Servo rotates right
    C -> Servo Centers
## Project Setup
1. Arduino
    Connect the servo motor:
        - Signal -> Pin 11
        - VCC -> 5V
        - GND -> GND
2. Python
    install Dependencies:
    pip install opencv-python mediapipe pyserial

# Edge Impulse
Edge Impulse is a leading cloud-based Machine Learning operations (MLOps) platform tailored for developing TinyML (embedded machine learning) systems.