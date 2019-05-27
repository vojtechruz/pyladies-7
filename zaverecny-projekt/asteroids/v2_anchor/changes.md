# Image is positioned by its middle, not lower left corner
# Also important for rotation
# // means integer division (floor) - 5//2 is 2 but 5/2 is 2.5
image.anchor_x = image.width // 2
image.anchor_y = image.height // 2