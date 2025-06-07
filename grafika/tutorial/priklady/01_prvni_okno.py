import pyglet

# Vytvoření okna o velikosti 800x600 pixelů
window = pyglet.window.Window(width=800, height=600, caption="Moje první Pyglet okno")

# Funkce pro vykreslení obsahu okna
@window.event
def on_draw():
    # Vyčištění okna (smazání předchozího obsahu)
    window.clear()
    # Zde budeme později přidávat kód pro vykreslení objektů

# Spuštění aplikace
pyglet.app.run()