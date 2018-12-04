class Board:

    def __init__(self):
        self.snake = [(0, 0), (1, 0), (2,0)]
        self.direction = (1,0)


    def move(self):
        current_x = self.snake[-1][0]
        current_y = self.snake[-1][1]
        new_x = current_x + self.direction[0]
        new_y = current_y + self.direction[1]
        self.snake.append((new_x, new_y))
        self.snake.pop(0)

    def change_direction(self, new_x, new_y):
        old_x, old_y = self.direction
        # Now snake cannot move in the opposite direction than the original
        if (old_x, old_y) != (-new_x, -new_y):
            self.direction = (new_x, new_y)