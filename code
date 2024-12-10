from machine import Pin, PWM
import random
from neopixel import NeoPixel
from time import sleep_ms

# Pin setup for magnetic switches
segul_pins = {
    1: Pin(48, Pin.IN, Pin.PULL_UP),
    2: Pin(47, Pin.IN, Pin.PULL_UP),
    3: Pin(10, Pin.IN, Pin.PULL_UP),
    4: Pin(11, Pin.IN, Pin.PULL_UP),
    5: Pin(8, Pin.IN, Pin.PULL_UP),
    6: Pin(9, Pin.IN, Pin.PULL_UP),
    7: Pin(18, Pin.IN, Pin.PULL_UP),
    8: Pin(17, Pin.IN, Pin.PULL_UP),
    'red': Pin(14, Pin.IN, Pin.PULL_UP),
    'black': Pin(13, Pin.IN, Pin.PULL_UP),
}

takki_a = Pin(39, Pin.IN, Pin.PULL_DOWN)  # Button to start the spin
neo = NeoPixel(Pin(38), 16)              # LEDs
hatalari = PWM(Pin(37))                  # Speaker for sounds
hatalari.duty(0)                         # Start with no sound

# State variables
selected_choices = set()  # Holds the selected pins (numbers or colors)


def detect_selections():
    """Waits for players to place magnets and finalize their selections."""
    global selected_choices
    selected_choices.clear()  # Reset previous choices
    print("Spilarar, setjið segla á valin pinna (1-8, rauður, svartur).")
    
    # Wait until at least one selection is detected
    while not selected_choices:
        for name, pin in segul_pins.items():
            if pin.value() == 0:  # Magnet detected (pin pulled low)
                selected_choices.add(name)

    print(f"Valdir möguleikar: {selected_choices}")
    print("Ýtið á takkann til að snúa hjólinu.")

    # Wait for button press to confirm all selections
    while takki_a.value() == 1:  # Wait until button is pressed
        pass  # Do nothing until button is pressed
    print("Hjólið byrjar að snúast!")


def spin_wheel():
    """Simulates the spinning of the roulette wheel."""
    staerd = 16
    staða = 0
    spin_speed = 100
    for i in range(30):  # Simulate the spinning effect
        neo.fill((0, 0, 0))
        neo[staða] = (255, 0, 0) if i % 2 == 0 else (0, 255, 0)  # Alternate colors for effect
        neo.write()
        sleep_ms(spin_speed)
        staða = (staða + 1) % staerd
        spin_speed += 10  # Gradually slow down

    # Determine the random result
    randtala = random.randint(1, 8)
    print(f"Roulette niðurstaða: {randtala} {'(Odd/Rauður)' if randtala % 2 == 1 else '(Even/Svartur)'}")
    return randtala


def check_results(randtala):
    """Checks if any of the selected choices match the random result."""
    if randtala in selected_choices:
        return True
    if 'red' in selected_choices and randtala % 2 == 1:  # Odd numbers
        return True
    if 'black' in selected_choices and randtala % 2 == 0:  # Even numbers
        return True
    return False


def play_victory_sound():
    """Plays the victory sound."""
    victory_melodia = [392, 330, 440, 494, 523]
    for tone in victory_melodia:
        hatalari.freq(tone)
        hatalari.duty(512)
        sleep_ms(300)
        hatalari.duty(0)
        sleep_ms(100)


def play_loss_sound():
    """Plays the loss sound."""
    for _ in range(3):  # Beep 3 times
        hatalari.freq(200)
        hatalari.duty(512)
        sleep_ms(200)
        hatalari.duty(0)
        sleep_ms(200)


# Main game loop
while True:
    print("Bíddu eftir vali spilaranna...")
    detect_selections()  # Wait for all players to make selections and press the button

    result = spin_wheel()  # Spin the wheel and get the result

    if check_results(result):
        print("Ein eða fleiri spilarar unnu!")
        play_victory_sound()
    else:
        print("Enginn vann!")
        play_loss_sound()

    print("Nýr leikur byrjar. Veljið aftur!")

