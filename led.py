from time import sleep
import board
from digitalio import DigitalInOut, Direction
# GP14
led = DigitalInOut(board.GP14)
led.direction = Direction.OUTPUT

while True :

    led.value = True
