import pyglet

ROTATION_SPEED = 4

class Spaceship:
    def __init__(self):
        self.x = 0
        self.y = 0
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
        self.sprite.rotation = self.rotation
        self.sprite.draw()

    def tick(self, time_elapsed):
        print("Tick Tock!")
