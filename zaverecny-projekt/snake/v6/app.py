# NEW: Better snake pictures

from board import Board
import pyglet
from pathlib import Path

TILE_SIZE = 30
WIDTH = 30
HEIGHT = 15
TILES_DIRECTORY = Path('snake-tiles')
snake_tiles = {}

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
    pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
    pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

    if board.game_over:
        label = pyglet.text.Label('GAME OVER',
                                  font_name='Times New Roman',
                                  font_size=36,
                                  x=window.width//2, y=window.height//2,
                                  anchor_x='center', anchor_y='center')
        label.draw()

    # Draw snake tile by tile
    for index, val in enumerate(board.snake):
        snake_tile_image_name = board.get_image_name(index)
        snake_tile = snake_tiles[snake_tile_image_name]
        snake_tile.blit(val[0] * TILE_SIZE, val[1] * TILE_SIZE, width=TILE_SIZE, height=TILE_SIZE)
    # Draw each food
    apple = pyglet.image.load('apple.png')
    for x, y in board.food:
        apple.blit(x * TILE_SIZE, y * TILE_SIZE, width=TILE_SIZE, height=TILE_SIZE)


def tick(time_elapsed):
    board.move()


board = Board(WIDTH, HEIGHT)

window = pyglet.window.Window(WIDTH*TILE_SIZE, HEIGHT*TILE_SIZE)
window.push_handlers(on_draw=draw, on_key_press=key_pressed)
pyglet.clock.schedule_interval(tick, 1 / 6)

for path in TILES_DIRECTORY.glob('*.png'):
    snake_tiles[path.stem] = pyglet.image.load(path)

pyglet.app.run()
