import pyglet


def key_pressed(symbol, modifiers):
    print("Pressed key: " + str(symbol))


def key_released(symbol, modifiers):
    print("Released key: " + str(symbol))


window = pyglet.window.Window()
# When a user presses a key, key_pressed function will be called
# When a user releases a key, key_released function will be called
window.push_handlers(on_key_press=key_pressed, on_key_release=key_released)
pyglet.app.run()

# Documentation of pyglet keyboard handling
# https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/programming_guide/keyboard.html
