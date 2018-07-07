enable mouse in Kivy on RPi
- edit `nano ~/.kivy/config.ini`
- add `touchring = show_cursor=true` under [modules] at the bottom of the file

uninvert mouse y axis for Kivy on RPi
- edit `/usr/local/lib/python2.7/dist-packages/kivy/input/providers/hidinput.py`
- update around line 417 to the following `invert_y = int(bool(drs('invert_y', 0)))`

fml?
