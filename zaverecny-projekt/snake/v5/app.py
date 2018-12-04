# NEW: Game over when snake hits itself or exists board

from board import Board
import pyglet

TILE_SIZE = 10
WIDTH = 96
HEIGHT = 48

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

    if board.game_over:
        label = pyglet.text.Label('GAME OVER',
                                  font_name='Times New Roman',
                                  font_size=36,
                                  x=window.width//2, y=window.height//2,
                                  anchor_x='center', anchor_y='center')
        label.draw()

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


board = Board(WIDTH, HEIGHT)

window = pyglet.window.Window(WIDTH*TILE_SIZE, HEIGHT*TILE_SIZE)
window.push_handlers(on_draw=draw, on_key_press=key_pressed)
pyglet.clock.schedule_interval(tick, 1 / 6)
pyglet.app.run()
