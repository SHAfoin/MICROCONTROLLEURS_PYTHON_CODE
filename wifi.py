# dans settings.toml
# CIRCUITPY_WIFI_SSID = "C:\Users\baobab\not_a_virus.exe"
# CIRCUITPY_WIFI_PASSWORD = "xxxxxxxxxxxxxxxxxxxxxx"

import os
import ipaddress
import wifi
import socketpool
print()
print("Tentative de connection au WiFi de SSID ",os.getenv('CIRCUITPY_WIFI_SSID'))
# connect to your SSID
wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))
print("Connecté au WiFi")
pool = socketpool.SocketPool(wifi.radio)
# Affiche l'adresse MAC sur le terminal REPL
print("Mon adresse MAC :", [hex(i) for i in wifi.radio.mac_address])
# Affiche l'adresse IP sur le terminal REPL
print("Mon adresse IP ", wifi.radio.ipv4_address)