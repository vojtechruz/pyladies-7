We now pass keys pressed to the tick method of our spaceship.

Then left/right keys are used to change rotation:

def tick(self, time_elapsed, keys_pressed):
    if pyglet.window.key.LEFT in keys_pressed:
        self.rotation = self.rotation + time_elapsed*ROTATION_SPEED
    if pyglet.window.key.RIGHT in keys_pressed:
        self.rotation = self.rotation - time_elapsed*ROTATION_SPEED
        
In the draw() method of the spaceship, we now set rotation of the sprite:

    def draw(self):
        ...
        # we have rotation in rads, pyglet uses degrees
        # also, pyglet's zero is up, ours is on the right, right?
        self.sprite.rotation = 90 - math.degrees(self.rotation)
        self.sprite.draw()        