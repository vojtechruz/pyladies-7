import pyglet

def stisknuta_klavesa(symbol, modifikatory):

    # Klávesy lze přistupovat přes:
    # pyglet.window.key.*
    # Například pyglet.window.key.A
    # nebo pyglet.window.key.ENTER

    if symbol == pyglet.window.key.UP:
        print("Jdu NAHORU!")
    elif symbol == pyglet.window.key.DOWN:
        print("Jdu DOLŮ")
    elif symbol == pyglet.window.key.LEFT:
        print("Jdu DOLEVA")
    elif symbol == pyglet.window.key.RIGHT:
        print("Jdu DOPRAVA")

okno = pyglet.window.Window()
# Když uživatel stiskne klávesu, bude volána funkce stisknuta_klavesa
okno.push_handlers(on_key_press=stisknuta_klavesa)
pyglet.app.run()

# Dokumentace k ovládání klávesnice v pyglet
# https://pyglet.readthedocs.io/en/latest/programming_guide/keyboard.html