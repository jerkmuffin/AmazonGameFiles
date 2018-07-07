from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
# from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout


class plinthBox(GridLayout):
    pass

class pushy(GridLayout):
    pass

class makeitgoApp(App):
    def build(self):
        bigLay = GridLayout()
        bigLay.cols = 4
        bigLay.rows = 2
        a = pushy()
        for i in range(0,4):
            x = plinthBox()
            bigLay.add_widget(x)
        bigLay.add_widget(a)
        return bigLay


if __name__ == "__main__":
    makeitgoApp().run()
