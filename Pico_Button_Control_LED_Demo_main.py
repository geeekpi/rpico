from machine import Pin
import time


led = Pin(10, Pin.OUT)
btn = Pin(18, Pin.IN, Pin.PULL_UP)

while True:
    if btn.value() == 0:
        print("BTN 1 is Pressed!")
        print(time.localtime())
        led.value(0)
        time.sleep(0.5)
    else:
        led.value(1)
        
