import pyglet
from spaceship import Spaceship

WINDOW_HEIGHT = 400
WINDOW_WIDTH = 800

objects = []
keys_pressed = set()
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

def on_key_pressed(key, modifiers):
    keys_pressed.add(key)
    print("Key pressed " + str(key))
    print("Keys currently pressed: " + str(keys_pressed))


def on_key_released(key, modifiers):
    keys_pressed.remove(key)
    print("Key released " + str(key))
    print("Keys currently pressed: " + str(keys_pressed))

init_spaceship()
window.push_handlers(
    on_draw=draw_all_objects,
    on_key_press=on_key_pressed,
    on_key_release=on_key_released
)
pyglet.app.run()


