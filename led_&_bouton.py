from time import sleep
import board
from digitalio import DigitalInOut, Direction
# GP14
led = DigitalInOut(board.GP14)
led.direction = Direction.OUTPUT

bouton = DigitalInOut(board.GP13)
bouton.direction = Direction.INPUT

while True :

    led.value = True
    if bouton.value:
        led.value = False
        sleep(0.1) # Essentiel sinon marche pas