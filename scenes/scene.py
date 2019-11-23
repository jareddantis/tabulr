from pyglet.graphics import Batch

class Scene:
    def __init__(self, window, bus):
        self.window = window
        self.bus = bus
        self.batch = Batch()
        self.margin = 36
        self.sprites = {}

    def init_sprite(self, name, sprite):
        self.sprites[name] = sprite

    def is_clicked(self, sprite_name, mouse_x, mouse_y):
        sprite_min_x = self.sprites[sprite_name].x
        sprite_max_x = sprite_min_x + self.sprites[sprite_name].image.width
        sprite_min_y = self.sprites[sprite_name].y
        sprite_max_y = sprite_min_y + self.sprites[sprite_name].image.height
        return sprite_min_x <= mouse_x <= sprite_max_x and sprite_min_y <= mouse_y <= sprite_max_y

    '''
    pyglet methods
    '''

    def on_draw(self):
        self.batch.draw()

    def on_destroy(self):
        for sprite in self.sprites.values():
            sprite.delete()

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def update(self, dt):
        pass
