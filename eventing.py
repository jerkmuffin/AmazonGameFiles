from pygame import mixer as mix
import RPi.GPIO as g
import time
import os

button_led = 37
button_switch = 31
relay = 3


g.setmode(g.BOARD)
g.setup(button_led, g.OUT)
g.setup(relay, g.OUT)
g.setup(button_switch, g.IN, pull_up_down=g.PUD_UP)
g.output(button_led, 1)
switch_state = False
magneted_chans = []

mix.init(96000)
right = mix.Sound('right.ogg')
wrong = mix.Sound('wrong.ogg')
success = mix.Sound('success.ogg')

all_good = False
def cb(chan):
    if not g.input(chan):
        if chan not in magneted_chans:
            magneted_chans.append(chan)
            right.play()
    else:
        if chan in magneted_chans:
            magneted_chans.remove(chan)
            wrong.play()
    print("{} are magneted".format(magneted_chans))


# sense pins for hall effects
for i in [5, 7, 11, 13]:
    g.setup(i, g.IN, pull_up_down=g.PUD_UP)
    g.add_event_detect(i, g.BOTH, callback=cb, bouncetime=200)


while True:
    try:
        if len(magneted_chans) == 4:
            if all_good == False:
                success.play()
                all_good = True
            print('testing button')
            g.output(button_led, 0)
            if not switch_state:
                print('relay off')
                if g.input(button_switch) == 0:
                    print('button pressed relay was off')
                    g.output(relay, 1)
                    switch_state = True
                    time.sleep(2)
            if switch_state:
                print('relay on')
                if g.input(button_switch) == 0:
                    print('button pressed relay was on')
                    g.output(relay, 0)
                    switch_state = False
                    time.sleep(2)

        else:
            g.output(button_led, 1)
            all_good = False
        time.sleep(0.2)
    except KeyboardInterrupt:
        g.cleanup()
