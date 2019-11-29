from pyglet.graphics import Batch

class Scene:
    def __init__(self, window, bus):
        """
        Initialize the Scene object.
        :param window: Pyglet window object. Must be same throughout application.
        :param bus: Event bus. Used for communicating scene changes to main application thread.
        """
        self.window = window
        self.bus = bus
        self.batch = Batch()
        self.margin = 36
        self.sprites = {}
        self.inputs = []

    def init_sprite(self, name, sprite, is_button=True):
        """
        Store sprite for easy garbage collection later.
        :param name: Name of sprite
        :param sprite: pyglet.sprite.Sprite instance
        :param is_button: Whether sprite is used as a button. Used in managing hover states.
        """
        self.sprites[name] = (sprite, is_button)

    def is_clicked(self, sprite_name, mouse_x, mouse_y):
        """
        Check if a mouse click falls on a sprite.
        :param sprite_name: Name of sprite to check
        :param mouse_x: x-coordinate of mouse click
        :param mouse_y: y-coordinate of mouse click
        """
        sprite = self.sprites[sprite_name][0]
        sprite_min_x = sprite.x
        sprite_max_x = sprite_min_x + sprite.image.width
        sprite_min_y = sprite.y
        sprite_max_y = sprite_min_y + sprite.image.height
        return sprite_min_x <= mouse_x <= sprite_max_x and sprite_min_y <= mouse_y <= sprite_max_y

    def on_destroy(self):
        """
        Removes all registered sprites from video memory.
        Called just before the scene is changed.
        """
        for sprite in self.sprites.values():
            sprite[0].delete()

    def on_draw(self):
        self.batch.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        pass

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
        pass

    def on_text(self, text):
        pass

    def on_text_motion(self, motion):
        pass

    def on_text_motion_select(self, motion):
        pass

    def on_key_press(self, symbol, modifiers):
        pass

    def set_focus(self, focus):
        pass

    def update(self, dt):
        pass
