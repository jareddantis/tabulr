from pyglet.graphics import Batch
from ui import TextInput
from pyglet.sprite import Sprite
from pyglet.resource import image

class Scene:
    def __init__(self, window, bus, title='Welcome to tabulr', draw_waves=False):
        """
        Initialize the Scene object.
        :param window: Pyglet window object. Must be same throughout application.
        :param bus: Event bus. Used for communicating scene changes to main application thread.
        """
        self.window = window
        self.window_title = title
        self.bus = bus
        self.batch = Batch()
        self.margin = 36
        self.sprites = {}
        self.inputs = []

        # Waves background
        if draw_waves:
            waves_img = image('side-waves.png')
            waves_img.anchor_x = waves_img.width
            waves = Sprite(waves_img, x=window.width, y=0, batch=self.batch)
            waves.opacity = 160
            self.init_sprite('waves', waves, is_button=False)

    def init_sprite(self, name, sprite, is_button=True):
        """
        Store sprite for easy garbage collection later.
        :param name: Name of sprite
        :param sprite: pyglet.sprite.Sprite instance
        :param is_button: Whether sprite is used as a button. Used in managing hover states.
        """
        self.sprites[name] = (sprite, is_button)

    def on_destroy(self):
        """
        Removes all registered sprites from video memory.
        Called just before the scene is changed.
        """
        for sprite in self.sprites.values():
            sprite[0].delete()

    def on_draw(self):
        """
        Draws all objects that are part of this scene's render batch.
        """
        self.batch.draw()

        # Window title
        self.window.set_caption(self.window_title)

    def on_mouse_motion(self, x, y, dx, dy):
        for text_field in self.inputs:
            # Change cursor into caret on text input hover
            if text_field.hit_test(x, y):
                self.window.set_mouse_cursor(self.window.get_system_mouse_cursor(self.window.CURSOR_TEXT))
                break
        else:
            # Change button hover state on hover
            for sprite, is_button in self.sprites.values():
                if is_button:
                    if sprite.hit_test(x, y):
                        sprite.on_mouse_enter()
                        break
                    else:
                        sprite.on_mouse_leave()
            else:
                self.window.set_mouse_cursor(self.window.get_system_mouse_cursor(self.window.CURSOR_DEFAULT))

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if isinstance(self.window.focus, TextInput):
            self.window.focus.caret.on_mouse_drag(x, y, dx, dy, buttons, modifiers)

    def on_text(self, text):
        if isinstance(self.window.focus, TextInput):
            self.window.focus.caret.on_text(text)

    def on_text_motion(self, motion):
        if isinstance(self.window.focus, TextInput):
            self.window.focus.caret.on_text_motion(motion)

    def on_text_motion_select(self, motion):
        if isinstance(self.window.focus, TextInput):
            self.window.focus.caret.on_text_motion_select(motion)

    def set_focus(self, focus):
        if isinstance(self.window.focus, TextInput):
            self.window.focus.caret.visible = False
            self.window.focus.caret.mark = self.window.focus.caret.position = 0

        self.window.focus = focus
        if isinstance(focus, TextInput):
            self.window.focus.caret.visible = True
            self.window.focus.caret.mark = 0
            self.window.focus.caret.position = len(self.window.focus.document.text)

    def update(self, dt):
        pass
