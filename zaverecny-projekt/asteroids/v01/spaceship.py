import pyglet

class Spaceship:
    def __init__(self):
        self.x = 0
        self.y = 0
        image = pyglet.image.load("../assets/PNG/playerShip1_blue.png")
        self.sprite = pyglet.sprite.Sprite(image)

    def draw(self):
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.sprite.draw()
