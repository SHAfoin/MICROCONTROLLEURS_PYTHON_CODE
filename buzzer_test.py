import time
import board
import pwmio
from digitalio import DigitalInOut, Direction

buzzer  = DigitalInOut(board.GP26)
buzzer.direction = Direction.OUTPUT

while True :
    buzzer.value = True
    time.sleep(1)
    buzzer.value=False
    time.sleep(1)