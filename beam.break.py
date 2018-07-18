#!/usr/bin/env python

import RPi.GPIO as g
import requests
import time

g.setmode(g.BOARD)
g.setup(7, g.IN, pull_up_down=g.PUD_DOWN)
g.setup(5, g.OUT)
g.output(5, 1)

baseURL = "http://192.168.10.246:8080/"

def fire():
  try:
    ret = requests.get(baseURL + 'api/record/4')
    if ret.status_code == 200:
      print("returned: {}".format(ret.json()))
  except:
    print ret.status_code

  g.output(5, 0)
  time.sleep(0.5)
  g.output(5, 1)

print "fire"
fire()
print "fired"

while True:
  if g.input(7) == 1:
    fire()
    time.sleep(2)
  else:
    time.sleep(0.2)



