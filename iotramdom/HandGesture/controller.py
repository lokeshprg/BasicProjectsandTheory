import pyfirmata2

comport = 'COM8'
board = pyfirmata2.Arduino(comport)

# Servo Pins
bomotor1 = board.get_pin('d:8:o')
bomotor2 = board.get_pin('d:7:o')



def led(fingerUp):


    if fingerUp == [0,0,0,0,0]:
        bomotor1.write(0)
        bomotor2.write(1)
        

    elif fingerUp == [0,1,1,1,1]:
        bomotor1.write(1)
        bomotor2.write(0)
    
    elif fingerUp == [0,1,0,0,0]:
        bomotor1.write(0)
        bomotor2.write(0)