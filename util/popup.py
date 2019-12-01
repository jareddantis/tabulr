from pyglet.window import Window
from pyglet.graphics import Batch

class Popup(Window):
    def __init__(self, parent_window, on_close, caption, width=640, height=480):
        """
        Create new secondary window.
        Currently this is used to confirm already entered courses and to confirm background image.
        :param parent_window: Parent pyglet.window.Window instance (to switch back to afterward)
        :param on_close: Function to call after this window is closed
        :param caption: Title bar caption
        """
        super().__init__(caption=caption, style=Window.WINDOW_STYLE_TOOL, width=width, height=height)
        self.switch_to()
        self.margin = 36
        self.closed = False
        self.on_close_callback = on_close
        self.batch = Batch()
        self.parent_window = parent_window

    def on_draw(self):
        self.clear()

        # On-screen text and buttons
        self.batch.draw()

    def on_close(self, proceed=False):
        self.on_close_callback(proceed)
        self.closed = True
        self.close()
        self.parent_window.switch_to()
        self.parent_window.activate()

    def switch_to(self):
        super().switch_to()
        self.activate()