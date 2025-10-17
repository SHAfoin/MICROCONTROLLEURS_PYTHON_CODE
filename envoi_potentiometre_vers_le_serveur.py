import wifi
import socketpool
import ssl
from time import sleep, time
import os
import ipaddress
import analogio
import board
from digitalio import DigitalInOut, Direction

ledR = DigitalInOut(board.GP21)
ledR.direction = Direction.OUTPUT
ledG = DigitalInOut(board.GP20)
ledG.direction = Direction.OUTPUT
ledB = DigitalInOut(board.GP19)
ledB.direction = Direction.OUTPUT

TIMEOUT = None
HOST = "192.168.1.111" # Adresse IP du serveur A MODIFIER
PORT = 12345 # Port du serveur

print("Tentative de connection au WiFi de SSID ",os.getenv('CIRCUITPY_WIFI_SSID'))

# connect to your SSID
wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))

print("Connecté au WiFi")

pool = socketpool.SocketPool(wifi.radio)

print("Creation de la socket")

potentiometre = analogio.AnalogIn(board.GP26)


with pool.socket(pool.AF_INET, pool.SOCK_STREAM) as s:
    s.settimeout(TIMEOUT)
    print("Connection au serveur")
    s.connect((HOST, PORT))
    while True : 
        
        print("Envoi")
        print("Valeur du potentiometre :", potentiometre.value) 
        
        # Envoi de chaînes de caractères
        # sent = s.send(b"Hello, world")
        # sent = s.send(b"quit")
        
        #Envoi de la valeur du potentiometre
        # Convertir l'entier en string
        string_value = str(potentiometre.value)
        
        # Convertir le string en bytes
        byte_value = string_value.encode('utf-8')
        sent = s.send(byte_value)
        
        print("Réception")
        buff = bytearray(128)
        numbytes = s.recv_into(buff)
        
        print(buff.decode('utf-8').strip())
        
        if "Bleu" in buff.decode('utf-8') :
            print("Passage en bleu")
            ledB.value = True
            ledR.value = ledG.value = False
        elif "Rouge" in buff.decode('utf-8'): 
            print("Passage en rouge")
            ledR.value = True
            ledB.value = ledG.value = False
        else : 
            print("Passage en vert")
            ledG.value = True
            ledB.value = ledR.value = False
            
        sleep(2)
    
