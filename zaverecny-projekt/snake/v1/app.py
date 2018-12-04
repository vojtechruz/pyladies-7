from board import Board
import pyglet

TILE_SIZE = 10


def key_pressed(symbol, modifiers):
    if symbol == pyglet.window.key.UP:
        board.direction = (0, 1)
    elif symbol == pyglet.window.key.DOWN:
        board.direction = (0, -1)
    elif symbol == pyglet.window.key.LEFT:
        board.direction = (-1, 0)
    elif symbol == pyglet.window.key.RIGHT:
        board.direction = (1, 0)


def draw():
    # Clear contents of the window, delete everything
    window.clear()
    # Draw snake tile by tile
    green_image = pyglet.image.load('green.png')
    for x, y in board.snake:
        green_image.blit(x * TILE_SIZE, y * TILE_SIZE, width=TILE_SIZE, height=TILE_SIZE)


def tick(time_elapsed):
    board.move()


board = Board()

window = pyglet.window.Window()
window.push_handlers(on_draw=draw, on_key_press=key_pressed)
# Snake moves ever y 1/4 of second
pyglet.clock.schedule_interval(tick, 1 / 4)
pyglet.app.run()