import random


class Board:

    def __init__(self, width, height):
        self.snake = [(0, 0), (1, 0), (2, 0)]
        self.direction = (1, 0)
        self.width = width
        self.height = height
        self.food = []
        self.add_food()
        self.add_food()
        self.add_food()

    def move(self):
        current_x = self.snake[-1][0]
        current_y = self.snake[-1][1]
        new_x = current_x + self.direction[0]
        new_y = current_y + self.direction[1]
        self.snake.append((new_x, new_y))
        if (self.snake[-1] in self.food):
            self.food.remove(self.snake[-1])
            self.add_food()
        else:
            self.snake.pop(0)

    def change_direction(self, new_x, new_y):
        old_x, old_y = self.direction
        # Now snake cannot move in the opposite direction than the original
        if (old_x, old_y) != (-new_x, -new_y):
            self.direction = (new_x, new_y)

    def add_food(self):
        for try_number in range(100):
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            position = x, y
            if (position not in self.snake) and (position not in self.food):
                self.food.append(position)
                return
