from machine import Pin
import random
from neopixel import NeoPixel
from time import sleep_ms
randtala = random.randint(1,8)

segulA = Pin(12, Pin.IN, Pin.PULL_UP)
segulB = Pin(13, Pin.IN, Pin.PULL_UP)
segulC = Pin(14, Pin.IN, Pin.PULL_UP)
segulD = Pin(15, Pin.IN, Pin.PULL_UP)
segulE = Pin(16, Pin.IN, Pin.PULL_UP)
segulF = Pin(17, Pin.IN, Pin.PULL_UP)
segulG = Pin(18, Pin.IN, Pin.PULL_UP)
segulH = Pin(19, Pin.IN, Pin.PULL_UP)
segulI = Pin(20, Pin.IN, Pin.PULL_UP)
segulJ = Pin(21, Pin.IN, Pin.PULL_UP)
takki_a = Pin(11, Pin.IN, Pin.PULL_DOWN)
#hatalari_active = Pin(7, Pin.OUT) # Pinni 7 skilgreindur sem úttakspinni (stafrænn)


def valnartolur():
    if segulA.value == 1:
        valinTala1 = True

    if segulB.value == 1:
        valinTala2 = True

    if segulC.value == 1:
        valinTala3 = True

    if segulD.value == 1:
        valinTala4 = True

    if segulE.value == 1:
        valinTala5 = True

    if segulF.value == 1:
        valinTala6 = True

    if segulG.value == 1:
        valinTala7 = True

    if segulH.value == 1:
        valinTala8 = True


    if segulI.value == 1: 
        raudur = True
        
    if segulJ.value == 1:
        svartur = True

def rula():
    #setja inn kóða fyrir að ljósið að rúla
    neo = NeoPixel(Pin(14), 16)
    staerd = 16
    
    staða = 0
    
    while True:
        neo.fill((0, 0, 0))
        neo[staða] = (255, 0, 0)
        neo[(staða + 1) % staerd] = (255, 0, 0)
        neo.write()
        sleep_ms(100)
        staða = (staða + 1) % staerd    
    randtala = random.randint(1,8)
    if valinTala1 and randtala==1:
        vann()
    elif valinTala2 and randtala==2:
        vann()
    elif valinTala3 and randtala==3:
        vann()
    elif valinTala4 and randtala==4:
        vann()
    elif valinTala5 and randtala==5:
        vann()
    elif valinTala6 and randtala==6:
        vann()
    elif valinTala7 and randtala==7:
        vann()
    elif valinTala8 and randtala==8:
        vann()
    elif raudur and randtala.isOdd():
        vann()
    elif svartur and randtala.isEven():
        vann()
    else:
        tapp()

def vann():
    #setja in blikk og tónlist fyrir að vinna og eyða síðan pass
    print("vann")
def tapp():
    print("tapp")
while True:
    #if takki_a.value == 1:
        valnartolur()
        rula()

