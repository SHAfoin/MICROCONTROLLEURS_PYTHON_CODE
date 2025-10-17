from time import sleep, time
import random
import board
from digitalio import DigitalInOut, Direction
import analogio

def pourcentage(input) :
    return input/65535.0*100
    
def can(input) :
    return input/65535.0*3.3
    

potentiometre = analogio.AnalogIn(board.GP26)
while True:
    print("Valeur du potentiomètre:", pourcentage(potentiometre.value), "%")
    print("Valeur du potentiomètre (pourcent):", pourcentage(potentiometre.value), "%")
    print("Valeur du potentiomètre (CAN) :", can(potentiometre.value), "V")
    sleep(0.5)