#!/usr/bin/env python3
import pyglet
from res import Resource
from scenes import *
from event_bus import EventBus

bus = EventBus()                                                        # Communication from scenes
res = Resource()                                                        # Application graphical/font resources
window = pyglet.window.Window(caption='tabulr')                         # Main application window
scenes = [WelcomeScreen(window, bus), CourseInputScreen(window, bus)]   # Application scenes
scene = 0                                                               # Current application scene

# for scene switching
@bus.on('next_scene')
def on_next_scene():
    '''
    Change the scene that is currently being displayed to the next one.
    :return:
    '''
    global scene
    if scene < len(scenes) - 1:
        scenes[scene].on_destroy()
        scene += 1

@window.event
def on_draw():
    '''
    Draw current scene.
    :return:
    '''
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
