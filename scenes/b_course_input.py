import pyglet
from ui import Button, Text, TextInput
from .scene import Scene
from pyglet.window.mouse import *
from pyglet.sprite import Sprite
from pyglet.resource import image

class CourseInputScreen(Scene):
    def __init__(self, window, bus):
        super().__init__(window, bus)
        self.title = Text('Input a', batch=self.batch, size=22,
                          x=self.margin, y=self.window.height - self.margin - 22)
        self.title_bold = Text('course', bold=True, batch=self.batch, size=22,
                               x=self.margin + self.title.content_width + 8, y=self.window.height - self.margin - 22)

        # Waves
        waves_img = image('side-waves.png')
        waves_img.anchor_x = waves_img.width
        waves = Sprite(waves_img, x=window.width, y=0, batch=self.batch)
        waves.opacity = 160
        self.init_sprite('waves', waves)

        # Next button
        next_button = Button('tick', self.window, self.batch, y=self.margin)
        next_button.x = self.window.width - self.margin - next_button.image.width
        self.init_sprite('next_button', next_button)

        # Add button
        add_button = Button('add-to-sched', self.window, self.batch, x=self.margin, y=self.margin)
        self.init_sprite('add_button', add_button)

        # View button
        view_button = Button('view-courses', self.window, self.batch,
                             x=(1.5*self.margin) + add_button.width, y=self.margin)
        self.init_sprite('view_button', view_button)

        # Section
        self.inputs = [
            # Course Title
            TextInput('', self.margin, 320, 200, self.batch),
            # Venue
            TextInput('', self.margin, 250, self.window.width - 210, self.batch),
            # Instructor (Optional)
            TextInput('', self.margin, 180, self.window.width - 210, self.batch)
        ]
        self.window.focus = None
        self.set_focus(self.inputs[0])

        # Section labels
        self.labels = [
            Text('Course title', size=14, x=self.margin, y=350, batch=self.batch),
            Text('Venue', size=14, x=self.margin, y=280, batch=self.batch),
            Text('Instructor (optional)', size=14, x=self.margin, y=210, batch=self.batch)
        ]

    def on_draw(self):
        super().on_draw()
        self.window.set_caption('tabulr | Input subjects')

    def on_mouse_press(self, x, y, button, modifiers):
        if self.is_clicked('next_button', x, y) and button == LEFT:
            self.bus.emit('next_scene')
        else:
            for input in self.inputs:
                if input.hit_test(x, y):
                    self.set_focus(input)
                    break
            else:
                self.set_focus(None)

            if self.window.focus:
                self.window.focus.caret.on_mouse_press(x, y, button, modifiers)

    def on_mouse_motion(self, x, y, dx, dy):
        # Change cursor on text input hover
        for input in self.inputs:
            if input.hit_test(x, y):
                self.window.set_mouse_cursor(self.window.get_system_mouse_cursor(self.window.CURSOR_TEXT))
                break
        else:

            # Change button state on hover
            for sprite in self.sprites:
                try:
                    if sprite.hit_test(x, y):
                        sprite.on_mouse_enter()
                        break
                    else:
                        sprite.on_mouse_leave()
                except Exception:
                    continue
            else:
                self.window.set_mouse_cursor(self.window.get_system_mouse_cursor(self.window.CURSOR_DEFAULT))

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.window.focus:
            self.window.focus.caret.on_mouse_drag(x, y, dx, dy, buttons, modifiers)

    def on_text(self, text):
        if self.window.focus:
            self.window.focus.caret.on_text(text)

    def on_text_motion(self, motion):
        if self.window.focus:
            self.window.focus.caret.on_text_motion(motion)

    def on_text_motion_select(self, motion):
        if self.window.focus:
            self.window.focus.caret.on_text_motion_select(motion)

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.TAB:
            if modifiers & pyglet.window.key.MOD_SHIFT:
                direction = -1
            else:
                direction = 1

            if self.window.focus in self.inputs:
                i = self.inputs.index(self.window.focus)
            else:
                i = 0
                direction = 0

            self.set_focus(self.inputs[(i + direction) % len(self.inputs)])

    def set_focus(self, focus):
        if self.window.focus:
            self.window.focus.caret.visible = False
            self.window.focus.caret.mark = self.window.focus.caret.position = 0

        self.window.focus = focus
        if self.window.focus:
            self.window.focus.caret.visible = True
            self.window.focus.caret.mark = 0
            self.window.focus.caret.position = len(self.window.focus.document.text)
