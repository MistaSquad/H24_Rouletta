from machine import machine
import random
randtala = random.randint(1,8)

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


    if segulK.value == 1: 
        raudur = True
        
    if segulL.value == 1:
        svartur = True

def rula(valnartolurnar):
    randtala = random.randint(1,8)
    if valinTala1 and randtala==1:

    elif valinTala2 and randtala==2:

    elif valinTala3 and randtala==3:

    elif valinTala4 and randtala==4:

    elif valinTala5 and randtala==5:

    elif valinTala6 and randtala==6:

    elif valinTala7 and randtala==7:

    elif valinTala8 and randtala==8:

    elif raudur and randtala.isOdd():
        
    elif svartur and randtala.isEven():

    else:
        


