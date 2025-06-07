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