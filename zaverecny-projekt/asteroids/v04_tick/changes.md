Spaceship now has tick method

def tick(self, time_elapsed):
    print("Tick Tock!")
    
And for each of our space objects we call its tick():

def tick_all_objects(time_elapsed):
    for obj in objects:
        obj.tick(time_elapsed)
                
And we do it every 1/30th of a second:

pyglet.clock.schedule_interval(tick_all_objects, 1/30)


    