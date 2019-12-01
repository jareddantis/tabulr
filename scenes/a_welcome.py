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
        self.init_sprite('waves', waves, is_button=False)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == LEFT:
            if self.sprites['next_button'][0].hit_test(x, y):
                self.bus.emit('next_scene')

    def on_mouse_motion(self, x, y, dx, dy):
        next_button = self.sprites['next_button'][0]
        image_width = next_button.x + next_button.width
        image_height = next_button.y + next_button.height
        if image_width > x > next_button.x and image_height > y > next_button.y:
            next_button.on_mouse_enter()
        else:
            next_button.on_mouse_leave()
