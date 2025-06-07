import pyglet


def vykresli_hada():
    # Vyčistí obsah okna, smaže vše
    okno.clear()
    # Vykreslí hada.
    # Pozice je levý dolní roh, pokud není určeno jinak
    sprite_hada.draw()

def tik(uplynuly_cas):
   # Pokaždé, když je tato funkce volána, posune hada
   # o jeden pixel doprava
   sprite_hada.x = sprite_hada.x+1


okno = pyglet.window.Window()

obrazek_hada = pyglet.image.load('had.png')
sprite_hada = pyglet.sprite.Sprite(obrazek_hada)

pyglet.clock.schedule_interval(tik, 1/30)


# Pokaždé, když potřebujeme překreslit (například při minimalizaci a poté
# maximalizaci okna aplikace), bude volána funkce vykresli_hada
okno.push_handlers(on_draw=vykresli_hada)
pyglet.app.run()
