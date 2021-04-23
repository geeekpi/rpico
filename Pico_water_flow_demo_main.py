# streaming led
from machine import Pin
import time

leds = []
for i in range(1,7):
    leds.append(Pin(i, Pin.OUT))
    print(leds)

while True:
    for led in leds:
        led.value(1)
        time.sleep(0.01)
        led.value(0)
        time.sleep(0.01)