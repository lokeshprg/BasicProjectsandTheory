import pyfirmata2

comport='COM8'
board=pyfirmata2.Arduino(comport)

servo1 = board.get_pin('d:8:s')

def led(fingerUp):
    if fingerUp==[0,0,0,0,0]:
        servo1.write(0)
    elif fingerUp==[1,1,1,1,1]:
        servo1.write(180)