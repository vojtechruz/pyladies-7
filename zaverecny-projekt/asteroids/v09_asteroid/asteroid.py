from space_object import SpaceObject

# Degrees per second
ROTATION_SPEED = 200
ACCELERATION = 200

class Asteroid(SpaceObject):
    def __init__(self):
        super().__init__()

    def image_path(self):
        return "../assets/PNG/Meteors/meteorBrown_big3.png"

    def tick(self, time_elapsed, keys_pressed, window):
        self.x = self.x + time_elapsed*self.x_speed
        self.y = self.y + time_elapsed*self.y_speed

        # infinite space - wraparound coordinates
        self.x %= window.width
        self.y %= window.height



