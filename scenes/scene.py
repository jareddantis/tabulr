class Scene:
    def __init__(self, window, batch):
        self.window = window
        self.batch = batch
        self.margin_left = 36
        self.sprites = {}

    def init_sprite(self, name, sprite):
        self.sprites[name] = sprite

    def on_destroy(self):
        for sprite in self.sprites.values():
            sprite.delete()
