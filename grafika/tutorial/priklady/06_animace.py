import pyglet
import random

window = pyglet.window.Window(width=800, height=600, caption="Základy animace")

# Vytvoření batch pro efektivní vykreslování
batch = pyglet.graphics.Batch()

# Vytvoření seznamu animovaných objektů
circles = []
for i in range(20):
    x = random.randint(0, window.width)
    y = random.randint(0, window.height)
    size = random.randint(10, 50)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    circle = pyglet.shapes.Circle(x, y, size, color=color, batch=batch)
    
    # Přidání vlastností pro animaci
    circle.dx = random.uniform(-100, 100)  # rychlost v ose x
    circle.dy = random.uniform(-100, 100)  # rychlost v ose y
    
    circles.append(circle)

# Přidání FPS displeje
fps_display = pyglet.window.FPSDisplay(window=window)

@window.event
def on_draw():
    window.clear()
    batch.draw()
    fps_display.draw()  # Zobrazení FPS

def update(dt):
    for circle in circles:
        # Aktualizace pozice
        circle.x += circle.dx * dt
        circle.y += circle.dy * dt
        
        # Odraz od okrajů okna
        if circle.x < circle.radius or circle.x > window.width - circle.radius:
            circle.dx = -circle.dx
        if circle.y < circle.radius or circle.y > window.height - circle.radius:
            circle.dy = -circle.dy

# Registrace funkce update pro pravidelné volání
pyglet.clock.schedule_interval(update, 1/60)  # 60 FPS

pyglet.app.run()