# What is I2C protocol
I2C is the communication protocol between used to allow communication betweeen electronic devices (memory chips, sensors, displays, etc) to communicate with a microcontroller like Arduino UNO, ESP32, ESP8266 using only two wires.
Without I2C, electronic devices would require more than two wires. With I2C protocol devices only require two communication wires
1. SDA (Serial Data: This wire carreis actual data)     
2. SCLK (Serial Clock: )

Along with VCC and GND, so only four wires are required.
Every I2C device has an unique address.
***Example:-***
| Device | Address |
|--------|---------|
|  LCD   |   0x27  |
|  MPU6050   |   0x68 |
|  DS3231 RTC  |  0x57  |

# I2C pins on common boards
| Board | SDA | SCLK |
|-------|-----|------|
| Arduino UNO | A4 | A5 |
| ESP8266 | D2 | D1 |
| ESP32 | GPIO21 | GPIO22 |

# Advantages of I2C
- Only two communication wires
- Multiple devices can share the same bus
- Supports many slave devices
- Simple wiring
- Widely used in sensors and display

# Disadvantages of I2C
- Slower than SPI
- Communication distance should be short
- Devices must have unique address
