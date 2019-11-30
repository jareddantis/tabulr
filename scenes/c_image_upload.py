from .scene import Scene
from ui import Text, Button
from pyglet.window.mouse import *
from tkinter import filedialog

class ImageUploadScreen(Scene):
    def __init__(self, window, bus):
        super().__init__(window, bus)
        self.title = Text('Select', batch=self.batch, size=22,
                          x=self.margin, y=self.window.height - self.margin - 22)
        self.title_bold = Text('an image', bold=True, batch=self.batch, size=22,
                               x=self.margin + self.title.content_width + 8, y=self.window.height - self.margin - 22)

        # Image pick button
        pick_button = Button('pick-image', self.window, self.batch)
        pick_button.x = self.window.width//2 - pick_button.width//2
        pick_button.y = self.window.height//2 - pick_button.height//2
        self.init_sprite('pick_button', pick_button)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == LEFT:
            if self.sprites['pick_button'][0].hit_test(x, y):
                # Spawn file picker
                # Not working on macOS - we have no choice except to explicitly specify a path for now
                file_path = filedialog.askopenfilename(filetypes=[('Image files', '.jpg .png')])
                print(file_path)
