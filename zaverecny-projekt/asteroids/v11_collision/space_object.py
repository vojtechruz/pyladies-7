import pyglet
import math
from pyglet import gl

# Degrees per second
ROTATION_SPEED = 200
ACCELERATION = 200

class SpaceObject:
    def __init__(self):

        self.x = 0
        self.y = 0
        self.x_speed = 0
        self.y_speed = 0
        self.rotation = 0
        self.can_collide = False
        self.collision = False

        image = pyglet.image.load(self.image_path())
        # Image is positioned by its middle, not lower left corner
        # Also important for rotation
        # // means integer division (floor) - 5//2 is 2 but 5/2 is 2.5
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        self.sprite = pyglet.sprite.Sprite(image)
        self.radius = self.sprite.width//2 + 3

    def draw_circle(self, x, y, radius):
        iterations = 20
        s = math.sin(2*math.pi / iterations)
        c = math.cos(2*math.pi / iterations)

        dx, dy = radius, 0

        gl.glBegin(gl.GL_LINE_STRIP)
        if(self.collision):
            gl.glColor3d(255, 0, 0)
        else:
            gl.glColor3d(255, 255, 255)

        for i in range(iterations+1):
            gl.glVertex2f(x+dx, y+dy)
            dx, dy = (dx*c - dy*s), (dy*c + dx*s)
        gl.glEnd()

    def draw(self):
        self.sprite.x = self.x
        self.sprite.y = self.y

        # we have rotation in rads, pyglet uses degrees
        # also, pyglet's zero is up, ours is on the right, right?
        self.sprite.rotation = 90 - math.degrees(self.rotation)

        self.sprite.draw()
        self.draw_circle(self.sprite.x, self.sprite.y, self.radius)





