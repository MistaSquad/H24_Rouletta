from machine import Pin
import random
from neopixel import NeoPixel
from time import sleep_ms
randtala = random.randint(1,8)

segulA = Pin(48, Pin.IN, Pin.PULL_UP)
segulB = Pin(47, Pin.IN, Pin.PULL_UP)
segulC = Pin(10, Pin.IN, Pin.PULL_UP)
segulD = Pin(11, Pin.IN, Pin.PULL_UP)
segulE = Pin(8, Pin.IN, Pin.PULL_UP)
segulF = Pin(9, Pin.IN, Pin.PULL_UP)
segulG = Pin(18, Pin.IN, Pin.PULL_UP)
segulH = Pin(17, Pin.IN, Pin.PULL_UP)
segulI = Pin(14, Pin.IN, Pin.PULL_UP)
segulJ = Pin(13, Pin.IN, Pin.PULL_UP)
takki_a = Pin(39, Pin.IN, Pin.PULL_DOWN)
neo = NeoPixel(Pin(38), 16)
#hatalari_active = Pin(7, Pin.OUT) # Pinni 7 skilgreindur sem úttakspinni (stafrænn)


def valnartolur():
    '''
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
        '''
    val=input(int("veldu tölu"))

def rula():
    #setja inn kóða fyrir að ljósið að rúla
    staerd = 16
    staða = 0
    while True:
        randtala = random.randint(1,8)
        neo.fill((0, 0, 0))
        neo[staða] = (255, 0, 0)
        neo[(staða + 1) % staerd] = (255, 0, 0)
        neo.write()
        sleep_ms(100)
        staða = (staða + 1) % staerd    
    if valinTala1 and randtala==1:
        vann()
        print("1 vann")
    elif valinTala2 and randtala==2:
        vann()
        print("2 vann")
    elif valinTala3 and randtala==3:
        vann()
        print("3 vann")
    elif valinTala4 and randtala==4:
        vann()
        print("4 vann")
    elif valinTala5 and randtala==5:
        vann()
        print("5 vann")
    elif valinTala6 and randtala==6:
        vann()
        print("6 vann")
    elif valinTala7 and randtala==7:
        vann()
        print("7 vann")
    elif valinTala8 and randtala==8:
        vann()
        print("8 vann")
    elif raudur and randtala.isOdd():
        vann()
        print("raudur vann")
    elif svartur and randtala.isEven():
        vann()
        print("svartur vann")
    else:
        tapp()

def vann():
    #setja in blikk og tónlist fyrir að vinna og eyða síðan pass
    # Spila sigur tónlist fyrir sigurvegara
    hatalari.freq(10000)  # Há tíðni
    hatalari.duty(1000)  # Fullur styrkur
    sleep_ms(100)  # Spila í stuttan tíma
    hatalari.duty(0)  # Slökkva
    sleep_ms(100)  # Bíða stutt
    victory_melodia = [392, 330, 440, 494, 523]  # Sigurtónar
    for tone in victory_melodia:
        hatalari.freq(tone)  # Tíðni fyrir tón
        hatalari.duty(1000)  # Stillt á styrk
        sleep_ms(300)  # Spila tón
        hatalari.duty(0)  # Slökkva á hljóði
        sleep_ms(100)  # Bíða
    print("vann")
def tapp():
    print("tapp")
while True:
    #if takki_a.value == 1:
        valnartolur()
        rula()

