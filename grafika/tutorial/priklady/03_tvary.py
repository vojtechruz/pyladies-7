import pyglet

window = pyglet.window.Window(width=800, height=600, caption="Kreslení tvarů")

# Vytvoření batch pro efektivní vykreslování
batch = pyglet.graphics.Batch()

# Vytvoření různých tvarů
circle = pyglet.shapes.Circle(x=100, y=150, radius=50, color=(255, 0, 0), batch=batch)
rectangle = pyglet.shapes.Rectangle(x=200, y=200, width=200, height=100, color=(0, 255, 0), batch=batch)
line = pyglet.shapes.Line(x=400, y=100, x2=700, y2=300, thickness=3, color=(0, 0, 255), batch=batch) # width misto thickness u jine verze pygletu
star = pyglet.shapes.Star(x=600, y=150, outer_radius=50, inner_radius=30, num_spikes=5, color=(255, 255, 0), batch=batch)

@window.event
def on_draw():
    window.clear()
    # Vykreslení všech tvarů najednou pomocí batch
    batch.draw()

pyglet.app.run()