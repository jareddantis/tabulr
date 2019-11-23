#!/usr/bin/env python3
import pyglet
from res import Resource
from scenes import *
from event_bus import EventBus

bus = EventBus()
res = Resource()
window = pyglet.window.Window(caption='tabulr')
scenes = [WelcomeScreen(window, bus)]
scene = 0

@bus.on('next_scene')
def on_next_scene():
    global scene
    scene += 1

@window.event
def on_draw():
    window.clear()
    scenes[scene].on_draw()

@window.event
def on_mouse_motion(x, y, dx, dy):
    scenes[scene].on_mouse_motion(x, y, dx, dy)

@window.event
def on_mouse_press(x, y, button, modifiers):
    scenes[scene].on_mouse_press(x, y, button, modifiers)

def update(dt):
    scenes[scene].update(dt)

if __name__ == "__main__":
    pyglet.gl.glClearColor(43/255, 65/255, 98/255, 1)
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()
