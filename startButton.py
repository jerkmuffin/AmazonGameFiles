import RPi.GPIO as g
import time
import requests

PIN = 8 # senser PIN Hook the other side to GROUND
g.setmode(g.BOARD)
g.setup(PIN, g.IN, pull_up_down=g.PUD_UP)


class StartTimerButton(object):
    def __init__(self, butt_pin):
        self.press = False
        self.start_url = "https://darkopstest.azurewebsites.net/api/start"
        self.bp = butt_pin

    def _call_api(self):
        ret = requests.get(self.start_url)
        if ret.status_code == 200:
            print("okie dokie")
            self.press = False
            time.sleep(2)
        else:
            print("uh oh {}".format(ret.status_code))

    def run(self):
        while True:
            if not g.input(self.bp) and not self.press:
                self.press = True
                self._call_api()
            else:
                time.sleep(0.1)

if __name__ == "__main__":
    StartTimerButton(PIN).run()
