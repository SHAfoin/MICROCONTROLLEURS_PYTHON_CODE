from time import sleep
import board
from digitalio import DigitalInOut, Direction
# La LED qui se trouve sur la carte
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

for i in range (5) :
    led.value = True
    print("led on : allumée", i)
    sleep(2)
    led.value = False
    print("led off : éteinte", i)
    sleep(2)