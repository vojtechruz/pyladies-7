import pyglet
from spaceship import Spaceship
from asteroid import Asteroid
from pyglet import gl
import random

WINDOW_HEIGHT = 400
WINDOW_WIDTH = 800
ASTEROID_COUNT = 4
ASTEROID_MIN_SPEED = 10
ASTEROID_MAX_SPEED = 50

objects = []
keys_pressed = set()
window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT)

def init_spaceship():
    spaceship = Spaceship()
    spaceship.x = window.width/2
    spaceship.y = window.height/2

    objects.append(spaceship)

def init_asteroids():
    for i in range(ASTEROID_COUNT):
        asteroid = Asteroid()
        asteroid.x = random.randint(0, window.width)
        asteroid.y = random.randint(0, window.height)
        asteroid.x_speed = random.randint(-1,1) * random.randint(ASTEROID_MIN_SPEED,ASTEROID_MAX_SPEED)
        asteroid.y_speed = random.randint(-1,1) * random.randint(ASTEROID_MIN_SPEED,ASTEROID_MAX_SPEED)
        objects.append(asteroid)
    pass

def draw_all_objects():
    window.clear()

    for x_offset in (-window.width, 0, window.width):
        for y_offset in (-window.height, 0, window.height):
            # Remember the current state
            gl.glPushMatrix()
            # Move everything drawn from now on by (x_offset, y_offset, 0)
            gl.glTranslatef(x_offset, y_offset, 0)

            # Draw
            for obj in objects:
                obj.draw()

            # Restore remembered state (this cancels the glTranslatef)
            gl.glPopMatrix()


def tick_all_objects(time_elapsed):
    for obj in objects:
        obj.tick(time_elapsed, keys_pressed, window)

def on_key_pressed(key, modifiers):
    keys_pressed.add(key)

def on_key_released(key, modifiers):
    keys_pressed.remove(key)


init_spaceship()
init_asteroids()
window.push_handlers(
    on_draw=draw_all_objects,
    on_key_press=on_key_pressed,
    on_key_release=on_key_released
)
pyglet.clock.schedule_interval(tick_all_objects, 1/30)
pyglet.app.run()