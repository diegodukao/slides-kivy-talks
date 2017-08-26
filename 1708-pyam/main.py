from kivy.app import App
from kivy.config import Config
from kivy.core.window import Keyboard, Window
from kivy.utils import get_color_from_hex

from pdfexporter import save_screenshot


class Slides(App):

    def on_key_down(self, window, key, *args):
        if key == Keyboard.keycodes['right']:
            self.root.load_next()
        if key == Keyboard.keycodes['left']:
            self.root.load_previous()
        if key == Keyboard.keycodes['down']:
            save_screenshot(self.root.index)

    def on_start(self):
        Window.bind(on_key_down=self.on_key_down)

if __name__ == "__main__":
    Window.clearcolor = get_color_from_hex('#FFFFFF')
    Window.size = (1280, 960)
    # Window.fullscreen = True
    Config.write()
    Slides().run()
