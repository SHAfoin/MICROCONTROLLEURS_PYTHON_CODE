from time import sleep, time
import random
import board
from digitalio import DigitalInOut, Direction
import analogio

ledR = DigitalInOut(board.GP20)
ledR.direction = Direction.OUTPUT
ledG = DigitalInOut(board.GP19)
ledG.direction = Direction.OUTPUT
ledB = DigitalInOut(board.GP21)
ledB.direction = Direction.OUTPUT

potentiometre = analogio.AnalogIn(board.GP26)

def fraction(input) :
    return input/65535.0
    
def pourcentage(input) :
    return fraction(input)*100
    
def can(input) :
    return fraction(input)*3.3

while True:
    
    if (pourcentage(potentiometre.value) < 33) :
        ledB.value = True
        ledR.value = ledG.value = False
    elif (pourcentage(potentiometre.value) >= 33 and pourcentage(potentiometre.value) < 66) :
        ledG.value = True
        ledR.value = ledB.value = False
    else : 
        ledR.value = True
        ledG.value = ledB.value = False
    
    sleep(0.1)