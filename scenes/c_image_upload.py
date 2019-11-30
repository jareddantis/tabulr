from .scene import Scene
from ui import Text, Button
from pyglet.window.mouse import *
from tkinter import Tk, filedialog

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

        # Tkinter instance for dialog
        self.__tkinter = None

    def on_pick_file(self):
        self.__tkinter = Tk()
        self.__tkinter.withdraw()
        file_path = filedialog.askopenfilename(filetypes=[('Image files', '.jpg .png')])
        print(file_path)
        self.__tkinter.destroy()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == LEFT:
            if self.is_clicked('pick_button', x, y):
                # Spawn file picker
                self.on_pick_file()
