# testing to learn about kivy
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


if __name__ == "__main__":
    PatcherApp().run()
