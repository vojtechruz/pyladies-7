import pyglet
import math
from space_object import SpaceObject
from laser import Laser

# Degrees per second
ROTATION_SPEED = 4
ACCELERATION = 200
LASER_SPEED = 500
LASER_FIRE_RATE = 0.3

class Spaceship(SpaceObject):
    def __init__(self, batch, objects, window):
        super().__init__(batch, objects, window)
        self.engine_counter = 2
        self.engine_image_number = "06"
        self.laser_cooldown = 0
        engine_image = self.get_engine_image()

        self.engine_sprite = pyglet.sprite.Sprite(engine_image, batch=batch)

    def image_path(self):
        return "../assets/PNG/playerShip1_orange.png"

    def tick(self, time_elapsed, keys_pressed, window):
        self.engine_counter = self.engine_counter -1
        self.laser_cooldown = self.laser_cooldown - time_elapsed

        if self.engine_counter == 0:
            self.engine_counter = 2
            engine_image = self.get_engine_image()
            self.engine_sprite = pyglet.sprite.Sprite(engine_image, batch=self.batch)

        self.engine_sprite.visible = False
        if pyglet.window.key.LEFT in keys_pressed:
            self.rotation = self.rotation + time_elapsed*ROTATION_SPEED
        if pyglet.window.key.RIGHT in keys_pressed:
            self.rotation = self.rotation - time_elapsed*ROTATION_SPEED
        if pyglet.window.key.UP in keys_pressed:
            self.engine_sprite.visible = True
            self.x_speed += time_elapsed * ACCELERATION * math.cos(self.rotation)
            self.y_speed += time_elapsed * ACCELERATION * math.sin(self.rotation)
        if pyglet.window.key.SPACE in keys_pressed:
            self.fire_laser()

        self.x = self.x + time_elapsed*self.x_speed
        self.y = self.y + time_elapsed*self.y_speed

        # infinite space - wraparound coordinates
        self.x %= window.width
        self.y %= window.height

        self.engine_sprite.x = self.x
        self.engine_sprite.y = self.y
        self.engine_sprite.rotation = 270 - math.degrees(self.rotation)

        super().update_sprite()


    def destroy_object(self):
        super().destroy_object()
        self.engine_sprite.delete()

    def get_engine_image(self):
        if self.engine_image_number == "06":
            self.engine_image_number = "07"
        else:
            self.engine_image_number = "06"

        engine_image = pyglet.image.load("../assets/PNG/effects/fire"+self.engine_image_number+".png")
        engine_image.anchor_x = engine_image.width //2
        engine_image.anchor_y = -engine_image.height -5
        return engine_image

    def fire_laser(self):
        if(self.laser_cooldown <= 0):
            laser = Laser(self.batch, self.objects, self.window)
            laser.x = self.x + self.sprite.width // 2 * math.cos(self.rotation)
            laser.y = self.y + self.sprite.height // 2 * math.sin(self.rotation)
            laser.x_speed = self.x_speed + LASER_SPEED * math.cos(self.rotation)
            laser.y_speed = self.y_speed + LASER_SPEED * math.sin(self.rotation)
            laser.rotation = self.rotation
            self.laser_cooldown = LASER_FIRE_RATE

