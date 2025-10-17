import board
import adafruit_dht
from time import sleep

dht = adafruit_dht.DHT22(board.GP19)

def lire_capteur() :
    return (dht.temperature, dht.humidity)

while True :
    
    valeur = lire_capteur()
    print("Temperature : ", valeur[0])
    print("Huimidité : ", valeur[1])
    sleep(2)