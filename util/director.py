from event_bus import EventBus
from scenes import WelcomeScreen, CourseInputScreen
from pyglet.window import Window
from util.course_mgr import CourseManager

class Director(EventBus):
    def __init__(self, window: Window):
        super().__init__()
        self.course_mgr = CourseManager(self)
        self.window = window
        self.scene = 0
        self.scenes = [
            WelcomeScreen(window, self),
            CourseInputScreen(window, self, self.course_mgr)
        ]

    @property
    def current_scene(self):
        return self.scenes[self.scene]

    def on_draw(self):
        self.current_scene.on_draw()

    def on_update(self, dt):
        self.current_scene.update(dt)

    def on_next_scene(self):
        """
        Change the scene that is currently being displayed to the next one.
        """
        if self.scene < len(self.scenes) - 1:
            self.current_scene.on_destroy()
            self.scene += 1
