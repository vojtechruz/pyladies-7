import pyglet

def key_pressed(symbol, modifiers):

    # Keys can be accessed via:
    # pyglet.window.key.*
    # Such as pyglet.window.key.A
    # or pyglet.window.key.ENTER

    if symbol == pyglet.window.key.UP:
        print("Going UP!")
    elif symbol == pyglet.window.key.DOWN:
        print("Going DOWN")
    elif symbol == pyglet.window.key.LEFT:
        print("Going LEFT")
    elif symbol == pyglet.window.key.RIGHT:
        print("Going RIGHT")

window = pyglet.window.Window()
# When a user presses a key, key_pressed function will be called
window.push_handlers(on_key_press=key_pressed)
pyglet.app.run()

# Documentation of pyglet keyboard handling
# https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/programming_guide/keyboard.html