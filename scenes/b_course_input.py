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

        # Waves background
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

        # Text inputs
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

        # Text input labels and status messages
        self.labels = [
            Text('Course title', size=14, x=self.margin, y=350, batch=self.batch),
            Text('Section', size=14, x=self.margin + 250, y=350, batch=self.batch),
            Text('Venue', size=14, x=self.margin, y=280, batch=self.batch),
            Text('Instructor (optional)', size=14, x=self.margin, y=210, batch=self.batch),
            Text('', size=12, x=add_button.x + add_button.width + self.margin,
                 y=self.margin + add_button.height//2 - 4, batch=self.batch),
            Text('', size=12, bold=True, x=self.margin, y=self.margin*2 + add_button.height, batch=self.batch)
        ]

        # Error message properties
        self.error_elapsed = 0
        self.error_opacity = 0

        # Course manager instance
        self.manager = manager
        self.manager.set_close_handler(self.on_viewer_closed)

    def on_viewer_closed(self, proceed=False):
        if proceed:
            # All courses confirmed, go to next scene
            self.bus.emit('next_scene')
        else:
            # User only deleted a course or something
            self.update_count()

    def update_count(self):
        """
        Update on-screen course count.
        :return:
        """
        num_courses = self.manager.num_courses
        if num_courses > 0:
            self.labels[4].text = '{} course{} added'.format(num_courses, 's' if num_courses != 1 else '')
        else:
            self.labels[4].text = ''

    def on_draw(self):
        super().on_draw()
        self.window.set_caption('tabulr | Input subjects')

    def on_mouse_press(self, x, y, button, modifiers):
        if self.sprites['next_button'][0].hit_test(x, y) and button == LEFT:
            # Check if we can go to the next scene
            if self.manager.num_courses > 0:
                # At least one course was specified, go ahead
                self.hide_error_message()
                self.manager.view_courses()
            else:
                # No courses specified
                self.set_error_message('Please add at least one course first.')
        elif self.sprites['add_button'][0].hit_test(x, y) and button == LEFT:
            # Get course details
            title = self.inputs[0].content
            section = self.inputs[1].content
            venue = self.inputs[2].content
            instructor = self.inputs[3].content

            # Make sure title and venue are not empty
            if len(title) and len(section) and len(venue):
                self.hide_error_message()
                self.manager.add_course(title, section, venue, instructor)

                # Update course count
                self.update_count()

                # Put focus back on first text input
                self.set_focus(self.inputs[0])

                # Empty text inputs
                for text_field in self.inputs:
                    text_field.content = ''
            else:
                self.set_error_message('Title, section, and venue cannot be empty.')
        else:
            for text_field in self.inputs:
                if text_field.hit_test(x, y):
                    self.set_focus(text_field)
                    text_field.caret.on_mouse_press(x, y, button, modifiers)
                    return
            else:
                self.set_focus(None)

    def on_key_press(self, symbol, modifiers):
        """
        Allows focusing text inputs through Tab and Shift+Tab.
        :param symbol: Keyboard symbol
        :param modifiers: Keyboard modifier keys
        :return:
        """
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

    def hide_error_message(self):
        """
        Hides the error message.
        """
        self.labels[5].color = (0, 0, 0, 0)
        self.error_opacity = 0

    def set_error_message(self, msg):
        """
        Displays a red error message.
        :param msg: Error message
        """
        self.labels[5].text = msg
        self.labels[5].color = (236, 64, 122, 255)
        self.error_elapsed = 0
        self.error_opacity = 255

    def update(self, dt):
        """
        Fades out the error message after 1.5 seconds of initial visibility.
        :param dt: Time elapsed since last update
        """
        if self.error_opacity > 0:
            self.error_elapsed += dt
            if self.error_elapsed > 1.5:
                self.labels[5].color = (236, 64, 122, self.error_opacity)
                self.error_opacity -= 10
        else:
            self.hide_error_message()
