from ui import Button, Text
from .scene import Scene
from pyglet.window.mouse import *

class WelcomeScreen(Scene):
    def __init__(self, window):
        super().__init__(window)
        window.set_caption('Welcome to tabulr')
        self.title = Text('Welcome to', batch=self.batch,
                          x=self.margin_left, y=(self.window.height//2) + 100)
        self.title_bold = Text('tabulr', bold=True, batch=self.batch,
                               x=self.margin_left, y=(self.window.height//2) + 60)
        self.subtitle = Text('Your schedule, from list to wallpaper. Like magic.', size=12, batch=self.batch,
                             x=self.margin_left, y=self.window.height//2)
        self.init_sprite('next_button', Button('next', self.window, self.batch,
                                               x=self.margin_left, y=(self.window.height//2) - 100))

    def update(self, dt):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        if button == LEFT:
            if self.is_clicked('next_button', x, y):
                print('clicked next button')

    def on_mouse_motion(self, x, y, dx, dy):
        next_button = self.sprites['next_button']
        image_width = next_button.x + next_button.width
        image_height = next_button.y + next_button.height
        if image_width > x > next_button.x and image_height > y > next_button.y:
            next_button.on_mouse_enter()
        else:
            next_button.on_mouse_leave()
