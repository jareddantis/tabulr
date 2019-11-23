#!/usr/bin/env python3
import pyglet
from res import Resource
from scenes import *

res = Resource()
batch = pyglet.graphics.Batch()
window = pyglet.window.Window(caption='tabulr')
scenes = [WelcomeScreen(window, batch)]
scene = 0

@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_mouse_motion(x, y, dx, dy):
    scenes[scene].on_mouse_motion(x, y, dx, dy)

def update(dt):
    scenes[scene].update(dt)

if __name__ == "__main__":
    pyglet.gl.glClearColor(43/255, 65/255, 98/255, 1)
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()
