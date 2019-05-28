We created a set with all the keys which are currently pressed and not yet released

keys_pressed = set()

Whenever a key is pressed, we add it to the set


def on_key_pressed(key, modifiers):
    keys_pressed.add(key)

And when it is released, we remove it:

def on_key_released(key, modifiers):
    keys_pressed.remove(key)

Then we just need to make sure these functions are called when keyboard 
events are triggered:

window.push_handlers(
    on_draw=draw_all_objects,
    on_key_press=on_key_pressed,
    on_key_release=on_key_released
)