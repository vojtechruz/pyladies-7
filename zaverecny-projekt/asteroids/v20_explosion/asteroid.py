from space_object import SpaceObject
from explosion import Explosion

class Asteroid(SpaceObject):
    def __init__(self, batch, objects, window):
        super().__init__(batch, objects, window)
        self.can_collide = True

    def image_path(self):
        return "../assets/PNG/Meteors/meteorBrown_big3.png"

    def tick(self, time_elapsed, keys_pressed, window):
        self.x = self.x + time_elapsed*self.x_speed
        self.y = self.y + time_elapsed*self.y_speed

        # infinite space - wraparound coordinates
        self.x %= window.width
        self.y %= window.height

        self.rotation += (self.x_speed + self.y_speed)*0.001
        super().update_sprite()

    def hit_by_laser(self):
        explosion = Explosion(self.batch, self.objects, self.window)
        explosion.x = self.x
        explosion.y = self.y
        self.destroy_object()

        return True


