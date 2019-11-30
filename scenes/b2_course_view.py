from pyglet.window import Window
from pyglet import gl, graphics
from util.scene import Scene
from ui import Text

class CourseViewer(Scene):
    def __init__(self, parent_window, bus, course_data):
        def on_draw():
            self.window.clear()
            self.batch.draw()

        def on_close():
            self.closed = True
            self.window.close()
            self.parent_window.switch_to()
            self.parent_window.activate()

        # Create window
        self.closed = False
        self.batch = graphics.Batch()
        self.bus = bus
        self.parent_window = parent_window
        self.window = Window(caption='View courses', style=Window.WINDOW_STYLE_TOOL)
        self.window.on_draw = on_draw
        self.window.on_close = on_close
        self.window.switch_to()
        gl.glClearColor(43 / 255, 65 / 255, 98 / 255, 1)
        super().__init__(self.window, bus)

        # The courses inputted so far is stored in self.course_data.
        # This is a dict, where each key is the course name
        # and the value is a tuple of the format (<venue>, <instructor>).
        self.course_data = course_data

        # UI text
        self.labels = [
            Text('View subjects', x=self.margin, y=self.window.height - self.margin, size=14, batch=self.batch),
            Text(str(self.course_data.items()), x=self.margin, y=self.margin, size=10, batch=self.batch)
        ]

    @property
    def is_viewing(self):
        return self.window.visible

    def switch_to(self):
        self.window.activate()
