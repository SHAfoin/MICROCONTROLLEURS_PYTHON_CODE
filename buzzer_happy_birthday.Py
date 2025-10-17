import time
import board
import pwmio

# Initialiser le buzzer pour la sortie PWM
buzzer = pwmio.PWMOut(board.GP26, variable_frequency=True)

# Durée d'une note noire
noire = 300
TempsNote = 60 / noire

do,re,mi,fa,sol,la,si = 32.7,36.71,41.20,43.65,49,55,61.74
A, B, C, D, E, F, G = la, si, do, re, mi, fa, sol 
A4, B4, C4, D4, E4, F4, G4 = 440, 493.88, 261.63, 293.66, 329.63, 349.23, 392

happyBirtday = [D4, D4, E4, D4, G4, F4, D4, D4, E4, D4, A4, G4, D4, D4]
happyBirthday_temps = [1,1,1,1,1,4,1,1,1,1,1,4,1,1]

def jouer_son(frequence, duree):
    # Définir la fréquence du buzzer
    buzzer.frequency = int(frequence)
    # Allumer le buzzer à 50% de volume (duty cycle)
    buzzer.duty_cycle = 65535 // 2
    # Attendre la durée de la note
    time.sleep(float(duree)*TempsNote)
    # Éteindre le buzzer
    buzzer.duty_cycle = 0
    
for i in range(len(happyBirtday)) :
    jouer_son(happyBirtday[i], happyBirthday_temps[i])
    
