import pyglet

class Button(pyglet.sprite.Sprite):
    def __init__(self, filename, window, batch, x=0, y=0):
        """
        Initialize the Button object.
        :param filename: Name of button image. For example, if we pass `tick` to this argument,
                         the application will look for the files `btn-tick.png` and `btn-tick-hover.png`
                         in the `res/` folder.
        :param window: Pyglet window object. Must be same throughout application.
        :param batch: Pyglet graphics batch. Must be the same throughout parent scene.
        :param x: x-coordinate of button position
        :param y: y-coordinate of button position
        """
        self.texture_default = pyglet.resource.image('btn-{}.png'.format(filename))
        self.texture_hover = pyglet.resource.image('btn-{}-hover.png'.format(filename))
        self.window = window
        super().__init__(self.texture_default, x=x, y=y, batch=batch)

    def hit_test(self, x, y):
        image_width = self.x + self.width
        image_height = self.y + self.height
        return image_width > x > self.x and image_height > y > self.y

    def on_mouse_enter(self):
        """
        Called when the mouse moves over the button.
        Causes the button to switch to its hover state.
        """
        self.image = self.texture_hover
        cursor = self.window.get_system_mouse_cursor(self.window.CURSOR_HAND)
        self.window.set_mouse_cursor(cursor)

    def on_mouse_leave(self):
        """
        Called when the mouse moves away from the button.
        Causes the button to revert to its normal state.
        """
        self.image = self.texture_default
        cursor = self.window.get_system_mouse_cursor(self.window.CURSOR_DEFAULT)
        self.window.set_mouse_cursor(cursor)
