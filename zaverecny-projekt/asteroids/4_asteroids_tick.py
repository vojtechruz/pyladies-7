import pyglet

def tick(time_elapsed):
    print("Tick-Tock...")
    print(str(time_elapsed) + "seconds since the last call")

# Function 'tick' will be called  every 1/2 second
# Note that it is just 'tick', not 'tick()'
pyglet.clock.schedule_interval(tick, 1/2)

pyglet.app.run()