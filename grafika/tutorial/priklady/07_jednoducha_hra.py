import pyglet
import random
from pyglet.window import key

# Vytvoření okna
window = pyglet.window.Window(width=800, height=600, caption="Jednoduchá hra")

# Načtení obrázků (použijeme barevné tvary místo obrázků)
batch = pyglet.graphics.Batch()

# Vytvoření hráče
player = pyglet.shapes.Rectangle(x=window.width//2, y=window.height//2, 
                                width=30, height=30, color=(0, 255, 0), batch=batch)
player.anchor_x = player.width // 2
player.anchor_y = player.height // 2

# Vytvoření objektů k sebrání
collectibles = []
for i in range(10):
    x = random.randint(20, window.width - 20)
    y = random.randint(20, window.height - 20)
    collectible = pyglet.shapes.Circle(x=x, y=y, radius=10, color=(255, 255, 0), batch=batch)
    collectibles.append(collectible)

# Skóre
score = 0
score_label = pyglet.text.Label(f'Skóre: {score}',
                               font_name='Arial',
                               font_size=18,
                               x=10, y=window.height - 30,
                               batch=batch)

# Instrukce
instructions = pyglet.text.Label('Použijte šipky pro pohyb, sbírejte žluté kruhy',
                                font_name='Arial',
                                font_size=14,
                                x=window.width - 10, y=window.height - 10,
                                anchor_x='right', anchor_y='top',
                                batch=batch)

# Zpracování vstupu
keys = key.KeyStateHandler()
window.push_handlers(keys)

# Rychlost hráče
player_speed = 200

@window.event
def on_draw():
    window.clear()
    batch.draw()

def update(dt):
    global score
    
    # Pohyb hráče
    if keys[key.LEFT]:
        player.x -= player_speed * dt
    if keys[key.RIGHT]:
        player.x += player_speed * dt
    if keys[key.UP]:
        player.y += player_speed * dt
    if keys[key.DOWN]:
        player.y -= player_speed * dt
    
    # Omezení pohybu na hranice okna
    player.x = max(player.width//2, min(window.width - player.width//2, player.x))
    player.y = max(player.height//2, min(window.height - player.height//2, player.y))
    
    # Kontrola kolizí s objekty
    for collectible in list(collectibles):
        # Jednoduchá detekce kolize pomocí vzdálenosti středů
        distance = ((player.x - collectible.x) ** 2 + (player.y - collectible.y) ** 2) ** 0.5
        if distance < player.width//2 + collectible.radius:
            # Kolize - sebrání objektu
            collectibles.remove(collectible)
            collectible.delete()
            score += 1
            score_label.text = f'Skóre: {score}'
            
            # Vytvoření nového objektu
            x = random.randint(20, window.width - 20)
            y = random.randint(20, window.height - 20)
            new_collectible = pyglet.shapes.Circle(x=x, y=y, radius=10, color=(255, 255, 0), batch=batch)
            collectibles.append(new_collectible)

# Registrace funkce update
pyglet.clock.schedule_interval(update, 1/60)

pyglet.app.run()