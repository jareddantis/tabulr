from event_bus import EventBus
from scenes import *
from .course_mgr import CourseManager

class Director(EventBus):
    def __init__(self, window):
        super().__init__()
        self.course_mgr = CourseManager(window)
        self.window = window

        # Available scenes
        self.scene = 4
        self.__init_scenes()

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
        """
        Adds all event handlers from the current scene to Pyglet's handler stack.
        This is an alternative to using the @window.event decorator,
        since we cannot use that in this context.
        A caveat of this is that we have to explicitly register and unregister
        event handlers every time we switch scenes, but that's much better than registering
        all handlers at once and forgetting about them afterward.
        """
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

    def __init_scenes(self):
        self.scenes = [
            WelcomeScreen(self.window, self),
            CourseInputScreen(self.window, self, self.course_mgr),
            ImageUploadScreen(self.window, self, self.course_mgr),
            GeneratorScreen(self.window, self, self.course_mgr),
            DoneScreen(self.window, self)
        ]

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

    def on_reset(self):
        """
        Starts the application over.
        :return:
        """
        self.__current_scene.on_destroy()
        self.__remove_event_handlers()
        self.scene = 0
        self.course_mgr.reset()
        self.__init_scenes()
        self.__add_event_handlers()
