import time
import board
import busio
import adafruit_ssd1306

I2C_SCL = board.GP7
I2C_SDA = board.GP6

i2c = busio.I2C(I2C_SCL, I2C_SDA)

print("Initialisation I2C...")
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

display.fill(0)
display.text('Hello', 0,1, 1)
display.show()
