# Transmission Control Protocol (TCP)

## What is TCP?

**TCP (Transmission Control Protocol)** is one of the core communication protocols of the Internet. It allows two devices connected to a network to exchange data **reliably, accurately, and in the correct order**.

TCP is known as a **connection-oriented protocol** because it establishes a connection between the sender and the receiver before any data is transmitted.

---

## Why Do We Need TCP?

When data travels across a network, it is divided into small pieces called **packets**. During transmission, packets may:

- Arrive out of order
- Get lost
- Become corrupted

TCP solves these problems by ensuring that:

- All packets reach the destination.
- Packets are reassembled in the correct order.
- Lost packets are retransmitted.
- Duplicate packets are discarded.

---

## Key Features of TCP

- **Connection-Oriented**
  - A connection is established before communication begins.

- **Reliable**
  - Guarantees data delivery.

- **Ordered Delivery**
  - Data arrives in the same order it was sent.

- **Error Detection**
  - Detects corrupted packets using checksums.

- **Flow Control**
  - Prevents the receiver from being overwhelmed by too much data.

- **Congestion Control**
  - Reduces network congestion by controlling the transmission rate.

---

## How TCP Works

TCP communication consists of three main stages:

### 1. Connection Establishment

Before sending data, both devices establish a connection using the **Three-Way Handshake**.

```
Client                      Server
  |                            |
  | -------- SYN ----------->  |
  |                            |
  | <------ SYN + ACK -------  |
  |                            |
  | -------- ACK ----------->  |
  |                            |
Connection Established
```

---

### 2. Data Transmission

Once the connection is established:

- The sender transmits data packets.
- The receiver checks each packet.
- The receiver sends an acknowledgment (ACK).
- If an ACK is not received, the sender retransmits the packet.

```
Client                     Server

Packet 1  -------------->
                ACK <------

Packet 2  -------------->
                ACK <------

Packet 3  -------------->
                ACK <------
```

---

### 3. Connection Termination

After communication is complete, the connection is closed.

```
Client                      Server

FIN --------------------->

                 ACK <-----

                 FIN <-----

ACK --------------------->
```

The connection is now terminated.

---

# What is a TCP Server?

A **TCP Server** is a program that waits for incoming client connections, accepts those connections, exchanges data, and closes the connection when communication is complete.

Examples of TCP servers include:

- Web Servers
- FTP Servers
- SSH Servers
- Database Servers
- ESP8266 Web Server

---

## TCP Server on ESP8266

When using the ESP8266, a TCP server can be created using the `WiFiServer` class.

```cpp
#include <ESP8266WiFi.h>

WiFiServer server(80);
```

Here:

- `WiFiServer` creates a TCP server.
- `80` is the port number.
- Port **80** is the default port used for HTTP.

---

## Starting the Server

```cpp
server.begin();
```

This starts the TCP server and begins listening for incoming client connections.

---

## Waiting for a Client

```cpp
WiFiClient client = server.available();
```

If a client connects, `server.available()` returns a `WiFiClient` object.

Otherwise, no client is available.

---

## Reading Data

```cpp
String request = client.readStringUntil('\r');
```

This reads the client's HTTP request.

Example request:

```
GET / HTTP/1.1
Host: 192.168.4.1
```

---

## Sending Data

```cpp
client.println("HTTP/1.1 200 OK");
client.println("Content-Type: text/html");
client.println();
client.println("<h1>Hello World</h1>");
```

The ESP8266 sends an HTTP response back to the browser.

---

## Closing the Connection

```cpp
client.stop();
```

This disconnects the client after communication is complete.

---

# TCP Server Communication Flow

```
Browser (Client)
        |
        | Connect
        ▼
ESP8266 TCP Server
        |
        | HTTP Request
        ▼
Arduino Code
        |
        | Process Request
        ▼
HTTP Response
        |
        ▼
Browser
```

---

# TCP vs UDP

| Feature | TCP | UDP |
|----------|-----|-----|
| Connection | Connection-Oriented | Connectionless |
| Reliability | Reliable | Not Guaranteed |
| Packet Order | Maintained | Not Guaranteed |
| Error Checking | Yes | Basic |
| Speed | Slower | Faster |
| Examples | HTTP, HTTPS, FTP, SSH | DNS, Video Streaming, Online Games |

---

# Real-World Analogy

Imagine ordering food at a restaurant.

### TCP

1. You enter the restaurant.
2. You place your order.
3. The waiter confirms your order.
4. Your food arrives correctly.
5. You pay the bill.
6. You leave.

Every step is confirmed, making the process reliable.

### UDP

Imagine shouting your order from outside the restaurant.

- The restaurant may hear you.
- They may not.
- Your order may be incomplete.
- No confirmation is provided.

This makes UDP faster but less reliable.

---

# Summary

- TCP stands for **Transmission Control Protocol**.
- It provides reliable and ordered communication between devices.
- A TCP server waits for incoming client connections.
- The ESP8266 uses `WiFiServer` to create a TCP server.
- Web browsers communicate with the ESP8266 over TCP using the HTTP protocol.
- TCP is widely used for web browsing, email, file transfer, and remote access.