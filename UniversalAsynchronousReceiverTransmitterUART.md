# Universal Asynchronous Receiver/Transmitter (UART)

## What is UART?

**UART (Universal Asynchronous Receiver/Transmitter)** is a hardware communication protocol that allows two devices to exchange data **serially**, meaning **one bit at a time**, without requiring a shared clock signal.

It is one of the most common communication methods used in embedded systems such as:

- Arduino
- ESP8266
- ESP32
- Raspberry Pi
- GPS Modules
- Bluetooth Modules
- GSM Modules
- Computers

---

# Why is UART Needed?

Suppose an Arduino wants to send temperature readings to a computer.

Instead of sending all 8 bits simultaneously (parallel communication), UART sends **one bit at a time** over a single communication line.

Example:

```
Character : A

ASCII Value : 65

Binary : 01000001
```

UART sends the bits one after another:

```
0 → 1 → 0 → 0 → 0 → 0 → 0 → 1
```

This reduces the number of wires required for communication.

---

# Why is UART Called Asynchronous?

"Asynchronous" means that **there is no separate clock wire** shared between the communicating devices.

Protocols like SPI and I²C use a clock signal to synchronize data transmission.

UART does **not** use a clock line.

Instead, both devices must agree on communication settings before data transmission begins.

These settings include:

- Baud Rate
- Number of Data Bits
- Parity
- Number of Stop Bits

If these settings match on both devices, communication will be successful.

---

# UART Pins

UART communication generally requires only three connections.

```
Arduino                 Computer

TX ---------------------> RX

RX <--------------------- TX

GND --------------------- GND
```

## TX (Transmit)

Sends data from the device.

## RX (Receive)

Receives incoming data.

## GND (Ground)

Provides a common voltage reference for both devices.

> **Important:** TX of one device always connects to RX of the other device.

---

# UART Frame Structure

UART sends every byte inside a frame.

The most common frame format is **8N1**.

- 8 Data Bits
- No Parity
- 1 Stop Bit

Frame structure:

```
Idle | Start | Data Bits | Stop

 1      0     01000001     1
```

A UART frame consists of:

1. Idle State
2. Start Bit
3. Data Bits
4. Optional Parity Bit
5. Stop Bit

---

# 1. Idle State

When no data is being transmitted, the communication line remains HIGH.

```
HIGH HIGH HIGH HIGH HIGH
```

The receiver continuously monitors the line waiting for the start bit.

---

# 2. Start Bit

Transmission begins by pulling the line LOW.

```
HIGH HIGH HIGH LOW
               ↑
          Start Bit
```

The falling edge tells the receiver that a new byte is about to arrive.

The receiver starts its internal timer based on this transition.

---

# 3. Data Bits

The actual data is transmitted immediately after the start bit.

Example:

```
Character : A

ASCII : 65

Binary : 01000001
```

UART transmits the **Least Significant Bit (LSB)** first.

Transmission order:

```
1
0
0
0
0
0
1
0
```

This is why UART transmission order appears reversed compared to normal binary representation.

---

# 4. Parity Bit (Optional)

The parity bit provides simple error detection.

## Even Parity

The total number of 1s must be even.

Example:

```
Data

10110010

Number of 1s = 4

Parity = 0
```

Another example:

```
Data

10110000

Number of 1s = 3

Parity = 1

Total = 4 Ones
```

## Odd Parity

The total number of 1s must be odd.

Many Arduino projects use **No Parity**, represented by the letter **N** in **8N1**.

---

# 5. Stop Bit

The stop bit marks the end of the frame.

The communication line returns HIGH.

```
Data Ends

↓

HIGH
```

This allows the receiver to prepare for the next byte.

---

# UART Timing

Suppose the baud rate is:

```
9600 baud
```

Time required to send one bit:

```
1 / 9600

≈ 104.17 µs
```

For an 8N1 frame:

- 1 Start Bit
- 8 Data Bits
- 1 Stop Bit

Total:

```
10 Bits
```

Time required to send one byte:

```
10 × 104.17 µs

≈ 1.04 ms
```

At **115200 baud**, one byte takes only about **87 µs**.

---

# UART Transmission Example

Arduino Code:

```cpp
Serial.println("HELLO");
```

UART sends:

```
'H'
'E'
'L'
'L'
'O'
```

Each character is transmitted in its own UART frame.

---

# UART in Arduino

Example:

```cpp
void setup()
{
    Serial.begin(9600);
}

void loop()
{
    Serial.println("Hello");
}
```

## Serial.begin(9600)

Configures the UART hardware to communicate at **9600 baud**.

## Serial.println()

Places the data into the UART transmit buffer.

The UART hardware automatically converts the characters into serial bits and sends them through the TX pin.

---

# Complete Communication Process

```
Arduino

Serial.println("Hi")

        │

        ▼

UART converts characters into bits

        │

        ▼

TX -----------------------> RX

        │

        ▼

Computer UART reconstructs the bits

        │

        ▼

Serial Monitor Displays

Hi
```

---

# Advantages of UART

- Simple to implement
- Requires only TX, RX, and GND
- Supported by almost all microcontrollers
- Excellent for debugging
- Ideal for point-to-point communication
- Low hardware complexity

---

# Disadvantages of UART

- No shared clock
- Both devices must use identical communication settings
- Slower than SPI
- Supports only point-to-point communication
- Limited error detection (optional parity only)

---

# UART vs SPI vs I²C

| Feature | UART | SPI | I²C |
|----------|------|-----|------|
| Clock Line | ❌ No | ✅ Yes | ✅ Yes |
| Wires Required | 2 Data + GND | 4 + GND | 2 + GND |
| Communication Type | Point-to-Point | Master-Slave | Multi-Device Bus |
| Speed | Medium | Very High | Medium |
| Complexity | Low | Medium | Medium |

---

# Summary

UART (Universal Asynchronous Receiver/Transmitter) is a hardware serial communication protocol that sends data **one bit at a time** using **TX** and **RX** lines without requiring a clock signal.

Since UART is asynchronous, both communicating devices must be configured with the same baud rate, data bits, parity, and stop bits.

Its simplicity, reliability, and wide hardware support make UART one of the most commonly used communication protocols for:

- Arduino debugging
- ESP8266 communication
- ESP32 projects
- GPS Modules
- Bluetooth Modules
- GSM Modules
- Computer Serial Communication

Although it is slower than SPI, UART remains the preferred communication protocol for simple and reliable point-to-point serial communication.