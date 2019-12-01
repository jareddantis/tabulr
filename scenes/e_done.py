from .scene import Scene
from pyglet.resource import image
from pyglet.sprite import Sprite
from pyglet.window.mouse import *
from ui import Text, Button
from os.path import abspath

class DoneScreen(Scene):
    def __init__(self, window, bus):
        super().__init__(window, bus, draw_waves=False, title='tabulr | Done')

        # Check mark
        check_img = image('check.png')
        check_img.anchor_x = check_img.width // 2
        check_img.anchor_y = check_img.height // 2
        check_sprite = Sprite(check_img, x=self.window.width//2, y=self.window.height//2 + 120, batch=self.batch)
        check_sprite.scale = 0.5
        self.init_sprite('check', check_sprite, is_button=False)

        # Text
        self.title = Text('Done', batch=self.batch, size=22, bold=True,
                          x=self.window.width//2, y=self.window.height//3 + 72)
        self.subtitle = Text('Open the following file to save your wallpaper:', batch=self.batch, size=14,
                             x=self.window.width//2, y=self.window.height//3 + 8)
        self.path = Text(abspath('htmlfile.html'), batch=self.batch, size=8, bold=True,
                             x=self.window.width//2, y=self.window.height//3 - 16)
        self.title.anchor_x = 'center'
        self.subtitle.anchor_x = 'center'
        self.path.anchor_x = 'center'

        # Restart button
        restart_button = Button('restart', self.window, self.batch,
                                x=self.window.width//2, y=self.margin)
        restart_button.x -= restart_button.width//2
        self.init_sprite('restart_button', restart_button)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == LEFT and self.sprites['restart_button'][0].hit_test(x, y):
            self.bus.emit('start_over')
