import pyglet
import math
from space_object import SpaceObject

# Degrees per second
ROTATION_SPEED = 200
ACCELERATION = 200

class Spaceship(SpaceObject):
    def __init__(self):
        super().__init__()

    def image_path(self):
        return "../assets/PNG/playerShip1_orange.png"

    def tick(self, time_elapsed, keys_pressed, window):
        if pyglet.window.key.LEFT in keys_pressed:
            self.rotation = self.rotation + time_elapsed*ROTATION_SPEED
        if pyglet.window.key.RIGHT in keys_pressed:
            self.rotation = self.rotation - time_elapsed*ROTATION_SPEED
        if pyglet.window.key.UP in keys_pressed:
            self.x_speed += time_elapsed * ACCELERATION * math.cos(self.rotation)
            self.y_speed += time_elapsed * ACCELERATION * math.sin(self.rotation)

        self.x = self.x + time_elapsed*self.x_speed
        self.y = self.y + time_elapsed*self.y_speed

        # infinite space - wraparound coordinates
        self.x %= window.width
        self.y %= window.height



