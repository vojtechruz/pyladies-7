from space_object import SpaceObject

class Laser(SpaceObject):
    def __init__(self, batch, objects):
        super().__init__(batch, objects)

    def image_path(self):
        return "../assets/PNG/Lasers/laserBlue02.png"

    def tick(self, time_elapsed, keys_pressed, window):
        self.x = self.x + time_elapsed*self.x_speed
        self.y = self.y + time_elapsed*self.y_speed

        # infinite space - wraparound coordinates
        self.x %= window.width
        self.y %= window.height

        super().update_sprite()




