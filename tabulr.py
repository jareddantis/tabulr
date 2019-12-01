#!/usr/bin/env python3
from pyglet import window, clock, app, gl
from res import Resource
from util import Director

res = Resource()                             # Application graphical/font resources
window = window.Window(caption='tabulr')     # Main application window
director = Director(window)                  # For switching between scenes

@director.on('next_scene')
def on_next_scene():
    director.on_next_scene()

@director.on('start_over')
def on_start_over():
    director.on_reset()

@window.event
def on_draw():
    window.clear()
    director.on_draw()

def update(dt):
    director.on_update(dt)

if __name__ == "__main__":
    gl.glClearColor(43/255, 65/255, 98/255, 1)
    clock.schedule_interval(update, 1/60.0)
    app.run()
