from pyglet.graphics import Batch

class Scene:
    def __init__(self, window):
        self.window = window
        self.batch = Batch()
        self.margin_left = 36
