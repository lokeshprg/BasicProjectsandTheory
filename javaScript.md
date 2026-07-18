# JS Introduction
## What can JavaScript do?
JavaScript is the programming language of the web.
It can calculate, manipulate and validate data.
It can update and change both HTML and CSS.

## JavaScript can change HTML Content
using:
 ```
 getElementById()
  ```
Finds the element by Id in html and change the element content using innerHTML.
*Example*
```
document.getElementById("demo").innerHTML = "Hello JavaScript";
```
*JavaScript accepts both double and single quotes.*

## JavaScript can change HTML Atrribute Values
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bulb ON/OFF</title>
</head>
<body>
    <h2>Bulb On and Off</h2>
    <img src="pic_bulboff.gif" id="myImage" styles="width:100px">
    <button onclick="document.getElementById('myImage').src='pic_bulbon.gif'">Turn On Bulb</button>
    <button onclick="getElementById('myImage').src='pic_bulboff.gif'">Turn Off Bulb</button>
</body>
</html>
```
## JavaScript can change HTML Styles (CSS)
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Style Manipulation</title>
</head>
<body>
    <h2>Change Font Size</h2>
    <p id="demo">JavaScript can change the style of an HTML element.</p>
    <button type="button" onclick="document.getElementById('demo').style.fontSize='35px'">Big!</button>
    <button type="button" onclick="getElementById('demo').style.fontSize='10px'">Small!</button>
    <button type="button" onclick="getElementById('demo').style.color='red'">Color!</button>
</body>
</html>
```

## JavaScript can Hide the HTML Elements
```
document.getElementById('demo').style.display = "none";
```

## JavaScript can show the HTML elements
```
document.getElementById('demo').style.display = "block";


JavaScript and java are completely different lnguage, both in concept and design
JavaScript was invented by Brednana Eich in 1995, and became ECMA standard in 1997.
ECMA-262 is the official name of the standard. ECMAScript is the official name of the standard.