from ui import Button
from .scene import Scene

class WelcomeScreen(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.next_button = Button('tick', window, self.batch,
                                  x=self.margin_left, y=(window.height//2) + 50)

    def update(self, dt):
        self.next_button.update(dt)

    def on_draw(self):
        self.batch.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        image_width = self.next_button.x + self.next_button.width
        image_height = self.next_button.y + self.next_button.height
        if image_width > x > self.next_button.x and image_height > y > self.next_button.y:
            self.next_button.on_mouse_enter()
        else:
            self.next_button.on_mouse_leave()
