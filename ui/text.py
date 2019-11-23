from pyglet.text import Label

class Text(Label):
    def __init__(self, content, bold=False, batch=None, size=28, x=0, y=0):
        super().__init__(content, batch=batch, font_name='Rubik Bold' if bold else 'Rubik',
                         font_size=size, x=x, y=y)
