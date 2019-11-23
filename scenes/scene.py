from pyglet.graphics import Batch

class Scene:
    def __init__(self, window, bus):
        '''
        Initialize the Scene object.
        :param window: Pyglet window object. Must be same throughout application.
        :param bus: Event bus. Used for communicating scene changes to main application thread.
        '''
        self.window = window
        self.bus = bus
        self.batch = Batch()
        self.margin = 36
        self.sprites = {}

    def init_sprite(self, name, sprite):
        '''
        Store sprite for easy garbage collection later.
        :param name: Name of sprite
        :param sprite: pyglet.sprite.Sprite instance
        '''
        self.sprites[name] = sprite

    def is_clicked(self, sprite_name, mouse_x, mouse_y):
        '''
        Check if a mouse click falls on a sprite.
        :param sprite_name: Name of sprite to check
        :param mouse_x: x-coordinate of mouse click
        :param mouse_y: y-coordinate of mouse click
        '''
        sprite_min_x = self.sprites[sprite_name].x
        sprite_max_x = sprite_min_x + self.sprites[sprite_name].image.width
        sprite_min_y = self.sprites[sprite_name].y
        sprite_max_y = sprite_min_y + self.sprites[sprite_name].image.height
        return sprite_min_x <= mouse_x <= sprite_max_x and sprite_min_y <= mouse_y <= sprite_max_y

    def on_destroy(self):
        '''
        Removes all registered sprites from video memory.
        Called just before the scene is changed.
        '''
        for sprite in self.sprites.values():
            sprite.delete()

    def on_draw(self):
        self.batch.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def update(self, dt):
        pass
