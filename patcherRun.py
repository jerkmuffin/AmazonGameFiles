# testing to learn about kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label


class Fml(StackLayout):
    pass

class PatcherApp(App):
    def build(self):
        return Fml()


if __name__ == "__main__":
    PatcherApp().run()
