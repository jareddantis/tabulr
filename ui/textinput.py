import pyglet

class Rectangle(object):
    '''Draws a rectangle into a batch.'''

    def __init__(self, x1, y1, x2, y2, batch):
        self.vertex_list = batch.add(4, pyglet.gl.GL_QUADS, None,
                                     ('v2i', [x1, y1, x2, y1, x2, y2, x1, y2]),
                                     ('c4B', [245, 240, 246, 255] * 4)
                                     )

class TextInput:
    def __init__(self, text, x, y, width, batch):
        self.document = pyglet.text.document.UnformattedDocument(text)
        self.document.set_style(0, len(self.document.text), {
            'color': (0, 0, 0, 255),
            'font_name': 'Rubik'
        })
        font = self.document.get_font()
        height = font.ascent - font.descent

        self.layout = pyglet.text.layout.IncrementalTextLayout(
            self.document, width, height, multiline=False, batch=batch)
        self.caret = pyglet.text.caret.Caret(self.layout)

        # Rectangular outline with padding
        pad = 8
        self.layout.x = x + pad
        self.layout.y = y + pad
        self.rectangle = Rectangle(x, y, x + width + pad*2, y + height + pad*2, batch)

    @property
    def content(self):
        return self.document.text

    @content.setter
    def content(self, new_content):
        self.document.text = new_content

    def hit_test(self, x, y):
        return (0 < x - self.layout.x < self.layout.width and
                0 < y - self.layout.y < self.layout.height)
