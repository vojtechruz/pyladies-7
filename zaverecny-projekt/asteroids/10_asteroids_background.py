import pyglet
window = pyglet.window.Window()
image = pyglet.image.load('assets/Backgrounds/purple.png')
background = pyglet.image.TileableTexture.create_for_image(image)

def on_draw():
    window.clear()

    background.blit_tiled(0, 0, 0, window.width, window.height)

window.push_handlers(on_draw=on_draw)
pyglet.app.run()