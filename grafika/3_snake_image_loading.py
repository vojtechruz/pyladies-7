import pyglet

def draw_snake():
    # Clear contents of the window, delete everything
    window.clear()
    # Draw snake.
    # The position is lower-left corner if not specified otherwise
    snake_sprite.draw()


window = pyglet.window.Window()
snake_image = pyglet.image.load('snake.png')
snake_sprite = pyglet.sprite.Sprite(snake_image)
# Every time we need to redraw (for example when minimalizing and then
# maximizing the app window), function draw_snake will be called
window.push_handlers(on_draw=draw_snake)
pyglet.app.run()