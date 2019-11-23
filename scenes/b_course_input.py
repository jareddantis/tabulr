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
        self.batch = pyglet.graphics.Batch()
        self.inputs = [
            # Course Title
            TextInput('', 200, 100, window.width - 210, self.batch),
            # Venue
            TextInput('', 200, 60, window.width - 210, self.batch),
            # Instructor (Optional)
            TextInput('', 200, 20, window.width - 210, self.batch)
        ]
        window.text_cursor = window.get_system_mouse_cursor('text')

        window.focus = None
        TextInput.set_focus(window, self.inputs[0])

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
        if button == LEFT:
            if self.is_clicked('next_button', x, y):
                self.bus.emit('next_scene')

    def on_mouse_motion(self, x, y, dx, dy):
        next_button = self.sprites['next_button']
        image_width = next_button.x + next_button.width
        image_height = next_button.y + next_button.height
        if image_width > x > next_button.x and image_height > y > next_button.y:
            next_button.on_mouse_enter()
        else:
            next_button.on_mouse_leave()
