#!/usr/bin/env python2

# Plinth plug game.  Check for patches, cue right/wrong  audio when a patch is made
# Need to be monitored from back of house.  KIVY?  Or some kinda LED???
# pretty ugly but working pretty bug free with looping through the inputs and checking a state list.

import RPi.GPIO as g
import time
from omxplayer.player import OMXPlayer




class PlugCheck(object):
    def __init__(self):
        self.list = [7, 16, 13, 33, 37, 40]
        self.list += [8, 10, 15, 32, 35, 38]
        self.list += [18, 22, 26, 29, 31, 36]
        self.list += [11, 12, 19, 21, 23, 24]
        self.state = []

        g.setmode(g.BOARD)
        for i in self.list:
            g.setup(i, g.IN, pull_up_down=g.PUD_UP)

    def horse(self, channel):
        print('horse {}'.format(channel))
        p = OMXPlayer("horse.mp3")

    def cat(self, channel):
        print('cat {}'.format(channel))
        p = OMXPlayer("Cat.mp3")

    def cb(self, chan):
        if chan not in self.state:
            self.state.append(chan)
            print(chan)

    def run(self):
        while True:
            for i in self.list:
                if g.input(i):
                    self.cb(i)
                else:
                    if i in self.state:
                        self.state.remove(i)
            time.sleep(0.1)

Foo = PlugCheck()
Foo.run()
