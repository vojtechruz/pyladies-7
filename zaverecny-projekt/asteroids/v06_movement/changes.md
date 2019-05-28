Our ship now has vertical and horizontal speed:
    
    self.x_speed = 0
    self.y_speed = 0


Key pressed UP will increase the speed of our ship:

    if pyglet.window.key.UP in keys_pressed:
        self.x_speed += time_elapsed * ACCELERATION * math.cos(self.rotation)
        self.y_speed += time_elapsed * ACCELERATION * math.sin(self.rotation)
    
    self.x = self.x + time_elapsed*self.x_speed
    self.y = self.y + time_elapsed*self.y_speed