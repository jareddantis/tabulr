import pyglet

class Resource:
    def __init__(self):
        pyglet.resource.path = ['res']
        pyglet.resource.reindex()
        pyglet.resource.add_font('Rubik-Regular.ttf')
        pyglet.resource.add_font('Rubik-Bold.ttf')

        self.FONT_REGULAR = pyglet.font.load('Rubik')
        self.FONT_BOLD = pyglet.font.load('Rubik', bold=True)