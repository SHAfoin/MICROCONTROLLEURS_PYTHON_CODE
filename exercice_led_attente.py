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
    ledR.value = ledG.value = ledB.value = True
    print("Attente :", fraction(potentiometre.value) * 5, "s")
    sleep(fraction(potentiometre.value) * 5)
    ledR.value = ledG.value = ledB.value = False
    sleep(fraction(potentiometre.value) * 5)