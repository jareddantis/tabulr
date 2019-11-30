from ui import Button, Text, TextInput
from .scene import Scene
from pyglet.window import key
from pyglet.window.mouse import *
from pyglet.sprite import Sprite
from pyglet.resource import image

class CourseInputScreen(Scene):
    def __init__(self, window, bus, manager):
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
        self.init_sprite('waves', waves, is_button=False)

        # Next button
        next_button = Button('next', self.window, self.batch, y=self.margin)
        next_button.x = self.window.width - self.margin - next_button.image.width
        self.init_sprite('next_button', next_button)

        # Add button
        add_button = Button('add-course', self.window, self.batch, x=self.margin, y=self.margin)
        self.init_sprite('add_button', add_button)

        # Section
        self.inputs = [
            # Course Title
            TextInput('', self.margin, 320, 200, self.batch),
            # Section
            TextInput('', self.margin + 250, 320, 100, self.batch),
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
            Text('Section', size=14, x=self.margin + 250, y=350, batch=self.batch),
            Text('Venue', size=14, x=self.margin, y=280, batch=self.batch),
            Text('Instructor (optional)', size=14, x=self.margin, y=210, batch=self.batch),
            Text('', size=12, x=add_button.x + add_button.width + self.margin,
                 y=self.margin + add_button.height//2 - 4, batch=self.batch)
        ]

        # Course manager instance
        self.manager = manager

    def on_draw(self):
        super().on_draw()
        self.window.set_caption('tabulr | Input subjects')

    def on_mouse_press(self, x, y, button, modifiers):
        if self.is_clicked('next_button', x, y) and button == LEFT:
            self.manager.view_courses()
        elif self.is_clicked('add_button', x, y) and button == LEFT:
            # Get course details
            title = self.inputs[0].content
            section = self.inputs[1].content
            venue = self.inputs[2].content
            instructor = self.inputs[3].content

            # Make sure title and venue are not empty
            if len(title) and len(section) and len(venue):
                self.manager.add_course(title, section, venue, instructor)

                # Update course count
                num_courses = self.manager.num_courses
                self.labels[4].text = '{} course{} added'.format(num_courses, 's' if num_courses != 1 else '')

                # Put focus back on first text input
                self.set_focus(self.inputs[0])

                # Empty text inputs
                for text_field in self.inputs:
                    text_field.content = ''
            else:
                print('Either title, section, or venue were left empty')
        else:
            for text_field in self.inputs:
                if text_field.hit_test(x, y):
                    self.set_focus(text_field)
                    text_field.caret.on_mouse_press(x, y, button, modifiers)
                    return
            else:
                self.set_focus(None)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.TAB:
            if modifiers & key.MOD_SHIFT:
                direction = -1
            else:
                direction = 1

            if self.window.focus in self.inputs:
                i = self.inputs.index(self.window.focus)
            else:
                i = 0
                direction = 0

            self.set_focus(self.inputs[(i + direction) % len(self.inputs)])
