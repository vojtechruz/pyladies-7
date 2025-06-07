import pyglet, random

batch = pyglet.graphics.Batch()
okno = pyglet.window.Window()
smer = 0
rychlost = 100
rychlost_strely = 400
rychlost_nepratel = 50
strely = []
nepratele = []
zivoty = 3
skore = 0
exploze_castice = []
barvy_nepratel = [ (208, 192, 80),  (80, 208, 112),(241, 79, 80),]

@okno.event
def on_draw():
    okno.clear()
    batch.draw()

@okno.event
def on_key_press(klavesa, modifikator):
    global smer

    if zivoty == 0:
        return

    if klavesa == pyglet.window.key.SPACE:
        strel()
    elif klavesa == pyglet.window.key.LEFT:
        smer = -1
    elif klavesa == pyglet.window.key.RIGHT:
        smer = 1


def spocitej_kolize(dt):
    global skore

    for strela in strely:
        for nepritel in nepratele:
            if abs(strela.x - nepritel.x) <= nepritel.width//2 and abs(strela.y - nepritel.y) <= nepritel.height//2:
                strely.remove(strela)
                strela.delete()
                vytvor_explozi(nepritel.x, nepritel.y, nepritel.barva)
                nepratele.remove(nepritel)
                nepritel.delete()
                skore += 1
                aktualizuj_zivoty_a_skore()

def vytvor_explozi(x, y, color):
    num_particles = 50

    for _ in range(num_particles):
        particle = pyglet.shapes.Rectangle(
            x=x, y=y,
            width=5, height=5,
            color=color,
            batch=batch
        )

        particle.dx = random.uniform(-200, 200)
        particle.dy = random.uniform(-200, 200)

        particle.rotation_speed = random.uniform(-360, 360)
        particle.rotation = 0

        exploze_castice.append(particle)

def pohni_exploze(dt):
    for particle in list(exploze_castice):
        particle.x += particle.dx * dt
        particle.y += particle.dy * dt

        # Add some gravity effect
        particle.dy -= 500 * dt  # Gravity

        # Rotate particle
        particle.rotation += particle.rotation_speed * dt

        if (particle.y < -50 or particle.x < -50 or
                particle.x > okno.width + 50):
            exploze_castice.remove(particle)
            particle.delete()


def tick(dt):
    pohni_hrace(dt)
    pohni_strely(dt)
    pohni_nepratele(dt)
    spocitej_kolize(dt)
    pohni_exploze(dt)


def pohni_hrace(dt):
    global rychlost
    hrac.x += smer * rychlost * dt
    if smer == 0:
        rychlost = 100
    else:
        rychlost += 1
    if hrac.x < 0:
        hrac.x = 0
        rychlost = 100
    elif hrac.x > okno.width - hrac.width:
        hrac.x = okno.width - hrac.width
        rychlost = 100


def konec_hry():
    game_over_label.visible = True
    pyglet.clock.unschedule(tick)
    pyglet.clock.unschedule(pridej_nepritele)



def aktualizuj_zivoty_a_skore():
    zivoty_label.text = f"Zivoty: {zivoty} Skore: {skore}"


def pohni_nepratele(dt):
    global zivoty

    for nepritel in nepratele:
        nepritel.y -= rychlost_nepratel * dt

        if nepritel.y < hrac.height:

            zivoty -= 1
            aktualizuj_zivoty_a_skore()
            if zivoty == 0:
                konec_hry()
                break
            vytvor_explozi(nepritel.x, nepritel.y, nepritel.barva)
            nepratele.remove(nepritel)
            nepritel.delete()


def pohni_strely(dt):
    for strela in strely:
        strela.y += rychlost_strely * dt

        if strela.y > okno.height:
            strely.remove(strela)
            strela.delete()


def strel():
    strela = pyglet.shapes.Rectangle(x=hrac.x + hrac.width //2, y=hrac.height+5, width=5, height=20, color=(255, 0, 0), batch=batch)
    strela.anchor_x = strela.width // 2
    strela.anchor_y = strela.height // 2
    strela.rotation = 0
    strely.append(strela)

def pridej_nepritele(dt):
    cislo_nepritele = random.randint(1, 3)
    nepritel_obrazek = pyglet.resource.image(f'nepritel_{cislo_nepritele}.png')
    nepritel_obrazek.anchor_x = nepritel_obrazek.width // 2
    nepritel_obrazek.anchor_y = nepritel_obrazek.height // 2
    nepritel = pyglet.sprite.Sprite(nepritel_obrazek, x=random.randint(nepritel_obrazek.width//2,okno.width- nepritel_obrazek.width), y=okno.height - nepritel_obrazek.height-50, batch=batch)
    nepritel.barva = barvy_nepratel[cislo_nepritele-1]
    nepratele.append(nepritel)

hrac_obrazek = pyglet.resource.image('player.png')
hrac = pyglet.sprite.Sprite(hrac_obrazek, x=okno.width // 2, y=0, batch=batch)

game_over_label = pyglet.text.Label('KONEC HRY',
                                    font_name='Arial',
                                    font_size=36,
                                    x=okno.width//2,
                                    y=okno.height//2,
                                    anchor_x='center',
                                    anchor_y='center',
                                    batch=batch)
zivoty_label = pyglet.text.Label('Zivoty',
                                    font_name='Arial',
                                    font_size=12,
                                    x=okno.width//2,
                                    y=okno.height-20,
                                    anchor_x='center',
                                    batch=batch)

game_over_label.visible = False
aktualizuj_zivoty_a_skore()

pyglet.clock.schedule_interval(tick, 1/60)
pyglet.clock.schedule_interval(pridej_nepritele, 1)

pyglet.app.run()









