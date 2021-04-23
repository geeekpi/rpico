from machine import Pin, I2C, SPI, PWM
import st7789py as st7789
from fonts import vga2_8x8 as font1
from fonts import vga1_16x32 as font2
import time
import struct

# spi
SCK = Pin(2)
MOSI = Pin(3)
RST = Pin(0, Pin.OUT)
DC = Pin(1, Pin.OUT)
pwm = PWM(Pin(28))

SCL = Pin(11)
SDA = Pin(10)
BUS = 1 

width = 240
height = 240 

# inititializing SPI and I2C ,PWM
spi0 = SPI(0, baudrate=40000000, polarity=1, phase=0, sck=SCK,mosi=MOSI)

# PWM section
# pwm.freq(1000)
# duty = 0 
# direction = 1

# I2C section
mma7660 = I2C(BUS,scl=SCL, sda=SDA, freq=40000000)

# Display section
display = st7789.ST7789(spi0, width, height, reset=RST, dc=DC,xstart=0, ystart=0,rotation=0)

display.fill(st7789.color565(255,255,0))
time.sleep(2)
display.fill(st7789.BLACK)
display.text(font2,"Hello MMA7660", 10, 10)

address = mma7660.scan()
print("I2C address:%x", hex(address[1]))
display.text(font2,"I2C addr: %x" %address[1] , 10, 40)

print("激活 MMA7660")
# 向寄存器 0x07写入 1
mma7660.writeto_mem(76, 7, b'1')
# The 6-bit measurement data is stored in the XOUT (0x00), YOUT (0x01), and ZOUT (0x02) registers 
try:
    while True:
        x= mma7660.readfrom_mem(76, 0, 6)
        y= mma7660.readfrom_mem(76, 1, 6)
        z= mma7660.readfrom_mem(76, 2, 6)

        xout = struct.unpack('>f', x)[0]
        yout = struct.unpack('>f', y)[0]
        zout = struct.unpack('>f', z)[0]

        print('x:{:+.10f},y:{:+.10f},z:{:+.10f}'.format(xout,yout,zout))
        display.text(font2,"x:{:.3f}".format(xout), 10, 80)
        display.text(font2,"y:{:.3f}".format(yout), 10, 120)
        display.text(font2,"z:{:.3f}".format(zout), 10, 160)
except KeyboardInterrupt:
    print("QUIT")
    display.fill(st7789.color565(255,0,0))
    display.text(font2, "GOOD BYE", 80, 120)





