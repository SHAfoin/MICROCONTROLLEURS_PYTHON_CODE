from time import sleep, time

import board
from digitalio import DigitalInOut, Direction
# GP14
led = DigitalInOut(board.GP14)
led.direction = Direction.OUTPUT

bouton = DigitalInOut(board.GP13)
bouton.direction = Direction.INPUT

start = 0
led.value = False

while True :
    if bouton.value:
        led.value = True
        start = time()
        print(start)
    else:
        if start != 0 and time() - start > 5:
            led.value = False
    sleep(0.1)