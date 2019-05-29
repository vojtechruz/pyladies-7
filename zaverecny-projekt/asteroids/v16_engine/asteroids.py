import pyglet
from spaceship import Spaceship
from asteroid import Asteroid
from pyglet import gl
import random

WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280
ASTEROID_COUNT = 4
ASTEROID_MIN_SPEED = 10
ASTEROID_MAX_SPEED = 50

objects = []
keys_pressed = set()
window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT)
game_over = False
batch = pyglet.graphics.Batch()
background_image = pyglet.image.load('../assets/Backgrounds/darkPurple.png')
background = pyglet.image.TileableTexture.create_for_image(background_image)

def init_spaceship():
    spaceship = Spaceship(batch)
    spaceship.x = window.width/2
    spaceship.y = window.height/2

    objects.append(spaceship)

def init_asteroids():
    for i in range(ASTEROID_COUNT):
        asteroid = Asteroid(batch)
        position = random.choice([0,1])
        if position == 0:
            asteroid.x = random.randint(0, window.width)
            asteroid.y = random.choice([0, window.height])
        else:
            asteroid.x = random.choice([0, window.width])
            asteroid.y = random.randint(0, window.height)

        asteroid.x_speed = random.choice([-1,1]) * random.randint(ASTEROID_MIN_SPEED,ASTEROID_MAX_SPEED)
        asteroid.y_speed = random.choice([-1,1]) * random.randint(ASTEROID_MIN_SPEED,ASTEROID_MAX_SPEED)
        objects.append(asteroid)

def draw_all_objects():
    window.clear()

    background.blit_tiled(0, 0, 0, window.width, window.height)

    if(game_over):
        game_over_label = pyglet.text.Label(
            'Game Over',
            font_name='League Gothic',
            font_size=40,
            x=window.width / 2,
            y=window.height / 2,
            anchor_x='center')
        game_over_label.draw()


    for x_offset in (-window.width, 0, window.width):
        for y_offset in (-window.height, 0, window.height):
            # Remember the current state
            gl.glPushMatrix()
            # Move everything drawn from now on by (x_offset, y_offset, 0)
            gl.glTranslatef(x_offset, y_offset, 0)

            # Draw
            batch.draw()

            # Restore remembered state (this cancels the glTranslatef)
            gl.glPopMatrix()

def distance(a, b, wrap_size):
    """Distance in one direction (x or y)"""
    result = abs(a - b)
    if result > wrap_size / 2:
        result = wrap_size - result
    return result

def overlaps(a, b):
    """Returns true iff two space objects overlap"""
    distance_squared = (distance(a.x, b.x, window.width) ** 2 +
                        distance(a.y, b.y, window.height) ** 2)
    max_distance_squared = (a.radius + b.radius) ** 2

    return distance_squared < max_distance_squared - 2000

def collision(obj):

    objects[0].destroy_object()
    obj.destroy_object()
    batch.draw()

    global game_over
    game_over = True

    pyglet.clock.unschedule(tick_all_objects)

def tick_all_objects(time_elapsed):
    ship = objects[0]

    for obj in objects:
        obj.tick(time_elapsed, keys_pressed, window)
        if(obj.can_collide and overlaps(ship, obj)):
            collision(obj)

def on_key_pressed(key, modifiers):
    keys_pressed.add(key)

def on_key_released(key, modifiers):
    keys_pressed.remove(key)


init_spaceship()
init_asteroids()
window.push_handlers(
    on_draw=draw_all_objects,
    on_key_press=on_key_pressed,
    on_key_release=on_key_released
)
pyglet.clock.schedule_interval(tick_all_objects, 1/30)
# window.set_fullscreen(fullscreen=True, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
pyglet.app.run()