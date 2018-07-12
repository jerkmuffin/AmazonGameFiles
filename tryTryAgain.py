import RPi.GPIO as g
import requests

from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout

from pygame import mixer as mix

g.setmode(g.BOARD)
state = []
good_list = [33, 26, 23, 38]
super_state = []
bg_color = (1, 0, 0, 1)

baseURL = "https://darkopstest.azurewebsites.net/"


class PlaySounds(object):
    def __init__(self):
        mix.init()
        self.wrong = mix.Sound('wrong.wav')
        self.right = mix.Sound('right.wav')

    def right_sound(self):
        self.right.play()

    def wrong_sound(self):
        self.wrong.play()


sound = PlaySounds()


def superCB(chan, **kwargs):
    if chan in good_list:
        if kwargs['insert']:
            sound.right_sound()
            print("insert: {}".format(chan))
            super_state.append(chan)
        else:
            print("remove: {}".format(chan))
            super_state.remove(chan)

            return ([0.5, 0.5, 0.5, 1], False)
        if set(good_list) == set(good_list).intersection(super_state):
            print("ALL the right plugs!")
            return ([0, 1, 0, 1], True)
        return ([0, 1, 0, 1], False)
    else:
        if kwargs['insert']:
            sound.wrong_sound()
            print("super list: {}".format(super_state))
            return ([1, 0, 0, 1], False)
        else:

            return ([0.5, 0.5, 0.5, 1], False)


class PlinthBox(GridLayout):
    pass


class SocialShareButton(GridLayout):
    def start_stop_social_share(self, but_num):
        ret = requests.get(baseURL + 'api/record/{}'.format(but_num))
        if ret.status_code == 200:
            print("But_num {} returned: {}".format(but_num, ret.json()))
        else:
            print ret.status_code

class ButtTest(Button):
    def __init__(self, **kwargs):
        super(ButtTest, self).__init__(**kwargs)
        if kwargs:
            self.num = kwargs['num']
            self.text = str(self.num)
            g.setup(self.num, g.IN, pull_up_down=g.PUD_UP)
            self.lay = kwargs['lay']
            self.big_background_color = [0.1, 0.1, 0.1, 1]

    def changeBackGround(self, r, g, b, a):
        with self.lay.canvas.before:
            Color(r, g, b, a)
            self.rect = Rectangle(size=(1900, 1200), pos=self.lay.pos)

    def update(self, dt):
        if g.input(self.num):
            if self.num not in state:
                state.append(self.num)
                (little, big) = superCB(chan=self.num, insert=True)
                self.background_color = little
                if big:
                    self.changeBackGround(0, 1, 0, 1)
                else:
                    self.changeBackGround(0.1, 0.1, 0.1, 1)
        else:
            if self.num in state:
                state.remove(self.num)
                (little, big) = superCB(chan=self.num, insert=False)
                self.background_color = little
                if not big:
                    self.changeBackGround(0.1, 0.1, 0.1, 1)


class GoManApp(App):
    def add_space(self, lay):
        foo = Label(size_hint=[None, None])
        foo.height = "40dp"
        foo.width = "80dp"
        lay.add_widget(foo)

    def build(self):
        layout = GridLayout()
        layout.cols = 7
        layout.rows = 2
        with layout.canvas.before:
            Color(0.1, 0.1, 0.1, 1)
            self.rect = Rectangle(size=(1900,1200), pos=layout.pos)

        x = [13, 7, 33, 16, 37, 40]
        a = PlinthBox()
        for i in x:
            exec("butt{} = ButtTest(num={}, lay=layout)".format(i, i))
            exec("Clock.schedule_interval(butt{}.update, 1.0/10.0)".format(i))
            exec("a.add_widget(butt{})".format(i))
        layout.add_widget(a)

        self.add_space(layout)

        y = [24, 21, 23, 19, 11, 12]
        b = PlinthBox()
        for i in y:
            exec("butt{} = ButtTest(num={}, lay=layout)".format(i, i))
            exec("Clock.schedule_interval(butt{}.update, 1.0/10.0)".format(i))
            exec("b.add_widget(butt{})".format(i))
        layout.add_widget(b)

        self.add_space(layout)

        w = [18, 29, 26, 22, 31, 36]
        c = PlinthBox()
        for i in w:
            exec("butt{} = ButtTest(num={}, lay=layout)".format(i, i))
            exec("Clock.schedule_interval(butt{}.update, 1.0/10.0)".format(i))
            exec("c.add_widget(butt{})".format(i))
        layout.add_widget(c)

        self.add_space(layout)

        z = [8, 15, 38, 35, 32, 10]
        d = PlinthBox()
        for i in z:
            exec("butt{} = ButtTest(num={}, lay=layout)".format(i, i))
            exec("Clock.schedule_interval(butt{}.update, 1.0/10.0)".format(i))
            exec("d.add_widget(butt{})".format(i))
        layout.add_widget(d)

        buttons = SocialShareButton()
        layout.add_widget(buttons)
        return layout


if __name__ == "__main__":
    try:
        GoManApp().run()
    except KeyboardInterrupt:
        App.get_running_app().stop()
        g.cleanup()
