We need to make sure when you exit the screen, you reappear at the opposite end:

    self.x %= window.width
    self.y %= window.height
    
The transition is not smoot though, it can be fixed by this:

    def draw_all_objects():
        window.clear()
    
        for x_offset in (-window.width, 0, window.width):
            for y_offset in (-window.height, 0, window.height):
                # Remember the current state
                gl.glPushMatrix()
                # Move everything drawn from now on by (x_offset, y_offset, 0)
                gl.glTranslatef(x_offset, y_offset, 0)
    
                # Draw
                for obj in objects:
                    obj.draw()
    
                # Restore remembered state (this cancels the glTranslatef)
                gl.glPopMatrix()    
                
It basically draws the whole scene shifted by X pixels to the top/bottom/left/right                