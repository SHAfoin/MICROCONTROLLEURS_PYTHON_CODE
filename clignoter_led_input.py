from time import sleep
import board
from digitalio import DigitalInOut, Direction
# La LED qui se trouve sur la carte
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

nb = int(input("Combien de clignotements ? "))

for i in range (nb) :
    led.value = True
    print("led on : allumée", i+1)
    sleep(2)
    led.value = False
    print("led off : éteinte", i+1)
    sleep(2)
    
print("J'ai clignoté", nb, "fois !")