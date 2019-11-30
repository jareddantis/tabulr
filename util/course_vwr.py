from pyglet.window import Window
from pyglet.gl import *
from pyglet.graphics import Batch
from ui import Text, Button

class CourseViewer(Window):
    def __init__(self, parent_window, course_data):
        # Create window
        super().__init__(caption='Confirm courses', style=Window.WINDOW_STYLE_TOOL)
        self.switch_to()
        self.closed = False
        self.batch = Batch()
        self.parent_window = parent_window
        glClearColor(43 / 255, 65 / 255, 98 / 255, 1)

        # The courses inputted so far will be stored in self.course_data.
        # This is a dict, where each key is the course name
        # and the value is a tuple of the format (<venue>, <instructor>).
        self.course_data = course_data

        # UI text
        self.margin = 36
        self.x_coords = [100, 250, 370, 480] # section, title, venue, instructor
        self.heading_y = self.height - 100
        self.labels = [
            Text('Confirm your', x=self.margin, y=self.height - self.margin - 12, size=20, batch=self.batch),
            Text('courses', x=self.margin + 170, y=self.height - self.margin - 12, size=20, bold=True, batch=self.batch),
            Text('Section', x=100, y=self.heading_y, size=12, bold=True, batch=self.batch),
            Text('Title', x=250, y=self.heading_y, size=12, bold=True, batch=self.batch),
            Text('Venue', x=370, y=self.heading_y, size=12, bold=True, batch=self.batch),
            Text('Instructor', x=480, y=self.heading_y, size=12, bold=True, batch=self.batch),
        ]

        # Rows
        self.delete_buttons = []
        self.course_rows = []
        self.generate_rows()

    def on_draw(self):
        self.clear()
        self.batch.draw()

    def on_close(self):
        self.closed = True
        self.close()
        self.parent_window.switch_to()
        self.parent_window.activate()

    def generate_rows(self):
        base_y = self.labels[5].y - self.labels[5].content_height - 8
        for course_name, course_details in self.course_data.items():
            # Course details
            course_section, course_venue, course_instructor = course_details
            course_row = [
                Text(course_section, x=self.x_coords[0], y=base_y, size=12, batch=self.batch),
                Text(course_name, x=self.x_coords[1], y=base_y, size=12, batch=self.batch),
                Text(course_venue, x=self.x_coords[2], y=base_y, size=12, batch=self.batch),
                Text(course_instructor, x=self.x_coords[3], y=base_y, size=12, batch=self.batch),
            ]
            self.course_rows.append(course_row)

            # Delete course button
            self.delete_buttons.append(Button('delete', self, self.batch, x=self.margin, y=base_y - 6))

            # Render next row at lower y
            base_y -= course_row[0].content_height + 16

    def switch_to(self):
        super().switch_to()
        self.activate()
