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
        self.show_tongue = False
        self.game_over = False

    def move(self):
        if (self.game_over):
            return

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

        self.check_snake_eats_itself()
        self.check_snake_exits_board()
        self.show_tongue = not self.show_tongue

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

    def check_snake_eats_itself(self):
        if (self.snake[-1] in self.snake[:-1]):
            self.game_over = True

    def check_snake_exits_board(self):
        x, y = self.snake[-1]
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            self.game_over = True

    def get_image_name(self, index):

        if index == 0:
            name_prev = "tail"
        else:
            name_prev = self.get_relative_position(index, index-1)

        if index == len(self.snake) - 1:
            if self.game_over:
                name_next = "dead"
            elif self.show_tongue:
                name_next = "tongue"
            else:
                name_next = "tongue"
        else:
            name_next = self.get_relative_position(index, index + 1)

        return name_prev + "-" + name_next

    def get_relative_position(self, index1, index2):
        x1, y1 = self.snake[index1]
        x2, y2 = self.snake[index2]

        if x1 == x2 and y1 == y2 - 1:
            return "top"
        if x1 == x2 and y1 == y2 + 1:
            return "bottom"
        if x1 == x2 - 1 and y1 == y2:
            return "right"
        if x1 == x2 + 1 and y1 == y2:
            return "left"
