from machine import Pin, PWM, freq
import time

pwm = PWM(Pin(18))
L_tones = [262, 294, 330, 349, 392, 440, 494 ]
M_tones = [523, 587, 659, 698, 784, 880, 988 ]
H_tones = [1046, 1175, 1318, 1397, 1568, 1760, 1967]

duration = 125

while True:
    for f in range(len(L_tones)):
        pwm.freq(L_tones[f])
        pwm.duty_u16(4000)
        time.sleep_ms(125)
        
    for f in range(len(M_tones)):
        pwm.freq(M_tones[f])
        pwm.duty_u16(4000)
        time.sleep_ms(62)
        
    for f in range(len(H_tones)):
        pwm.freq(H_tones[f])
        pwm.duty_u16(4000)
        time.sleep_ms(187)