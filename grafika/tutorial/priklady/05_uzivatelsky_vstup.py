import pyglet

window = pyglet.window.Window(width=800, height=600, caption="Zpracování uživatelského vstupu")

# Vytvoření spritu, který budeme ovládat
# Místo obrázku použijeme obdélník, aby příklad fungoval bez externích souborů
rectangle = pyglet.shapes.Rectangle(x=window.width//2, y=window.height//2, 
                                   width=50, height=50, color=(0, 255, 0))

# Proměnné pro sledování stisknutých kláves
keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)

# Rychlost pohybu spritu
speed = 200  # pixelů za sekundu

# Text s instrukcemi
instructions = pyglet.text.Label('Použijte šipky pro pohyb obdélníku, klikněte myší pro přesun',
                                font_name='Arial',
                                font_size=18,
                                x=10, y=window.height - 30)

@window.event
def on_draw():
    window.clear()
    instructions.draw()
    rectangle.draw()

def update(dt):
    # Pohyb spritu podle stisknutých kláves
    if keys[pyglet.window.key.LEFT]:
        rectangle.x -= speed * dt
    if keys[pyglet.window.key.RIGHT]:
        rectangle.x += speed * dt
    if keys[pyglet.window.key.UP]:
        rectangle.y += speed * dt
    if keys[pyglet.window.key.DOWN]:
        rectangle.y -= speed * dt
    
    # Omezení pohybu na hranice okna
    rectangle.x = max(0, min(window.width - rectangle.width, rectangle.x))
    rectangle.y = max(0, min(window.height - rectangle.height, rectangle.y))

# Registrace funkce update pro pravidelné volání
pyglet.clock.schedule_interval(update, 1/60)  # 60 FPS

@window.event
def on_mouse_press(x, y, button, modifiers):
    # Přesun spritu na místo kliknutí
    if button == pyglet.window.mouse.LEFT:
        rectangle.x = x - rectangle.width // 2
        rectangle.y = y - rectangle.height // 2

pyglet.app.run()