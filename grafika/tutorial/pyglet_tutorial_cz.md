# Pyglet Tutorial pro začátečníky

## Obsah
1. [Úvod do knihovny Pyglet](#úvod-do-knihovny-pyglet)
2. [Instalace](#instalace)
3. [Vytvoření prvního okna](#vytvoření-prvního-okna)
4. [Kreslení tvarů](#kreslení-tvarů)
5. [Práce s obrázky](#práce-s-obrázky)
6. [Zpracování uživatelského vstupu](#zpracování-uživatelského-vstupu)
7. [Přehrávání zvuků](#přehrávání-zvuků)
8. [Základy animace](#základy-animace)
9. [Jednoduchý příklad hry](#jednoduchý-příklad-hry)
10. [Další zdroje](#další-zdroje)

## Úvod do knihovny Pyglet

Pyglet je multiplatformní knihovna pro vývoj her a multimediálních aplikací v Pythonu. Je to open-source projekt, který nevyžaduje žádné externí závislosti a funguje na Windows, macOS i Linux. Pyglet poskytuje rozhraní pro práci s okny, grafikou, zvukem a uživatelským vstupem.

Hlavní výhody knihovny Pyglet:
- Jednoduchá instalace bez externích závislostí
- Nativní podpora pro OpenGL
- Přehrávání zvuků a hudby
- Zpracování událostí klávesnice a myši
- Načítání různých formátů obrázků a zvuků
- Podpora pro zobrazení textu a práci s fonty

## Instalace

Instalace knihovny Pyglet je velmi jednoduchá. Stačí použít správce balíčků pip:

```bash
pip install pyglet
```

Pro ověření, že instalace proběhla úspěšně, můžete spustit následující kód:

```python
import pyglet

print(f"Pyglet verze: {pyglet.version}")
```

## Vytvoření prvního okna

Začneme vytvořením jednoduchého okna. V Pygletu je to velmi snadné:

```python
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
```

Když spustíte tento kód, mělo by se objevit prázdné okno s titulkem "Moje první Pyglet okno". Okno můžete zavřít kliknutím na křížek nebo stisknutím klávesy Escape.

Pojďme přidat trochu textu do našeho okna:

```python
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
```

Tento kód vytvoří okno s textem "Ahoj, Pyglet!" uprostřed.

## Kreslení tvarů

Pyglet používá OpenGL pro vykreslování grafiky. Můžeme kreslit různé tvary pomocí primitiv OpenGL:

```python
import pyglet
from pyglet import gl

window = pyglet.window.Window(width=800, height=600, caption="Kreslení tvarů")

@window.event
def on_draw():
    window.clear()
    
    # Kreslení obdélníku
    gl.glColor3f(1.0, 0.0, 0.0)  # Červená barva (RGB)
    gl.glBegin(gl.GL_QUADS)
    gl.glVertex2f(100, 100)  # Levý dolní roh
    gl.glVertex2f(300, 100)  # Pravý dolní roh
    gl.glVertex2f(300, 300)  # Pravý horní roh
    gl.glVertex2f(100, 300)  # Levý horní roh
    gl.glEnd()
    
    # Kreslení trojúhelníku
    gl.glColor3f(0.0, 1.0, 0.0)  # Zelená barva
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glVertex2f(500, 100)  # Levý dolní roh
    gl.glVertex2f(700, 100)  # Pravý dolní roh
    gl.glVertex2f(600, 300)  # Horní vrchol
    gl.glEnd()

pyglet.app.run()
```

Tento kód vykreslí červený obdélník a zelený trojúhelník.

Pro jednodušší kreslení tvarů můžeme také použít třídu `pyglet.shapes`:

```python
import pyglet
from pyglet import shapes

window = pyglet.window.Window(width=800, height=600, caption="Kreslení tvarů")

# Vytvoření batch pro efektivní vykreslování
batch = pyglet.graphics.Batch()

# Vytvoření různých tvarů
circle = shapes.Circle(x=100, y=150, radius=50, color=(255, 0, 0), batch=batch)
rectangle = shapes.Rectangle(x=200, y=200, width=200, height=100, color=(0, 255, 0), batch=batch)
line = shapes.Line(x=400, y=100, x2=700, y2=300, width=3, color=(0, 0, 255), batch=batch)
star = shapes.Star(x=600, y=150, outer_radius=50, inner_radius=30, num_spikes=5, color=(255, 255, 0), batch=batch)

@window.event
def on_draw():
    window.clear()
    # Vykreslení všech tvarů najednou pomocí batch
    batch.draw()

pyglet.app.run()
```

## Práce s obrázky

Pyglet umožňuje snadno načítat a zobrazovat obrázky:

```python
import pyglet

window = pyglet.window.Window(width=800, height=600, caption="Práce s obrázky")

# Načtení obrázku (nahraďte 'obrazek.png' cestou k vašemu obrázku)
# Pokud nemáte vlastní obrázek, můžete použít:
# image = pyglet.resource.image('kitten.jpg')
try:
    image = pyglet.image.load('obrazek.png')
    sprite = pyglet.sprite.Sprite(image, x=window.width//2, y=window.height//2)
    # Nastavení kotvy (anchor) na střed obrázku
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2
except FileNotFoundError:
    # Pokud soubor neexistuje, vytvoříme místo něj text
    sprite = None
    label = pyglet.text.Label('Obrázek nebyl nalezen',
                              font_name='Arial',
                              font_size=24,
                              x=window.width//2, y=window.height//2,
                              anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    if sprite:
        sprite.draw()
    else:
        label.draw()

pyglet.app.run()
```

## Zpracování uživatelského vstupu

Pyglet umožňuje reagovat na události klávesnice a myši:

```python
import pyglet

window = pyglet.window.Window(width=800, height=600, caption="Zpracování uživatelského vstupu")

# Vytvoření spritu, který budeme ovládat
image = pyglet.resource.image('kitten.jpg')  # Použijte vlastní obrázek nebo tento vestavěný
sprite = pyglet.sprite.Sprite(image, x=window.width//2, y=window.height//2)
# Nastavení kotvy na střed obrázku
image.anchor_x = image.width // 2
image.anchor_y = image.height // 2

# Proměnné pro sledování stisknutých kláves
keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)

# Rychlost pohybu spritu
speed = 200  # pixelů za sekundu

# Text s instrukcemi
instructions = pyglet.text.Label('Použijte šipky pro pohyb obrázku',
                                font_name='Arial',
                                font_size=18,
                                x=10, y=window.height - 30)

@window.event
def on_draw():
    window.clear()
    instructions.draw()
    sprite.draw()

def update(dt):
    # Pohyb spritu podle stisknutých kláves
    if keys[pyglet.window.key.LEFT]:
        sprite.x -= speed * dt
    if keys[pyglet.window.key.RIGHT]:
        sprite.x += speed * dt
    if keys[pyglet.window.key.UP]:
        sprite.y += speed * dt
    if keys[pyglet.window.key.DOWN]:
        sprite.y -= speed * dt
    
    # Omezení pohybu na hranice okna
    sprite.x = max(sprite.image.width//2, min(window.width - sprite.image.width//2, sprite.x))
    sprite.y = max(sprite.image.height//2, min(window.height - sprite.image.height//2, sprite.y))

# Registrace funkce update pro pravidelné volání
pyglet.clock.schedule_interval(update, 1/60)  # 60 FPS

@window.event
def on_mouse_press(x, y, button, modifiers):
    # Přesun spritu na místo kliknutí
    if button == pyglet.window.mouse.LEFT:
        sprite.x = x
        sprite.y = y

pyglet.app.run()
```

## Přehrávání zvuků

Pyglet umožňuje přehrávat zvuky a hudbu:

```python
import pyglet

window = pyglet.window.Window(width=800, height=600, caption="Přehrávání zvuků")

# Načtení zvukového souboru (nahraďte 'zvuk.wav' cestou k vašemu zvuku)
try:
    sound = pyglet.media.load('zvuk.wav', streaming=False)
except FileNotFoundError:
    sound = None

# Vytvoření tlačítka pro přehrání zvuku
button_label = pyglet.text.Label('Přehrát zvuk',
                                font_name='Arial',
                                font_size=24,
                                x=window.width//2, y=window.height//2,
                                anchor_x='center', anchor_y='center')

# Vytvoření informačního textu
info_label = pyglet.text.Label('Klikněte na tlačítko pro přehrání zvuku',
                              font_name='Arial',
                              font_size=18,
                              x=window.width//2, y=window.height//2 - 50,
                              anchor_x='center', anchor_y='center')

if sound is None:
    info_label.text = 'Zvukový soubor nebyl nalezen'

@window.event
def on_draw():
    window.clear()
    button_label.draw()
    info_label.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    # Kontrola, zda bylo kliknuto na tlačítko
    if button == pyglet.window.mouse.LEFT:
        if (window.width//2 - 100 < x < window.width//2 + 100 and
            window.height//2 - 20 < y < window.height//2 + 20):
            if sound:
                sound.play()
                info_label.text = 'Zvuk se přehrává...'
            else:
                info_label.text = 'Zvukový soubor nebyl nalezen'

pyglet.app.run()
```

## Základy animace

Pyglet umožňuje vytvářet animace pomocí časovače a aktualizace pozic objektů:

```python
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

@window.event
def on_draw():
    window.clear()
    batch.draw()

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
```

## Jednoduchý příklad hry

Nyní vytvoříme jednoduchou hru, kde hráč ovládá postavu a sbírá objekty:

```python
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
```

## Další zdroje

Pro další studium knihovny Pyglet doporučuji následující zdroje:

1. **Oficiální dokumentace Pyglet**: https://pyglet.readthedocs.io/
2. **GitHub repozitář Pyglet**: https://github.com/pyglet/pyglet
3. **Příklady Pyglet**: https://github.com/pyglet/pyglet/tree/master/examples

### Užitečné tipy pro práci s Pyglet

1. **Používejte batch rendering** - Pro efektivní vykreslování více objektů najednou použijte `pyglet.graphics.Batch`.
2. **Správně nastavujte FPS** - Použijte `pyglet.clock.schedule_interval(update, 1/60)` pro plynulou animaci.
3. **Debugování** - Pro zobrazení FPS můžete použít `pyglet.clock.ClockDisplay()`.
4. **Správa zdrojů** - Používejte `pyglet.resource` pro načítání souborů.
5. **Správa oken** - Pyglet podporuje více oken a fullscreen režim.

### Závěr

Tímto jsme dokončili základní tutoriál knihovny Pyglet v češtině. Naučili jsme se, jak vytvořit okno, kreslit tvary a obrázky, zpracovávat uživatelský vstup, přehrávat zvuky a vytvořit jednoduchou hru.

Pyglet je velmi flexibilní knihovna, která vám umožní vytvářet 2D hry a multimediální aplikace v Pythonu. S těmito základními znalostmi můžete začít experimentovat a vytvářet vlastní projekty.

Hodně štěstí s vašimi projekty v Pygletu!