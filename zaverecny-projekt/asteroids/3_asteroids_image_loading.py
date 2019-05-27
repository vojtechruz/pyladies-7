import pyglet

spaceship_image = pyglet.image.load('assets/PNG/playerShip1_blue.png')
spaceship_sprite = pyglet.sprite.Sprite(spaceship_image)

def draw_spaceship():
    # Clear contents of the window, delete everything
    window.clear()
    # Draw spaceship.
    # The position is lower-left corner if not specified otherwise
    spaceship_sprite.draw()


window = pyglet.window.Window()
# Every time we need to redraw (for example when minimalizing and then
# maximizing the app window), function draw_spaceship will be called
window.push_handlers(on_draw=draw_spaceship)
pyglet.app.run()