# NEW: Added food  and growing when eating

from board import Board
import pyglet

TILE_SIZE = 10


def key_pressed(symbol, modifiers):
    # Without global keyword python would create new
    # local variable inside this function

    global board

    if symbol == pyglet.window.key.UP:
        board.change_direction(0, 1)
    elif symbol == pyglet.window.key.DOWN:
        board.change_direction(0, -1)
    elif symbol == pyglet.window.key.LEFT:
        board.change_direction(-1, 0)
    elif symbol == pyglet.window.key.RIGHT:
        board.change_direction(1, 0)


def draw():
    # Clear contents of the window, delete everything
    window.clear()

    # Draw snake tile by tile
    green_image = pyglet.image.load('green.png')
    for x, y in board.snake:
        green_image.blit(x * TILE_SIZE, y * TILE_SIZE, width=TILE_SIZE, height=TILE_SIZE)

    # Draw each food
    red_image = pyglet.image.load('red.png')
    for x, y in board.food:
        red_image.blit(x * TILE_SIZE, y * TILE_SIZE, width=TILE_SIZE, height=TILE_SIZE)


def tick(time_elapsed):
    board.move()


board = Board()

window = pyglet.window.Window()
window.push_handlers(on_draw=draw, on_key_press=key_pressed)
pyglet.clock.schedule_interval(tick, 1 / 4)
pyglet.app.run()
