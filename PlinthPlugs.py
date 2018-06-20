#!/usr/bin/env python2

# Plinth plug game.  Check for patches, cue right/wrong  audio when a patch is made
# Need to be monitored from back of house.  KIVY?  Or some kinda LED???
# pretty ugly but working pretty bug free with looping through the inputs and checking a state list.

import RPi.GPIO as g
import time
from omxplayer.player import OMXPlayer

g.setmode(g.BOARD)
list =  [7, 16, 13, 33, 37, 40]
list += [8, 10, 15, 32, 35, 38]
list += [18, 22, 26, 29, 31, 36]
list += [11, 12, 19, 21, 23, 24]

state = []
def horse(channel):
    print('horse {}'.format(channel))
    p = OMXPlayer("horse.mp3")


def cat(channel):
    print('cat {}'.format(channel))
    p = OMXPlayer("Cat.mp3")

def cb(chan):
  if chan not in state:
    state.append(chan)
    print(chan)

for i in list:
  g.setup(i, g.IN, pull_up_down=g.PUD_UP)

while True:
  for i in list:
    if g.input(i):
      cb(i)
    else:
      if i in state:
        state.remove(i)
  time.sleep(0.1)
