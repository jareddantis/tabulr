from ui import Button, Text
from .scene import Scene
from pyglet.window.mouse import *
from pyglet.sprite import Sprite
from pyglet.resource import image

class WelcomeScreen(Scene):
    def __init__(self, window, bus):
        super().__init__(window, bus)
        self.title = Text('Welcome to', batch=self.batch,
                          x=self.margin, y=(self.window.height//2) + 100)
        self.title_bold = Text('tabulr', bold=True, batch=self.batch,
                               x=self.margin, y=(self.window.height//2) + 60)
        self.subtitle = Text('Your schedule, from list to wallpaper. Like magic.', size=12, batch=self.batch,
                             x=self.margin, y=self.window.height//2)
        self.init_sprite('next_button', Button('next', self.window, self.batch,
                                               x=self.margin, y=(self.window.height//2) - 100))

        waves = Sprite(image('front-waves.png'), x=0, y=0, batch=self.batch)
        waves.opacity = 160
        self.init_sprite('waves', waves)

    def on_draw(self):
        super().on_draw()
        self.window.set_caption('Welcome to tabulr')

    def on_mouse_press(self, x, y, button, modifiers):
        if button == LEFT:
            if self.is_clicked('next_button', x, y):
                self.bus.emit('next_scene')

    def on_mouse_motion(self, x, y, dx, dy):
        next_button = self.sprites['next_button']
        image_width = next_button.x + next_button.width
        image_height = next_button.y + next_button.height
        if image_width > x > next_button.x and image_height > y > next_button.y:
            next_button.on_mouse_enter()
        else:
            next_button.on_mouse_leave()
