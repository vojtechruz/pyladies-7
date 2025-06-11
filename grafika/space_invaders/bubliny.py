import pyglet, random

window = pyglet.window.Window()

batch = pyglet.graphics.Batch()
shapes = []




@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_mouse_motion(x, y, dx, dy):
    circle = pyglet.shapes.Circle(x,y, random.randint(0,25), color=(random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(100,255)),batch=batch)
    circle.rychlostx = random.uniform(-100, 100)  # rychlost v ose x
    circle.rychlosty = random.uniform(-100, 100)  # rychlost v ose y
    shapes.append(circle)


def update(x):
    for circle in shapes:
        circle.x += circle.rychlostx*x
        circle.y += circle.rychlosty*x
        barva_puvodni = circle.color
        alfa = barva_puvodni[3]

        alfa -= 5

        barva_puvodni = (barva_puvodni[0], barva_puvodni[1], barva_puvodni[2], alfa)
        circle.color = barva_puvodni

        circle.radius += 30 * x  # Scale the radius reduction by time delta and adjust speed
        if alfa <= 0 or circle.radius <= 0:  # Add radius check
            shapes.remove(circle)
            circle.delete()



pyglet.clock.schedule_interval(update, 1/60)

pyglet.app.run()