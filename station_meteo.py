from time import sleep
import board
import busio
import adafruit_ssd1306
import adafruit_dht

dht = adafruit_dht.DHT22(board.GP19)
I2C_SCL = board.GP7
I2C_SDA = board.GP6

i2c = busio.I2C(I2C_SCL, I2C_SDA)

def lire_capteur() :
    return (dht.temperature, dht.humidity)

def goutte_d_eau(x, y, color) :
    display.pixel(x+3, y, color)
    display.pixel(x+4, y, color)
    display.pixel(x+3, y+1, color)
    display.pixel(x+4, y+1, color)
    display.pixel(x+2, y+2, color)
    display.pixel(x+3, y+2, color)
    display.pixel(x+4, y+2, color)
    display.pixel(x+5, y+2, color)
    display.pixel(x+2, y+3, color)
    display.pixel(x+3, y+3, color)
    display.pixel(x+4, y+3, color)
    display.pixel(x+5, y+3, color)
    display.pixel(x+1, y+4, color)
    display.pixel(x+2, y+4, color)
    display.pixel(x+3, y+4, color)
    display.pixel(x+4, y+4, color)
    display.pixel(x+5, y+4, color)
    display.pixel(x+6, y+4, color)
    display.pixel(x+1, y+5, color)
    display.pixel(x+2, y+5, color)
    display.pixel(x+3, y+5, color)
    display.pixel(x+4, y+5, color)
    display.pixel(x+5, y+5, color)
    display.pixel(x+6, y+5, color)
    display.pixel(x+2, y+6, color)
    display.pixel(x+3, y+6, color)
    display.pixel(x+4, y+6, color)
    display.pixel(x+5, y+6, color)

def rectangle (x, y, largeur, longueur, color) :
    for i in range(x, x+longueur+1) :
        display.pixel(i, y, color)
        display.pixel(i, y+largeur, color)
    for i in range(y+1, y+largeur+1) :
        display.pixel(x, i, color)
        display.pixel(x+longueur, i, color)

def thermometre(x, y, color) :
    display.pixel(x+3, y, color)
    display.pixel(x+4, y, color)
    display.pixel(x+3, y+1, color)
    display.pixel(x+4, y+1, color)
    display.pixel(x+3, y+2, color)
    display.pixel(x+4, y+2, color)
    display.pixel(x+3, y+3, color)
    display.pixel(x+4, y+3, color)
    display.pixel(x+2, y+4, color)
    display.pixel(x+3, y+4, color)
    display.pixel(x+4, y+4, color)
    display.pixel(x+5, y+4, color)
    display.pixel(x+2, y+5, color)
    display.pixel(x+5, y+5, color)
    display.pixel(x+2, y+6, color)
    display.pixel(x+3, y+6, color)
    display.pixel(x+4, y+6, color)
    display.pixel(x+5, y+6, color)

print("Initialisation I2C...")
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

while True :

    valeur = lire_capteur()
    temperature = "Temp : " + str(valeur[0]) + " C"
    humidite = "Hum : " + str(valeur[1]) + " %"

    display.fill(0)
    display.text(temperature, 16,8, 1)
    display.text(humidite, 16,16, 1)
    thermometre(8, 8, 1)
    goutte_d_eau(8,16,1)
    rectangle(4, 4, 26, 122, 1)
    display.show()
    sleep(2)

