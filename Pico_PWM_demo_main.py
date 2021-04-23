import time
from machine import Pin, PWM
from random import randint


pwm = PWM(Pin(1))
pwm.freq(1000)
duty = 0
direct = 1
notes = [262, 294, 330, 349, 392, 440, 494]

while True:
    freq = notes[randint(0, 6)]    
    pwm.freq(freq)
    for _ in range(8*256):
        duty += direct
        if duty > 255:
            duty = 255
            direct = -1
        elif duty < 0:
            duty = 0
            direct = 1
        pwm.duty_u16(duty * duty)
        time.sleep(0.001)
