from operator import abs

import pyglet
import random

okno = pyglet.window.Window()
smer = "doprava"
rychlost_hada = 100

def prekresli():
    okno.clear()
    sprite.draw()
    sprite_jablko.draw()

def tik(cas):
    pohni_hadem(cas)

    if sprite.x > okno.width:
        sprite.x = sprite.width //2

    if sprite.y > okno.height + sprite.height //2:
        sprite.y = sprite.height //2


def klavesa_stisknuta(klavesa, modifikator):
    global smer

    if klavesa == pyglet.window.key.LEFT:
        smer = "doleva"
    elif klavesa == pyglet.window.key.RIGHT:
        smer = "doprava"
    elif klavesa == pyglet.window.key.UP:
        smer = "nahoru"
    elif klavesa == pyglet.window.key.DOWN:
        smer = "dolu"

def pohni_hadem(cas):
    if smer == "doprava":
        sprite.x = sprite.x + 1 * rychlost_hada * cas
    if smer == "doleva":
        sprite.x = sprite.x - 1 * rychlost_hada * cas
    if smer == "nahoru":
        sprite.y = sprite.y + 1 * rychlost_hada * cas
    if smer == "dolu":
        sprite.y = sprite.y - 1 * rychlost_hada * cas


    if abs(sprite.x - sprite_jablko.x)  < 100 and (abs(sprite.y - sprite_jablko.y)):
        sprite_jablko.x = random.randint(0, okno.width)
        sprite_jablko.y = random.randint(0, okno.height)

okno.push_handlers(on_draw=prekresli, on_key_press=klavesa_stisknuta)

obrazek = pyglet.image.load("had.png")
obrazek.anchor_x = obrazek.width // 2
obrazek.anchor_y = obrazek.height // 2
sprite = pyglet.sprite.Sprite(obrazek, obrazek.width //2,obrazek.height //2)

obrazek_jablko = pyglet.image.load("jablko.png")
sprite_jablko = pyglet.sprite.Sprite(obrazek_jablko, 500, 500)
sprite_jablko.width = 100
sprite_jablko.height = 100

pyglet.clock.schedule_interval(tik, 1/30)



pyglet.app.run()