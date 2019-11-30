from .scene import Scene
from ui import Text

class ImageUploadScreen(Scene):
    def __init__(self, window, bus):
        super().__init__(window, bus)
        self.title = Text('Select', batch=self.batch, size=22,
                          x=self.margin, y=self.window.height - self.margin - 22)
        self.title_bold = Text('an image', bold=True, batch=self.batch, size=22,
                               x=self.margin + self.title.content_width + 8, y=self.window.height - self.margin - 22)