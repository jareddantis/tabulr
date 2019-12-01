from .scene import Scene
from pyglet.resource import image
from pyglet.sprite import Sprite
from ui import Text

class GeneratorScreen(Scene):
    def __init__(self, window, bus):
        super().__init__(window, bus, draw_waves=True, title='Generating')

        # Spinner
        self.elapsed = 0
        spinner_img = image('spinner.png')
        spinner_img.anchor_x = spinner_img.width // 2
        spinner_img.anchor_y = spinner_img.height // 2
        self.init_sprite('spinner',
                         Sprite(spinner_img, x=self.window.width//2, y=self.window.height//2 + 72, batch=self.batch),
                         is_button=False)

        # Text
        self.title = Text('Generating', batch=self.batch, size=22, bold=True,
                          x=self.window.width//2, y=self.window.height//3 + 24)
        self.subtitle = Text('Hang tight!', batch=self.batch, size=14,
                             x=self.window.width//2, y=self.window.height//3 - 24)
        self.title.anchor_x = 'center'
        self.subtitle.anchor_x = 'center'

    def update(self, dt):
        """
        Make the spinner spin
        :param dt: Time elapsed since last update
        """
        self.elapsed += dt
        if self.elapsed > 0.05:  # Rotate every 50ms
            self.elapsed = 0
            sprite = self.sprites['spinner'][0]
            sprite.rotation += 30
            if sprite.rotation == 360:
                sprite.rotation = 0
