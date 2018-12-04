import pyglet


def key_pressed(symbol, modifiers):
    # Number representing key
    print("symbol: " + symbol)
    # Number representing holding additional keys
    # such as CTRL, ALT or SHIFT
    print("modifiers: " + modifiers)


window = pyglet.window.Window()
# When a user presses a key, key_pressed function will be called
window.push_handlers(on_key_press=key_pressed)
pyglet.app.run()

# Documentation of pyglet keyboard handling
# https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/programming_guide/keyboard.html
