from space_object import SpaceObject

EXPLOSION_LIFETIME = 0.1


class Explosion(SpaceObject):
    def __init__(self, batch, objects, window):
        super().__init__(batch, objects, window)
        self.lifetime_remaining = EXPLOSION_LIFETIME

    def image_path(self):
        return "../assets/smokeParticleAssets/PNG/Explosion/explosion00.png"

    def tick(self, time_elapsed, keys_pressed, window):
        self.sprite.scale = 1/3

        super().update_sprite()

        self.lifetime_remaining = self.lifetime_remaining - time_elapsed
        if self.lifetime_remaining <= 0:
            self.destroy_object()

