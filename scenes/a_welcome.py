from ui import Button, Text
from .scene import Scene

class WelcomeScreen(Scene):
    def __init__(self, window, batch):
        super().__init__(window, batch)
        window.set_caption('Welcome to tabulr')
        self.title = Text('Welcome to', batch=self.batch,
                          x=self.margin_left, y=(self.window.height//2) + 100)
        self.title_bold = Text('tabulr', bold=True, batch=self.batch,
                               x=self.margin_left, y=(self.window.height//2) + 60)
        self.init_sprite('next_button', Button('next', self.window, self.batch,
                                               x=self.margin_left, y=(self.window.height//2) - 100))

    def update(self, dt):
        self.sprites['next_button'].update(dt)

    def on_mouse_motion(self, x, y, dx, dy):
        next_button = self.sprites['next_button']
        image_width = next_button.x + next_button.width
        image_height = next_button.y + next_button.height
        if image_width > x > next_button.x and image_height > y > next_button.y:
            next_button.on_mouse_enter()
        else:
            next_button.on_mouse_leave()
