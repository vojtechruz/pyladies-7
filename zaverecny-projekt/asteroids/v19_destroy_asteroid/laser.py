from space_object import SpaceObject

LASER_LIFETIME = 1.5

class Laser(SpaceObject):
    def __init__(self, batch, objects, window):
        super().__init__(batch, objects, window)
        self.lifetime_remaining = LASER_LIFETIME

    def image_path(self):
        return "../assets/PNG/Lasers/laserBlue02.png"

    def tick(self, time_elapsed, keys_pressed, window):
        self.x = self.x + time_elapsed*self.x_speed
        self.y = self.y + time_elapsed*self.y_speed

        # infinite space - wraparound coordinates
        self.x %= window.width
        self.y %= window.height

        super().update_sprite()

        self.lifetime_remaining = self.lifetime_remaining - time_elapsed
        if self.lifetime_remaining <= 0:
            self.destroy_object()

        for obj in self.objects:
            if self.overlaps(obj):
                remove_laser = obj.hit_by_laser()
                if(remove_laser):
                    self.destroy_object()






