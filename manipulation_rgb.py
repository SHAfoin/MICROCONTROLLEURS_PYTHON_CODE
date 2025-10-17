from time import sleep, time

import board
from digitalio import DigitalInOut, Direction
# GP14
ledR = DigitalInOut(board.GP20)
ledR.direction = Direction.OUTPUT
ledG = DigitalInOut(board.GP19)
ledG.direction = Direction.OUTPUT
ledB = DigitalInOut(board.GP21)
ledB.direction = Direction.OUTPUT

while True :
    ledR.value = True
    ledG.value = False
    ledB.value = False
    sleep(3)
    ledR.value = False
    ledG.value = True
    ledB.value = False
    sleep(3)
    ledR.value = False
    ledG.value = False
    ledB.value = True
    sleep(3)