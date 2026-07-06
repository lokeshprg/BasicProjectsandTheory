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