import RPi.GPIO as g
import time
import requests


g.setmode(g.BOARD)
g.setup(8, g.IN, pull_up_down=g.PUD_UP)


class StopTimerButton(object):
    def __init__(self, butt_pin):
        self.latch = True
        self.start_url = "https://darkopstest.azurewebsites.net/api/stop"
        self.bp = butt_pin

    def _call_api(self):
        print('calling home')
        ret = requests.get(self.start_url)
        if ret.status_code == 200:
            print("okie dokie")
            time.sleep(2)
        else:
            print("uh oh {}".format(ret.status_code))

    def run(self):
        while True:
            if not g.input(8) and self.latch:
                self._call_api()
                self.latch = False
                print('...unlatching')
            elif g.input(8):
                print("locked")
                self.latch = True
            else:
                time.sleep(0.1)

if __name__ == "__main__":
    StopTimerButton(8).run()
