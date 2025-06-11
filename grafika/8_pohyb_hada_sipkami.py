import pyglet



def stisknuta_klavesa(symbol, modifikatory):
    # Bez klíčového slova global by python vytvořil novou
    # lokální proměnnou uvnitř této funkce
    global posledni_stisknuta_klavesa
    posledni_stisknuta_klavesa = symbol


def vykresli_hada():
    # Vyčistí obsah okna, smaže vše
    okno.clear()
    # Vykreslí hada.
    # Pozice je levý dolní roh, pokud není určeno jinak
    sprite_hada.draw()

def tik(uplynuly_cas):
   # Pokaždé, když je tato funkce volána, posune hada

   if posledni_stisknuta_klavesa == pyglet.window.key.UP:
       print("Jdu NAHORU!")
       sprite_hada.y=sprite_hada.y+1
   elif posledni_stisknuta_klavesa == pyglet.window.key.DOWN:
       print("Jdu DOLŮ")
       sprite_hada.y=sprite_hada.y-1
   elif posledni_stisknuta_klavesa == pyglet.window.key.LEFT:
       print("Jdu DOLEVA")
       sprite_hada.x=sprite_hada.x-1
   elif posledni_stisknuta_klavesa == pyglet.window.key.RIGHT:
       print("Jdu DOPRAVA")
       sprite_hada.x=sprite_hada.x+1



pyglet.clock.schedule_interval(tik, 1/30)

okno = pyglet.window.Window()

obrazek_hada = pyglet.image.load('had.png')
sprite_hada = pyglet.sprite.Sprite(obrazek_hada)
posledni_stisknuta_klavesa = pyglet.window.key.RIGHT


# Pokaždé, když potřebujeme překreslit (například při minimalizaci a poté
# maximalizaci okna aplikace), bude volána funkce vykresli_hada
okno.push_handlers(on_draw=vykresli_hada, on_key_press=stisknuta_klavesa)
pyglet.app.run()

# Dokumentace k ovládání klávesnice v pyglet
# https://pyglet.readthedocs.io/en/latest/programming_guide/keyboard.html