from event_bus import EventBus
from scenes import *
from pyglet.window import Window
from .course_mgr import CourseManager

class Director(EventBus):
    def __init__(self, window):
        super().__init__()
        self.course_mgr = CourseManager(window)
        self.window = window  # type: Window
        self.scene = 0
        self.scenes = [
            WelcomeScreen(window, self),
            CourseInputScreen(window, self, self.course_mgr),
            ImageUploadScreen(window, self),
        ]

        # List of event handlers to add to window per scene
        self.__handler_names = [
            'on_key_press',
            'on_mouse_press',
            'on_mouse_motion',
            'on_mouse_drag',
            'on_text',
            'on_text_motion',
            'on_text_motion_select'
        ]
        self.__added_handlers = []
        self.__add_event_handlers()

    @property
    def __current_scene(self):
        return self.scenes[self.scene]

    def __add_event_handlers(self):
        # Add all event handlers from scene
        for listener_name in self.__handler_names:
            if listener_name in dir(self.__current_scene):
                listener = getattr(self.__current_scene, listener_name)
                if callable(listener):
                    self.__added_handlers.append(listener)
                    self.window.push_handlers(listener)

    def __remove_event_handlers(self):
        # Remove all added event handlers from scene
        while self.__added_handlers:
            self.window.remove_handlers(self.__added_handlers.pop())

    def on_draw(self):
        self.__current_scene.on_draw()

    def on_update(self, dt):
        self.__current_scene.update(dt)

    def on_next_scene(self):
        """
        Change the scene that is currently being displayed to the next one.
        """
        if self.scene < len(self.scenes) - 1:
            # Allow scene to do cleanup
            self.__current_scene.on_destroy()

            # Remove all event handlers
            self.__remove_event_handlers()

            # Increment scene and add new event handlers
            self.scene += 1
            self.__add_event_handlers()
