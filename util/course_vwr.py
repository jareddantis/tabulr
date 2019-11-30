from pyglet.window import Window
from pyglet.gl import *
from pyglet.graphics import Batch
from ui import Text

class CourseViewer(Window):
    def __init__(self, parent_window, course_data):
        # Create window
        super().__init__(caption='View courses', style=Window.WINDOW_STYLE_TOOL)
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
        margin=36
        self.labels = [
            Text('View', x=margin, y=self.height - margin, size=14, batch=self.batch),
            Text('courses', x=margin + 50, y=self.height - margin, size=14, bold=True, batch=self.batch),
            Text(str(self.course_data.items()), x=margin, y=margin, size=10, batch=self.batch)
        ]

    def on_draw(self):
        self.clear()
        self.batch.draw()

    def on_close(self):
        self.closed = True
        self.close()
        self.parent_window.switch_to()
        self.parent_window.activate()

    def switch_to(self):
        super().switch_to()
        self.activate()
