import pyglet

def vykresli_hada():
    # Vyčistí obsah okna, smaže vše
    okno.clear()
    # Vykreslí hada.
    # Pozice je levý dolní roh, pokud není určeno jinak
    sprite_hada.draw()


okno = pyglet.window.Window()
obrazek_hada = pyglet.image.load('had.png')
sprite_hada = pyglet.sprite.Sprite(obrazek_hada)
# Pokaždé, když potřebujeme překreslit (například při minimalizaci a poté
# maximalizaci okna aplikace), bude volána funkce vykresli_hada
okno.push_handlers(on_draw=vykresli_hada)
pyglet.app.run()
