from .scene import Scene
from ui import Text, Button, TextInput
from pyglet.window.mouse import *
from os import path
from PIL import Image
from util.image_vwr import ImageViewer
import imghdr

class ImageUploadScreen(Scene):
    def __init__(self, window, bus, manager):
        super().__init__(window, bus, draw_waves=True, title='Select a background image')
        self.manager = manager
        self.title = Text('Select a', batch=self.batch, size=22,
                          x=self.margin, y=self.window.height - self.margin - 22)
        self.title_bold = Text('background image', bold=True, batch=self.batch, size=22,
                               x=self.margin + self.title.content_width + 8, y=self.window.height - self.margin - 22)

        # Instructions
        self.subtitle = Text('Enter the path to a valid JPG or PNG image below.',
                             x=self.margin, y=self.window.height*2//3, size=12, batch=self.batch)

        # Text input
        input_width = 400
        self.path_input = TextInput('', self.margin, self.subtitle.y - 60, input_width, self.batch)
        self.set_focus(self.path_input)

        # Error text
        self.error_msg.y = self.path_input.layout.y - 50

        # Image pick button
        pick_button = Button('pick-image', self.window, self.batch, x=self.margin, y=self.margin)
        self.init_sprite('pick_button', pick_button)

        # ImageViewer
        self.image_viewer = None

    def check_file(self, file_path):
        # Check if path is not empty
        if len(file_path) == 0:
            return 'Path cannot be empty'

        # Check if file exists
        if not path.isfile(file_path):
            return 'File at specified path does not exist'

        # Check if file is JPG or PNG
        if not imghdr.what(file_path) in ['jpeg', 'png']:
            return 'Please use a JPEG or PNG file'

        # Check if file is valid
        try:
            test_image = Image.open(file_path)
            test_image.verify()
            test_image.close()
        except:
            return 'Image file is invalid or corrupted'

        return 'ok'

    def on_mouse_press(self, x, y, button, modifiers):
        if button == LEFT:
            if self.sprites['pick_button'][0].hit_test(x, y):
                # Get path
                file_path = self.path_input.content.rstrip()
                result = self.check_file(file_path)

                if result == 'ok':
                    self.manager.image_path = file_path
                    self.image_viewer = ImageViewer(file_path, self.window, self.on_viewer_closed)
                else:
                    self.set_error_message(result)
            elif self.path_input.hit_test(x, y):
                self.set_focus(self.path_input)
                self.path_input.caret.on_mouse_press(x, y, button, modifiers)

    def on_viewer_closed(self, proceed):
        if proceed:
            self.bus.emit('next_scene')
