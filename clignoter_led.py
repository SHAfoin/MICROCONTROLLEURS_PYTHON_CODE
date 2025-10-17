from time import sleep
import board
from digitalio import DigitalInOut, Direction
# La LED qui se trouve sur la carte
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
while True:
    led.value = True
    print("led on : allumée")
    sleep(1)
    led.value = False
    print("led off : éteinte")
    sleep(1)
