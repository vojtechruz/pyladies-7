import math
import random

import pyglet
from pyglet import gl
from pyglet.window import key

# Consts
ACCELERATION = 20  # pixels per sec per sec
ROTATION_SPEED = 4  # radians per sec
ASTEROID_SPEED = 100  # pixels/radians per sec (divided by 10 for rads)


# Global state:
objects = []  # we'll store all game objects here
pressed_keys = set()  # currently pressed keys, a set
batch = pyglet.graphics.Batch()  # we'll put all sprites here


# Classes:
class SpaceObject:
    """
    This class represents any space object

    Attributes:

     * x, y: position in the window
     * x_spped, y_speed: speed in x/y direction
     * rotation: rotation of the object in radians, 0 means facing north
    """
    def __init__(self):
        # set some initial values:
        self.x = 200
        self.y = 400
        self.rotation = 0
        self.x_speed = 0
        self.y_speed = 0

        # assign and position the sprite with image
        image = pyglet.image.load(self.image_path())
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        self.sprite = pyglet.sprite.Sprite(image, batch=batch)
        self.update_sprite()

        # register the ship to the global list of game objects
        objects.append(self)

    def update_sprite(self):
        """
        Take the attributes of the ship and apply them to it's sprite.
        Do some conversion if needed.
        """
        self.sprite.x = self.x
        self.sprite.y = self.y
        # we have rotation in rads, pyglet uses degrees
        # also, pyglet's zero is up, ours is on the right, right?
        self.sprite.rotation = 90 - math.degrees(self.rotation)

    def tick(self, dt):
        # apply SPEED * TIME = DISTANCE
        self.x += dt * self.x_speed
        self.y += dt * self.y_speed

        # infinite space - wraparound coordinates
        self.x %= window.width
        self.y %= window.height

        # finally, apply the changes to the sprite
        self.update_sprite()


class SpaceShip(SpaceObject):
    """
    Spaceship is controlled by keyboard!
    """
    def image_path(self):
        return '../assets/PNG/playerShip1_blue.png'

    def tick(self, dt):
        rotation_speed = 0  # no keys pressed, no rotation
        acceleration = 0
        if key.LEFT in pressed_keys:
            rotation_speed += ROTATION_SPEED
        if key.RIGHT in pressed_keys:
            rotation_speed -= ROTATION_SPEED
        if key.UP in pressed_keys:
            acceleration = ACCELERATION

        # Accelerate when key.UP is pressed
        self.x_speed += dt * acceleration * math.cos(self.rotation)
        self.y_speed += dt * acceleration * math.sin(self.rotation)

        self.rotation += rotation_speed * dt

        super().tick(dt)


class Asteroid(SpaceObject):
    """
    Asteroids fly by with random speed and rotation, they differ in sizes
    """
    def __init__(self):
        super().__init__()
        coin = random.randint(0, 1)
        if coin:
            self.x = window.width // 2
            self.y = 0
        else:
            self.x = 0
            self.y = window.height // 2
        self.x_speed = self.random_speed()
        self.y_speed = self.random_speed()
        self.rotation_speed = self.random_speed() // 10

    def random_speed(self):
        return random.randint(-ASTEROID_SPEED, ASTEROID_SPEED)

    def image_path(self):
        sizes = ['big', 'med', 'small', 'tiny']
        size = random.choice(sizes)
        num = random.randint(1, 2)
        return '../assets/PNG/Meteors/meteorGrey_{}{}.png'.format(size, num)

    def tick(self, dt):
        self.rotation += self.rotation_speed * dt
        super().tick(dt)


# main window
window = pyglet.window.Window()


# Create new spaceship, it registers itself to the global list
spaceship = SpaceShip()
# Add some asteroids
for _ in range(8):
    Asteroid()


# Pyglet objects and functions
def draw_all_objects():
    """For all objects, draw theirs sprites"""
    window.clear()

    for x_offset in (-window.width, 0, window.width):
        for y_offset in (-window.height, 0, window.height):
            # Remember the current state
            gl.glPushMatrix()
            # Move everything drawn from now on by (x_offset, y_offset, 0)
            gl.glTranslatef(x_offset, y_offset, 0)

            # Draw
            batch.draw()

            # Restore remembered state (this cancels the glTranslatef)
            gl.glPopMatrix()


def tick_all_objects(dt):
    """For all objects, tick them"""
    for obj in objects:
        obj.tick(dt)


def key_pressed(sym, mod):
    """Save the pressed keys to our global set"""
    pressed_keys.add(sym)


def key_released(sym, mod):
    """Remove the released keys from our global set"""
    pressed_keys.discard(sym)


# register our function as handlers:
window.push_handlers(
    on_draw=draw_all_objects,
    on_key_press=key_pressed,
    on_key_release=key_released,
)

# schedule our ticking function to happen often:
pyglet.clock.schedule_interval(tick_all_objects, 1/30)

# finally, run the game:
pyglet.app.run()