"""
Scan I2C – Programme à compléter (CircuitPython)
Objectif : détecter les périphériques I2C (ex. OLED SSD1306) branchés sur la Pico.
Matériel typique : OLED I2C (adresse attendue souvent 0x3C).
À compléter :
- TODO(1) : choisir les broches I2C (GP1=SCL / GP0=SDA) ou board.SCL/board.SDA
- TODO(2) : afficher un message différent si 0x3C est trouvé
- TODO(3) : ajouter une petite “aide au debug” si rien n’est détecté
"""
import time
import board
import busio
import adafruit_ssd1306
# ========= CONFIG =========
# TODO(1) : Choisir l’un des deux modes :
# 1) Broches de la Pico :
I2C_SCL = board.GP7
I2C_SDA = board.GP6
# =========================
# Crée le bus I2C
i2c = busio.I2C(I2C_SCL, I2C_SDA)
# Attendre que le bus soit libre
print("Initialisation I2C...")
while not i2c.try_lock():
    pass
try:
    print("Scan I2C en cours...")
    adresses = i2c.scan() # renvoie une liste d'entiers (adresses 7 bits)
finally:
    i2c.unlock()
if adresses:
    print("Périphériques détectés :", [hex(a) for a in adresses])
    # TODO(2) : si 0x3C est dans la liste, afficher un message spécifique
    for a in adresses :
        if '0x3c' == hex(a) :
            print("0x3c est présent !")
else:
    print("Aucun périphérique I2C détecté.")
    # TODO(3) : donner des pistes de debug aux étudiants
    print("Pistes de vérification :")
    print(" - GND commun entre la Pico et le module ?")
    print(" - les pins sont bien des pins SDA/SCL (voir le schéma des pins du raspberry pi) ?")
    print(" - Si oui, ils sont pas inversés ?")