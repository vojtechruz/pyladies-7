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



init_spaceship()
window.push_handlers(
    on_draw=draw_all_objects
)
pyglet.app.run()


