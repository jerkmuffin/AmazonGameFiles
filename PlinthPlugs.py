#!/usr/bin/env python2

# Plinth plug game.  Check for patches, cue right/wrong  audio when a patch is made
# Need to be monitored from back of house.  KIVY?  Or some kinda LED???
# pretty ugly but working pretty bug free with looping through the inputs and checking a state list.

import RPi.GPIO as g
import time
from omxplayer.player import OMXPlayer

import multiprocessing as mp

from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.stacklayout import StackLayout

class Fml(StackLayout):

    # def __init__ (self, **kwargs):
    #     super(Fml, self).__init__(**kwargs)
    #     self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
    #     self._keyboard.bind(on_key_down=self._on_keyboard_down)
    #
    color_change = ObjectProperty()
    #
    # def _keyboard_closed(self):
    #     self._keyboard.unbind(on_key_down=self._on_keyboard_down)
    #     self._keyboard = None
    #
    # def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
    #     if keycode:
    #         print(keycode)
    #     if keycode[1] == 'x':
    #         self.color_change.text = 'X'
    #         self.color_change.background_color = [1, 0, 0, 1]
    #     return True
    pass

class PatcherApp(App):
    pass


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
        print('run: running')
        while True:
            for i in self.list:
                if g.input(i):
                    self.cb(i)
                else:
                    if i in self.state:
                        self.state.remove(i)
            time.sleep(0.1)


if __name__ == "__main__":
    Foo = PlugCheck()
    # Bar = PatcherApp()
    # Foo.run()
    p = mp.Process(target=Foo.run, args=())
    p.start()
    q = mp.Process(target=PatcherApp().run(), args=())
    q.start()
    print('and then')
    # PatcherApp().run()
