from machine import Pin, PWM
import time

led1 = Pin(1, Pin.OUT)
led2 = Pin(2, Pin.OUT)
led3 = Pin(3, Pin.OUT)
led4 = Pin(4, Pin.OUT)


pwm = PWM(Pin(28))
#           do   re  mi    fa   sao  la   si   
L_tones = [262, 294, 330, 349, 392, 440, 494 ]
M_tones = [523, 587, 659, 698, 784, 880, 988 ]
H_tones = [1046, 1175, 1318, 1397, 1568, 1760, 1967]

# durations = [125, 62, 187, 94, 250, 125 ]
durations = [125,62,62,125,125]

twotigers = [262, 294, 330, 262, 262, 294, 330, 262, 330, 349, 392, 330, 349, 392, 392,
             440, 392, 349, 330,262, 392,440, 392, 349, 330, 262, 262, 392, 262, 262, 392, 262 ]

def play_atone(tone, duration):
    pwm.freq(tone)
    pwm.duty_u16(4000)
    time.sleep_ms(duration)

while True:
    for f in range(len(twotigers)):
        for d in range(len(durations)):
            play_atone(twotigers[f], durations[d])
            led1.toggle()
            time.sleep(0.01)
            led2.toggle()
            time.sleep(0.01)
            led3.toggle()
            time.sleep(0.01)
            led4.toggle()
        
     