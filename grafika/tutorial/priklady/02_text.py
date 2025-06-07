import pyglet

# Vytvoření okna
window = pyglet.window.Window(width=800, height=600, caption="Moje první Pyglet okno")

# Vytvoření popisku s textem
label = pyglet.text.Label('Ahoj, Pyglet!',
                          font_name='Arial',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    # Vykreslení popisku
    label.draw()

pyglet.app.run()