import pyglet

class Button(pyglet.sprite.Sprite):
    def __init__(self, filename, window, batch, x=0, y=0):
        self.texture_default = pyglet.resource.image('btn-{}.png'.format(filename))
        self.texture_hover = pyglet.resource.image('btn-{}-hover.png'.format(filename))
        self.filename = filename
        self.window = window
        super(Button, self).__init__(self.texture_default, x, y, batch=batch)

    def on_mouse_enter(self):
        self.image = self.texture_hover
        cursor = self.window.get_system_mouse_cursor(self.window.CURSOR_HAND)
        self.window.set_mouse_cursor(cursor)

    def on_mouse_leave(self):
        self.image = self.texture_default
        cursor = self.window.get_system_mouse_cursor(self.window.CURSOR_DEFAULT)
        self.window.set_mouse_cursor(cursor)