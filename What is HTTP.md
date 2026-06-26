# HTTP (HyperText Transfer Protocol)

## What is HTTP?
**HTTP** (HyperText Transfer Protocol) is the standard communication protocol used to tranfer data between a client (such as web browser, mobile app, ot IoT device like an ESP8266) and a server (a computer that hosts a services or websites).

Whenever you open a website, your browser uses HTTP to request the webpage from a server.

***HTTP is a set of rules that defines how a client and a server communicate over the internet or a local network.***

## How HTTP Works
Browser (request)----------> Server<br>
Browser <--------------(response) Server

*Example :-*
<div align="center">
<br>
you type:<br>
`http://example.com` <br>
            ↓<br>
Browser sends HTTP Request<br>
            ↓<br>
Server receives request<br>
            ↓<br>
Server processes request<br>
            ↓<br>
Server sends HTTP response<br>
            ↓<br>
Browser Displays webpage<br>
</div>

## Client and Server
### Client
The Client is the device requesting information.

**Examples :-**
- Chrome
- Firefox
- Edge
- ESP8266
- Mobile App
The client always initiates the communication.

### Server
A server stores webpages and resources.

**Example :-**
- Apache Server
- Nginx
- ESP8266 acting as a web server
The server waits for requestts and replies when asked.


## HTTP Request
A request is sent from the client to the server.

**Example :-**
GET /index.html HTTP/1.1
Host: example.com

*Meaning:*
- ***GET***: I want a webpage.
- ***/index.html***: This page.
- ***HTTP/1.1***: Using HTTP version 1.1.

## HTTP Response
The server replies.

**Example :-**
HTTP/1.1 200 OK
Content-Type: text/html

```
<html>
...
</html>
```
*Meaning:*
- ***HTTP/1.1***: Protocol version.
- ***200***: Success
- ***OK**: Everything is fine.
- ***HTML***: The webpage content.

### HTTP COMMUNICATION FLOW
Broweser (HTTP request)---> Server Processes Request (HTTP response)----> Browser Displays Website

## Structure of an HTTP Request
Every HTTP has several parts

```
GET /index.html HTTP/1.1
Host: example.com
User-AgentL: Chrome
Accept: text/html

(Body)
```
### Request Line
Contains:
- Method
- URL
- HTTP Version

### Headers
Extra Information.

**Example :-**
```
Host: example.com
```

Tells the browser which website is requested.

**Example :-**
```
User-Agent: Chrome
```

Tells the server which browser is sending the request.

### Body
Used maily for sending data.

**Example :-**
```
username=lokesh
password=1234
```

Usually used with POST requests.

## Structure of an HTTP Response

```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 120

<html>
...
</html>
```

Contains:
- Status Line
- Headers
- Body

## HTTP Methods
HTTP provides different methods depending on the action you want to perform.

| Method | Purpose | Example |
|--------|---------|---------|
| GET | Retrieve data | Open a webpage|
| POST | Send new data | Submit a login form |
| PUT | Replace existind data | Update a user profile |
| PATCH | Partially update data | Change only an email address |
| DELETE | Remove data | Delete a user account |
| HEAD | Retrieve headers only | Check if a page exists |
| Options | Ask which methods are supported | Browser checks server capabilities |

### GET 
Requests data.
**Example :-**
```
GET /temprature
```

### POST
Sends data.
**Example :-**
```
POST /login
```

username = Lokesh
password = 1234

## HTTP Status Codes
Every response contains a status code.

### 1xx - Informational
```
100 Continue
```
*Server says:*
continue sending data.

### 2xx - Success
```
200 OK
```
Everything worked.

**Other examples:**
- 201 Created
- 204 No Content

### 3xx - Redirection
**Example :-**
```
301 Moved Permanently
```
The resource has moved to a new URL.

### 4xx - Client Errors
**Example :-**
```
400 Bad Request
```
The request is malformed.

```
401 Unauthorised
```
Authentication is required.

```
403 Forbidden
```
Access is denied.

```
404 Not Found
```
The requested page doesn't exist.

### 5xx - Server Errors
**Examples :-**
```
500 Internal Server Error
```
Something went wrong on the server.

```
503 Service Unavailable
```
The server is temporarily unavailable.

## HTTP Headers
Headers provide additional information about the request or response.

*Common request headers:*
Host
User-Agent
Accept
Authorization
Cookie

*Common response headers:*
Content-Type
Content-Lenght
Server
Date
Cache-Control

**Example :-**
```
Content-Type: text/html
```
The browser knows to interpret the response as an HTML page.

## HTTP Versions
### HTTP/1.0
- One request per connection
- Slow because a new connection is needed for each request.
### HTTP/1.1
- Persistent connections by default.
- Multiple requests can reuse the same connection.
- Still widely used, including on many embedded devices like the ESP8266.
### HTTP/2
- Sends multiple requests simultaneously over a single connection (multiplexing).
- Compresses headers for better efficiency.
- Faster page loading.
### HTTP/3
- Uses the QUIC transport protocol instead of TCP.
- Faster Connection Setup.
- Better performance on unreliable networks. 

## HTTP vs HTTPS

| HTTP | HTTPS |
|------|-------|
| Data is sent in plain text | Data is encryted |
| Less secure | More Secure |
| Uses port 80 | Uses port 443 |
| Vulnerable to eavesdropping | Protects confidentially and integrity |

HTTPS adds encryption so that information like passwords and payment details cannot be easily read or altered while in transit.