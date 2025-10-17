import time
import board
import pwmio

# Initialiser le buzzer pour la sortie PWM
buzzer = pwmio.PWMOut(board.GP26, variable_frequency=True)

# Durée d'une note noire
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
    time.sleep(float(duree)*TempsNote)
    # Éteindre le buzzer
    buzzer.duty_cycle = 0
    
for i in range(len(auClairDeLaLune)) :
    jouer_son(auClairDeLaLune[i], auClairDeLaLune_temps[i])
    
