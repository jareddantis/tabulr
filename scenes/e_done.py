from .scene import Scene
from pyglet.resource import image
from pyglet.sprite import Sprite
from ui import Text

class DoneScreen(Scene):
    def __init__(self, window, bus):
        super().__init__(window, bus, draw_waves=True, title='Generating')

        self.title = Text('Done', batch=self.batch)