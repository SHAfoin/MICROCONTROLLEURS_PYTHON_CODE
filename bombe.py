from time import sleep, time 
import random
import board
from digitalio import DigitalInOut, Direction
import analogio
import pwmio

ledR = DigitalInOut(board.GP19)
ledR.direction = Direction.OUTPUT
ledG = DigitalInOut(board.GP20)
ledG.direction = Direction.OUTPUT
ledB = DigitalInOut(board.GP21)
ledB.direction = Direction.OUTPUT

bouton = DigitalInOut(board.GP16)
bouton.direction = Direction.INPUT

led = DigitalInOut(board.GP18)
led.direction = Direction.OUTPUT

potentiometre = analogio.AnalogIn(board.GP27)

buzzer = pwmio.PWMOut(board.GP26, variable_frequency=True)

noire = 200
TempsNote = 60 / noire

do,re,mi,fa,sol,la,si = 32.7,36.71,41.20,43.65,49,55,61.74
do4,re4,mi4,fa4,sol4,la4,si4 = 523.25,587.33,659.26,698.46,783.99,880,987.77
auClairDeLaLune = [do4, do4, do4, re4, mi4, re4, do4, mi4, re4, re4, do4]
auClairDeLaLune_temps = [1,1,1,1,2,2,1,1,1,1,2]

def jouer_son(frequence, duree):
    # Définir la fréquence du buzzer
    buzzer.frequency = int(frequence)
    # Allumer le buzzer à 50% de volume (duty cycle)
    buzzer.duty_cycle = 65535 // 2
    # Attendre la durée de la note
    sleep(float(duree)*TempsNote)
    # Éteindre le buzzer
    buzzer.duty_cycle = 0

def read_potentiometre() :
    return int(potentiometre.value/65535.0*90+10)

start_time = time()
max_time = 10
code_secret = random.randint(10,100)
last_valeur = 0
victory = False
last_bouton = False
ledB.value = ledR.value = ledG.value = True

while (victory == False and time() - start_time < max_time) : 

    valeur = read_potentiometre()
    if last_valeur != valeur :
        print("Valeur :", valeur)
        last_valeur = valeur
    
    if bouton.value == True and last_bouton != True:
        if valeur < code_secret :
            ledR.value = False
            ledB.value = True
            ledG.value = True
            jouer_son(do4, 0.5)
        elif valeur > code_secret : 
            ledR.value = True
            ledB.value = False
            ledG.value = True
            jouer_son(do4, 0.5)
            sleep(0.2)
            jouer_son(do4, 0.5)
        else : 
            ledR.value = True
            ledB.value = True
            ledG.value = False
            
            led.value = False
            victory = True
        
    last_bouton = bouton.value
    sleep(0.1)
    
if victory :
    print("Bien joué ! C'était", code_secret)
    for i in range(len(auClairDeLaLune)) :
        jouer_son(auClairDeLaLune[i], auClairDeLaLune_temps[i])
else :
    print("BOOM ! C'était", code_secret)
    jouer_son(do4, 10)
    led.value = True

