import pyglet
from ui import Button, Text, TextInput
from .scene import Scene
from pyglet.window.mouse import *

class CourseInputScreen(Scene):
    def __init__(self, window, bus):
        super().__init__(window, bus)
        self.title = Text('Input your', batch=self.batch, size=22,
                          x=self.margin, y=self.window.height - self.margin - 22)
        self.title_bold = Text('courses', bold=True, batch=self.batch, size=22,
                               x=self.margin + self.title.content_width + 8, y=self.window.height - self.margin - 22)

        # Next button
        next_button = Button('next', self.window, self.batch, y=self.margin)
        next_button.x = self.window.width - self.margin - next_button.image.width
        self.init_sprite('next_button', next_button)

        # Section
        self.inputs = [
            # Course Title
            TextInput('', 200, 100, self.window.width - 210, self.batch),
            # Venue
            TextInput('', 200, 60, self.window.width - 210, self.batch),
            # Instructor (Optional)
            TextInput('', 200, 20, self.window.width - 210, self.batch)
        ]
        self.window.focus = None
        self.set_focus(self.inputs[0])

        # Add to Schedule button: uncomment when btn-view & text field exists already
        # add_button = Button('view', self.window, self.batch)
        # add_button.x = instructor_field.x
        # add_button.y = self.window.height - self.margin - next_button.image.width
        # self.init_sprite('view_button', view_button)

        # View or Edit Courselist button: uncomment when btn-view exists already
        # view_button = Button('view', self.window, self.batch)
        # view_button.x = add_button.x
        # view_button.y = add_button.y + (self.margin + 25)
        # self.init_sprite('view_button', view_button)

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
        # Change button state on hover
        next_button = self.sprites['next_button']
        image_width = next_button.x + next_button.width
        image_height = next_button.y + next_button.height
        if image_width > x > next_button.x and image_height > y > next_button.y:
            next_button.on_mouse_enter()
        else:
            next_button.on_mouse_leave()

        # Change cursor on text input hover
        for input in self.inputs:
            if input.hit_test(x, y):
                self.window.set_mouse_cursor(self.window.get_system_mouse_cursor(self.window.CURSOR_TEXT))
                break
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
