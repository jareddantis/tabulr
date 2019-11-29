#!/usr/bin/env python3
from pyglet import window, clock, app, gl
from res import Resource
from util.director import Director

res = Resource()                                    # Application graphical/font resources
window = window.Window(caption='tabulr')     # Main application window
director = Director(window)                         # For switching between scenes

@director.on('next_scene')
def on_next_scene():
    director.on_next_scene()

@window.event
def on_draw():
    """
    Draw current scene.
    :return:
    """
    window.clear()
    director.on_draw()

@window.event
def on_mouse_motion(x, y, dx, dy):
    director.current_scene.on_mouse_motion(x, y, dx, dy)

@window.event
def on_mouse_press(x, y, button, modifiers):
    director.current_scene.on_mouse_press(x, y, button, modifiers)

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    director.current_scene.on_mouse_drag(x, y, dx, dy, buttons, modifiers)

@window.event
def on_text(text):
    director.current_scene.on_text(text)

@window.event
def on_text_motion(motion):
    director.current_scene.on_text_motion(motion)

@window.event
def on_text_motion_select(motion):
    director.current_scene.on_text_motion_select(motion)

@window.event
def on_key_press(symbol, modifiers):
    director.current_scene.on_key_press(symbol, modifiers)

def update(dt):
    director.current_scene.update(dt)

if __name__ == "__main__":
    gl.glClearColor(43/255, 65/255, 98/255, 1)
    clock.schedule_interval(update, 1/60.0)
    app.run()
