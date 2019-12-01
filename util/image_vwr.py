from .popup import Popup
from ui import Text, Button
from pyglet.image import load
from pyglet.sprite import Sprite
from pyglet.graphics import OrderedGroup
from pyglet.window import mouse
from pyglet import gl

class ImageViewer(Popup):
    def __init__(self, file_path, parent_window, on_close):
        super().__init__(parent_window, on_close, caption='tabulr | Confirm background image',
                         width=640, height=640)

        # Layer groups
        bg = OrderedGroup(0)
        fg = OrderedGroup(1)

        # Compute image sprite size, preserving aspect ratio
        bg_image = load(file_path)
        bg_image.anchor_x = bg_image.width//2
        bg_image.anchor_y = bg_image.height//2
        if bg_image.height > bg_image.width:
            scale = 640 / bg_image.height
        else:
            scale = 640 / bg_image.width

        # Background gradient
        gl.glEnable(gl.GL_BLEND)
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
        self.bg_gradient = self.batch.add(4, gl.GL_QUADS, fg,
                                          ('v2i', (0, 0, 640, 0, 640, 80, 0, 80)),
                                          ('c4B', (0, 0, 0, 255, 0, 0, 0, 255,
                                                   0, 0, 0, 0, 0, 0, 0, 0)))

        # Draw bg image
        self.bg_sprite = Sprite(bg_image, batch=self.batch, group=bg, x=320, y=320)
        self.bg_sprite.scale = scale

        # Confirmation text
        self.confirm_text = Text('Is this the image you want to use?', group=fg,
                                 size=12, x=self.margin, y=self.margin, bold=True, batch=self.batch)

        # Confirmation buttons
        self.buttons = [
            Button('yes', self, self.batch, x=590, y=30, group=fg),
            Button('no', self, self.batch, x=550, y=30, group=fg)
        ]

    def on_mouse_motion(self, x, y, dx, dy):
        for button in self.buttons:
            if button.hit_test(x, y):
                button.on_mouse_enter()
                return
            else:
                button.on_mouse_leave()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            if self.buttons[0].hit_test(x, y):
                # Proceed to next scene
                self.on_close(True)
            elif self.buttons[1].hit_test(x, y):
                # Pick image again
                self.on_close(False)