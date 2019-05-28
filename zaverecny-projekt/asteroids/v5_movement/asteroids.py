import pyglet
from spaceship import Spaceship

WINDOW_HEIGHT = 400
WINDOW_WIDTH = 800

objects = []
window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT)

def init_spaceship():
    spaceship = Spaceship()
    spaceship.x = window.width/2
    spaceship.y = window.height/2

    objects.append(spaceship)

def draw_all_objects():
    window.clear()

    for obj in objects:
        obj.draw()

def tick_all_objects(time_elapsed):
    for obj in objects:
        obj.tick(time_elapsed)



init_spaceship()
window.push_handlers(
    on_draw=draw_all_objects
)
pyglet.clock.schedule_interval(tick_all_objects, 1/30)
pyglet.app.run()


