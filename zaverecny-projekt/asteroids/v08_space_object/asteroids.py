import pyglet
from spaceship import Spaceship
from pyglet.math import Mat4, Vec3

WINDOW_HEIGHT = 400
WINDOW_WIDTH = 800

objects = []
keys_pressed = set()
window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT)

def init_spaceship():
    spaceship = Spaceship()
    spaceship.x = window.width/2
    spaceship.y = window.height/2

    objects.append(spaceship)

def draw_all_objects():
    window.clear()

    for x_offset in (-window.width, 0, window.width):
        for y_offset in (-window.height, 0, window.height):
            # Move everything drawn from now on by (x_offset, y_offset, 0)
            window.view = Mat4.from_translation(Vec3(x_offset, y_offset, 0))

            # Draw
            for obj in objects:
                obj.draw()

            # Restore the default (un-shifted) view
            window.view = Mat4()


def tick_all_objects(time_elapsed):
    for obj in objects:
        obj.tick(time_elapsed, keys_pressed, window)

def on_key_pressed(key, modifiers):
    keys_pressed.add(key)

def on_key_released(key, modifiers):
    keys_pressed.remove(key)


init_spaceship()
window.push_handlers(
    on_draw=draw_all_objects,
    on_key_press=on_key_pressed,
    on_key_release=on_key_released
)
pyglet.clock.schedule_interval(tick_all_objects, 1/30)
pyglet.app.run()