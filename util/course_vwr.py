from pyglet.window import Window, mouse
from pyglet import gl
from pyglet.graphics import Batch, draw
from pyglet.sprite import Sprite
from pyglet.resource import image
from ui import Text, Button
from itertools import islice

class CourseViewer(Window):
    def __init__(self, parent_window, course_data, on_close):
        # Create window
        super().__init__(caption='Confirm courses', style=Window.WINDOW_STYLE_TOOL)
        self.switch_to()
        self.closed = False
        self.on_close_callback = on_close
        self.batch = Batch()
        self.parent_window = parent_window

        # Window background
        gl.glClearColor(43 / 255, 65 / 255, 98 / 255, 1)
        waves = Sprite(image('front-waves.png'), x=0, y=0, batch=self.batch)
        waves.opacity = 160

        # The courses entered so far will be stored in self.course_data.
        # This is a dict, where each key is the course section
        # and the value is a tuple of the format (<title>, <venue>, <instructor>).
        self.course_data = course_data

        # UI text
        self.margin = 36
        self.x_coords = [100, 250, 370, 480]  # section, title, venue, instructor
        self.heading_y = self.height - 90
        self.labels = [
            Text('Confirm your', x=self.margin, y=self.height - self.margin - 12, size=20, batch=self.batch),
            Text('courses', x=self.margin + 170, y=self.height - self.margin - 12, size=20, bold=True, batch=self.batch),
            Text('Section', x=100, y=self.heading_y, size=12, bold=True, batch=self.batch),
            Text('Title', x=250, y=self.heading_y, size=12, bold=True, batch=self.batch),
            Text('Venue', x=370, y=self.heading_y, size=12, bold=True, batch=self.batch),
            Text('Instructor', x=480, y=self.heading_y, size=12, bold=True, batch=self.batch),
            Text('Page 1 of 1', x=self.margin * 4, y=self.margin + 8, size=10, batch=self.batch)
        ]

        # Next button
        next_button = Button('next', self, self.batch, y=self.margin)
        next_button.x = self.width - next_button.image.width - 24
        next_button.scale = 0.8
        self.ui_buttons = [next_button]

        # Table pagination
        self.page = 0
        self.pages = []
        self.paginate()
        self.ui_buttons.extend([
            Button('left', self, self.batch, x=self.margin, y=self.margin),
            Button('right', self, self.batch, x=self.margin * 2, y=self.margin),
        ])

        # Rows
        self.delete_buttons = []
        self.course_rows = []
        self.generate_rows()

    def on_draw(self):
        self.clear()

        # Line separators
        top_y = self.labels[0].y - 16
        bottom_y = self.ui_buttons[0].y + self.ui_buttons[0].height + 16
        draw(2, gl.GL_LINES, ('v2i', (self.margin, top_y,
                                      self.width - self.margin, top_y)))
        draw(2, gl.GL_LINES, ('v2i', (self.margin, bottom_y,
                                      self.width - self.margin, bottom_y)))

        # On-screen text and buttons
        self.batch.draw()

    def on_close(self, proceed=False):
        self.on_close_callback(proceed)
        self.closed = True
        self.close()
        self.parent_window.switch_to()
        self.parent_window.activate()

    def on_mouse_motion(self, x, y, dx, dy):
        for button_list in (self.ui_buttons, self.delete_buttons):
            for button in button_list:
                if button.hit_test(x, y):
                    button.on_mouse_enter()
                    return
                else:
                    button.on_mouse_leave()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            if self.ui_buttons[0].hit_test(x, y):
                # Proceed to next scene
                self.on_close(True)
            elif self.ui_buttons[1].hit_test(x, y):
                # Previous page
                if self.page > 0:
                    self.page -= 1
                    self.regenerate_rows()
            elif self.ui_buttons[2].hit_test(x, y):
                # Next page
                if self.page < len(self.pages) - 1:
                    self.page += 1
                    self.regenerate_rows()
            else:
                for i in range(len(self.delete_buttons)):
                    button = self.delete_buttons[i]
                    if button.hit_test(x, y):
                        button.on_mouse_leave()

                        # Remove course
                        course_section = self.course_rows[i][0].text
                        del self.course_data[course_section]

                        # Regenerate on-screen table
                        self.page = 0
                        self.regenerate_rows()
                        break

    def generate_rows(self):
        self.course_rows = []
        self.delete_buttons = []

        def truncate_text(text, max_len=10):
            if len(text) <= max_len:
                return text
            return text[:max_len] + '...'

        base_y = self.labels[5].y - self.labels[5].content_height - 12
        course_data = self.pages[self.page]
        for course_section, course_details in course_data.items():
            # Course details
            course_name, course_venue, course_instructor = course_details
            course_row = [
                Text(truncate_text(course_section, 15), x=self.x_coords[0], y=base_y, size=12, batch=self.batch),
                Text(truncate_text(course_name), x=self.x_coords[1], y=base_y, size=12, batch=self.batch),
                Text(truncate_text(course_venue), x=self.x_coords[2], y=base_y, size=12, batch=self.batch),
                Text(truncate_text(course_instructor, 15), x=self.x_coords[3], y=base_y, size=12, batch=self.batch),
            ]
            self.course_rows.append(course_row)

            # Delete course button
            self.delete_buttons.append(Button('delete', self, self.batch, x=self.margin, y=base_y - 6))

            # Render next row at lower y
            base_y -= course_row[0].content_height + 16

    def regenerate_rows(self):
        # Delete on-screen rows
        for row in self.course_rows:
            for label in row:
                label.delete()
        for button in self.delete_buttons:
            button.delete()

        # Check if there is anything to render
        if len(self.course_data) > 0:
            self.paginate()
            self.generate_rows()
        else:
            self.on_close()

    def paginate(self):
        """
        Split courses into chunks for easy navigation.
        """
        def chunks(data, size=8):
            # Split dict into list of dicts of specified size
            # https://stackoverflow.com/a/22878842
            it = iter(data)
            for i in range(0, len(data), size):
                yield {k: data[k] for k in islice(it, size)}

        self.pages = []
        for page in chunks(self.course_data):
            self.pages.append(page)

        # Update total page count
        self.update_page_count()

    def update_page_count(self):
        self.labels[6].text = 'Page {} of {}'.format(self.page + 1, len(self.pages))

    def switch_to(self):
        super().switch_to()
        self.activate()
