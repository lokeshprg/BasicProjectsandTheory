import pyfirmata2

comport = 'COM8'
board = pyfirmata2.Arduino(comport)

# Servo Pins
servo1 = board.get_pin('d:8:s')
servo2 = board.get_pin('d:9:o')
servo3 = board.get_pin('d:10:o')
servo4 = board.get_pin('d:11:o')


def led(fingerUp):

    # Sab band (0 degree)
    if fingerUp == [0,0,0,0,0]:
        servo1.write(0)
        servo2.write(0)
        servo3.write(0)
        servo4.write(0)

    # 1 Finger
    elif fingerUp == [0,1,0,0,0]:
        servo1.write(1)
        servo2.write(0)
        servo3.write(0)
        servo4.write(0)

    # 2 Fingers
    elif fingerUp == [0,1,1,0,0]:
        servo1.write(0)
        servo2.write(1)
        servo3.write(0)
        servo4.write(0)

    # 3 Fingers
    elif fingerUp == [0,1,1,1,0]:
        servo1.write(0)
        servo2.write(0)
        servo3.write(1)
        servo4.write(0)

    # 4 Fingers
    elif fingerUp == [0,1,1,1,1]:
        servo1.write(0)
        servo2.write(0)
        servo3.write(0)
        servo4.write(1)

    # 5 Fingers
    elif fingerUp == [1,1,1,1,1]:
        servo1.write(1)
        servo2.write(1)
        servo3.write(1)
        servo4.write(1)