import pyglet

snake_image = pyglet.image.load('snake.png')
snake_sprite = pyglet.sprite.Sprite(snake_image)
last_key_pressed = pyglet.window.key.RIGHT


def key_pressed(symbol, modifiers):
    # Without global keyword python would create new
    # local variable inside this function
    global last_key_pressed
    last_key_pressed = symbol


def draw_snake():
    # Clear contents of the window, delete everything
    window.clear()
    # Draw snake.
    # The position is lower-left corner if not specified otherwise
    snake_sprite.draw()

def tick(time_elapsed):
   # Every time this is called, move the snake

   if(last_key_pressed == pyglet.window.key.UP):
       print("Going UP!")
       snake_sprite.y=snake_sprite.y+1
   elif(last_key_pressed == pyglet.window.key.DOWN):
       print("Going DOWN")
       snake_sprite.y=snake_sprite.y-1
   elif(last_key_pressed == pyglet.window.key.LEFT):
       print("Going LEFT")
       snake_sprite.x=snake_sprite.x-1
   elif(last_key_pressed == pyglet.window.key.RIGHT):
       print("Going RIGHT")
       snake_sprite.x=snake_sprite.x+1

pyglet.clock.schedule_interval(tick, 1/30)

window = pyglet.window.Window()
# Every time we need to redraw (for example when minimalizing and then
# maximizing the app window), function draw_snake will be called
window.push_handlers(on_draw=draw_snake, on_key_press=key_pressed)
pyglet.app.run()