from time import sleep, time
import random

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
    ledR.value = random.choice([True, False])
    ledG.value = random.choice([True, False])
    ledB.value = random.choice([True, False])
    sleep(1)
    