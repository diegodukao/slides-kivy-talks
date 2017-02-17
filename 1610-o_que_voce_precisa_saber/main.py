from kivy.app import App
from kivy.config import Config
from kivy.core.window import Keyboard, Window
from kivy.utils import get_color_from_hex


class Slides(App):

    def on_key_down(self, window, key, *args):
        if key == Keyboard.keycodes['right']:
            self.root.load_next()
        if key == Keyboard.keycodes['left']:
            self.root.load_previous()

    def on_start(self):
        Window.bind(on_key_down=self.on_key_down)

if __name__ == "__main__":
    Window.clearcolor = get_color_from_hex('#FFFFFF')
    Config.write()
    Slides().run()
