import pyglet
import math
from pyglet import gl

# Degrees per second
ROTATION_SPEED = 200
ACCELERATION = 200

class SpaceObject:
    def __init__(self, batch, objects):

        self.x = 0
        self.y = 0
        self.x_speed = 0
        self.y_speed = 0
        self.rotation = 0
        self.can_collide = False
        self.objects = objects
        self.batch = batch

        image = pyglet.image.load(self.image_path())
        # Image is positioned by its middle, not lower left corner
        # Also important for rotation
        # // means integer division (floor) - 5//2 is 2 but 5/2 is 2.5
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        self.sprite = pyglet.sprite.Sprite(image, batch=batch)
        self.radius = self.sprite.width//2 + 3
        objects.append(self)

    def update_sprite(self):
        self.sprite.x = self.x
        self.sprite.y = self.y

        # we have rotation in rads, pyglet uses degrees
        # also, pyglet's zero is up, ours is on the right, right?
        self.sprite.rotation = 90 - math.degrees(self.rotation)


    def destroy_object(self):
        self.sprite.delete()



