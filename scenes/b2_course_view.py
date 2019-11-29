from pyglet.window import Window
from pyglet import gl
from util.scene import Scene
from ui import Text

class CourseViewer(Scene):
    def __init__(self, bus, course_data):
        def on_draw():
            self.window.clear()

            for label in self.labels:
                label.draw()

        # Create window
        self.bus = bus
        self.window = Window(caption='View courses', style=Window.WINDOW_STYLE_TOOL)
        self.window.on_draw = on_draw
        gl.glClearColor(43 / 255, 65 / 255, 98 / 255, 1)
        super().__init__(self.window, bus)

        # The courses inputted so far is stored in self.course_data.
        # This is a dict, where each key is the course name
        # and the value is a tuple of the format (<venue>, <instructor>).
        self.course_data = course_data

        # UI text
        self.labels = [
            Text('View subjects', x=self.margin, y=self.window.height - self.margin, size=14),
            Text(str(self.course_data.items()), x=self.margin, y=self.margin, size=10)
        ]