import random

import pygame
from enum import Enum

class PlayingField:

    def __init__(self, dimension):
        self.dimension = dimension

        self.fields = None
        self.snake = None
        self.food = None
        self.snake_length = 4
        self.score = 0
        self.snake_grow = False
        self.direction = Direction.RIGHT

        self.createPlayingField()
        self.createSnake()


    def createPlayingField(self):
        fields = [[0 for x in range(self.dimension)] for y in range(self.dimension)]

        for xPos in range(self.dimension):
            for yPos in range(self.dimension):
                fields[xPos][yPos] = SingleField(xPos, yPos, FieldState.OFF)

        self.fields = fields

    def createSnake(self):
        starting_pos_x = int(self.dimension / 2)
        starting_pos_y = int(self.dimension / 2)

        self.snake = []

        for i in range(self.snake_length):
            self.snake.append(SingleField(starting_pos_x - i, starting_pos_y, FieldState.SNAKE))


        self.drawSnakeOnField()

    def drawSnakeOnField(self):
        for field in self.snake:
            self.fields[field.x_pos][field.y_pos] = field

    def drawFoodOnField(self):
        self.fields[self.food.x_pos][self.food.y_pos] = self.food

    def moveSnakeOne(self):
        current_head = self.snake[0]

        new_head = SingleField(
            (current_head.x_pos + self.direction.value[0]) % self.dimension,
            (current_head.y_pos + self.direction.value[1]) % self.dimension,
            FieldState.SNAKE
        )

        if self.snake_grow is True:
            self.snake_grow = False
        else:
            to_delete = self.snake.pop()
            self.fields[to_delete.x_pos][to_delete.y_pos].setState(FieldState.OFF)


        for field in self.snake:
            if field.x_pos == new_head.x_pos:
                if field.y_pos == new_head.y_pos:
                    return True  # Schlange trifft sich selbst

        self.snake.insert(0, new_head)

        self.drawSnakeOnField()

        if self.food is not None:
            if new_head.x_pos is self.food.x_pos:
                if new_head.y_pos is self.food.y_pos:
                    self.snake_grow = True
                    self.score += 1

        return False

    def spawnFood(self):
        food_x = None
        food_y = None
        on_snake = True

        while on_snake:

            food_x = random.randint(0, self.dimension - 1)
            food_y = random.randint(0, self.dimension - 1)

            on_snake = False
            for field in self.snake:
                if field.x_pos == food_x:
                    if field.y_pos == food_y:
                        on_snake = True

        self.food = SingleField(food_x, food_y, FieldState.FOOD)

        self.drawFoodOnField()



    def setDirection(self, direction):
        if direction is direction.LEFT:
            if self.direction is not direction.RIGHT:
                self.direction = direction
        elif direction is direction.RIGHT:
            if self.direction is not direction.LEFT:
                self.direction = direction
        elif direction is direction.UP:
            if self.direction is not direction.DOWN:
                self.direction = direction
        elif direction is direction.DOWN:
            if self.direction is not direction.UP:
                self.direction = direction

    def getCurrentPlayingField(self):
        return self.fields

class SingleField:

    def __init__(self, x_pos, y_pos, state):
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.rect = pygame.Rect((x_pos * 30, y_pos * 30, 30, 30))
        self.field_state = state

    def getXPos(self):
        return self.x_pos

    def getYPos(self):
        return self.y_pos

    def getStateAsColor(self):
        return self.field_state.value

    def setState(self, state):
        self.field_state = state


class Theme(Enum):
    DARK = (24, 25, 36)
    BACKGROUND = (57, 58, 85)
    YELLOW = (255, 204, 0)
    GREEN = (0, 255, 83)

class FieldState(Enum):
    OFF = Theme.BACKGROUND.value
    SNAKE = Theme.YELLOW.value
    FOOD = Theme.GREEN.value

class Direction(Enum):
    RIGHT = (1, 0)
    LEFT = (-1, 0)
    UP = (0, -1)
    DOWN = (0, 1)



