from time import sleep
import board
import busio
import adafruit_ssd1306
import adafruit_dht

dht = adafruit_dht.DHT22(board.GP19)
I2C_SCL = board.GP7
I2C_SDA = board.GP6

i2c = busio.I2C(I2C_SCL, I2C_SDA)

N = 64 ; buf = [None] * N ; head = 0 ; size = 0

def push(v):
    global head, size
    buf[(head + size) % N] = v
    if size < N:
        size += 1
    else:
        head = (head + 1) % N

def as_list():  # ordre ancien→récent
    return [buf[(head + i) % N] for i in range(size)]


def lire_capteur():
    return (dht.temperature, dht.humidity)


def goutte_d_eau(x, y, color):
    display.pixel(x + 3, y, color)
    display.pixel(x + 4, y, color)
    display.pixel(x + 3, y + 1, color)
    display.pixel(x + 4, y + 1, color)
    display.pixel(x + 2, y + 2, color)
    display.pixel(x + 3, y + 2, color)
    display.pixel(x + 4, y + 2, color)
    display.pixel(x + 5, y + 2, color)
    display.pixel(x + 2, y + 3, color)
    display.pixel(x + 3, y + 3, color)
    display.pixel(x + 4, y + 3, color)
    display.pixel(x + 5, y + 3, color)
    display.pixel(x + 1, y + 4, color)
    display.pixel(x + 2, y + 4, color)
    display.pixel(x + 3, y + 4, color)
    display.pixel(x + 4, y + 4, color)
    display.pixel(x + 5, y + 4, color)
    display.pixel(x + 6, y + 4, color)
    display.pixel(x + 1, y + 5, color)
    display.pixel(x + 2, y + 5, color)
    display.pixel(x + 3, y + 5, color)
    display.pixel(x + 4, y + 5, color)
    display.pixel(x + 5, y + 5, color)
    display.pixel(x + 6, y + 5, color)
    display.pixel(x + 2, y + 6, color)
    display.pixel(x + 3, y + 6, color)
    display.pixel(x + 4, y + 6, color)
    display.pixel(x + 5, y + 6, color)


def rectangle(x, y, largeur, longueur, color):
    for i in range(x, x + longueur + 1):
        display.pixel(i, y, color)
        display.pixel(i, y + largeur, color)
    for i in range(y + 1, y + largeur + 1):
        display.pixel(x, i, color)
        display.pixel(x + longueur, i, color)


def thermometre(x, y, color):
    display.pixel(x + 3, y, color)
    display.pixel(x + 4, y, color)
    display.pixel(x + 3, y + 1, color)
    display.pixel(x + 4, y + 1, color)
    display.pixel(x + 3, y + 2, color)
    display.pixel(x + 4, y + 2, color)
    display.pixel(x + 3, y + 3, color)
    display.pixel(x + 4, y + 3, color)
    display.pixel(x + 2, y + 4, color)
    display.pixel(x + 3, y + 4, color)
    display.pixel(x + 4, y + 4, color)
    display.pixel(x + 5, y + 4, color)
    display.pixel(x + 2, y + 5, color)
    display.pixel(x + 5, y + 5, color)
    display.pixel(x + 2, y + 6, color)
    display.pixel(x + 3, y + 6, color)
    display.pixel(x + 4, y + 6, color)
    display.pixel(x + 5, y + 6, color)


print("Initialisation I2C...")
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

BORNE_SUPERIEURE = 65
BORNE_INFERIEURE = 45
HAUTEUR_COURBE = 10

def afficher_courbe():
    historique = as_list()
    for i, v in enumerate(historique):
        if v is None:
            continue
        else:
            x = (
                3 + i * 2
            )  # on décale de 4 à gauche et les colonnes auront 2 d'épaisseur
            y = 30 - int(
                (max(min(v, BORNE_SUPERIEURE), BORNE_INFERIEURE) - BORNE_INFERIEURE)
                / (BORNE_SUPERIEURE - BORNE_INFERIEURE)
                * HAUTEUR_COURBE
            )
            print(y)
            # on dessine les colonnes
            for j in range(y, 30):
                for k in range(2):
                    display.pixel(x + k, j, 1)


while True:

    temperature, humidite = lire_capteur()
    push(humidite)
    temperature_text = "Temp : " + str(temperature) + " C"
    humidite_text = "Hum : " + str(humidite) + " %"

    # Affichage des informations
    display.fill(0)
    display.text(temperature_text, 12, 4, 1)
    display.text(humidite_text, 12, 12, 1)
    # Affichage des logos
    thermometre(4, 4, 1)
    goutte_d_eau(4, 12, 1)
    rectangle(2, 2, 28, 124, 1)

    afficher_courbe()

    display.show()
    sleep(0.1)
