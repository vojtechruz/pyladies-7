import pyglet
import math

# Degrees per second
ROTATION_SPEED = 200
ACCELERATION = 200

class Spaceship:
    def __init__(self):

        self.x = 0
        self.y = 0
        self.x_speed = 0
        self.y_speed = 0
        self.rotation = 0

        image = pyglet.image.load("../assets/PNG/playerShip1_blue.png")
        # Image is positioned by its middle, not lower left corner
        # Also important for rotation
        # // means integer division (floor) - 5//2 is 2 but 5/2 is 2.5
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        self.sprite = pyglet.sprite.Sprite(image)

    def draw(self):
        self.sprite.x = self.x
        self.sprite.y = self.y

        # we have rotation in rads, pyglet uses degrees
        # also, pyglet's zero is up, ours is on the right, right?
        self.sprite.rotation = 90 - math.degrees(self.rotation)

        self.sprite.draw()

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



