import pyglet


def stisknuta_klavesa(symbol, modifikatory):
    # Číslo reprezentující klávesu
    print("symbol: " + str(symbol))
    # Číslo reprezentující držení dodatečných kláves
    # jako CTRL, ALT nebo SHIFT
    print("modifikatory: " + str(modifikatory))


okno = pyglet.window.Window()
# Když uživatel stiskne klávesu, bude volána funkce stisknuta_klavesa
okno.push_handlers(on_key_press=stisknuta_klavesa)
pyglet.app.run()

# Dokumentace k ovládání klávesnice v pyglet
# https://pyglet.readthedocs.io/en/latest/programming_guide/keyboard.html