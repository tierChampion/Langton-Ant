# Super ant or TURMITES where the ant also has a state

# Fibonnaci Spiral: 2, 2, [[1, "L", 1], [1, "L", 0]], [[0, "R", 1], [1, "N", 1]]
# Symmetric lines: 2, 2, [[1, "N", 1], [1, "L", 1]], [[0, "R", 1], [1, "N", 1]]
# Magic pyramid: 2, 2, [[1, "N", 1], [0, "L", 1]], [[0, "R", 1], [1, "N", 1]]
# Snail Shell: 2, 2, [[1, "R", 0], [0, "L", 1]], [[0, "L", 1], [1, "R", 1]]
# Spiral: 2, 2, [[1, "N", 1], [0, "L", 0]], [[0, "R", 1], [1, "N", 1]]
# Diagonal:
# 7, 8, [[5, 'N', 7], [0, 'N', 3], [2, 'N', 5], [5, 'N', 3], [4, 'R', 3], [2, 'R', 1], [2, 'N', 4], [3, 'R', 3]],
# [[6, 'N', 0], [4, 'N', 5], [6, 'L', 3], [1, 'R', 2], [5, 'N', 4], [3, 'N', 7], [2, 'L', 7], [3, 'R', 3]],
# [[1, 'N', 3], [5, 'R', 1], [2, 'N', 0], [6, 'L', 7], [6, 'L', 7], [6, 'R', 5], [5, 'L', 5], [4, 'L', 6]],
# [[4, 'R', 6], [6, 'N', 6], [2, 'L', 7], [0, 'N', 0], [3, 'L', 4], [0, 'L', 5], [5, 'R', 2], [1, 'N', 0]],
# [[6, 'N', 0], [5, 'R', 0], [5, 'L', 0], [3, 'R', 6], [3, 'L', 1], [0, 'R', 6], [3, 'R', 1], [6, 'R', 4]],
# [[2, 'R', 2], [6, 'R', 4], [2, 'L', 4], [5, 'L', 6], [5, 'L', 5], [3, 'R', 1], [0, 'R', 3], [2, 'L', 3]],
# [[2, 'R', 7], [4, 'L', 2], [3, 'R', 6], [5, 'L', 1], [4, 'L', 3], [4, 'L', 2], [4, 'L', 4], [6, 'L', 6]]
# Stuck: 8, 3 [[3, 'N', 0], [1, 'N', 1], [0, 'L', 2]], [[4, 'R', 2], [6, 'L', 2], [6, 'L', 2]],
# [[2, 'L', 1], [0, 'L', 2], [7, 'L', 0]], [[2, 'L', 2], [2, 'R', 0], [1, 'L', 1]],
# [[4, 'R', 1], [3, 'R', 2], [7, 'R', 0]], [[7, 'R', 0], [6, 'L', 1], [0, 'R', 1]],
# [[7, 'N', 1], [6, 'L', 1], [0, 'R', 1]], [[7, 'L', 0], [4, 'N', 1], [4, 'L', 0]]

# Panda face: 3, 7, [[[0, 'R', 6], [0, 'N', 1], [2, 'L', 3], [2, 'L', 3], [2, 'R', 2], [2, 'L', 1], [2, 'R', 0]],
# [[0, 'L', 3], [0, 'L', 4], [1, 'N', 1], # [2, 'N', 0], [0, 'R', 2], [1, 'L', 0], [2, 'R', 2]],
# [[2, 'N', 5], [1, 'L', 5], [0, 'N', 0], [0, 'N', 6], [0, 'L', 1], [2, 'L', 4], [1, 'R', 4]]]

# Big plane 9, 9
# [
# [[8, 'R', 7], [2, 'R', 2], [8, 'N', 0], [6, 'L', 1], [8, 'L', 2], [5, 'N', 6], [1, 'L', 1], [4, 'N', 1], [1, 'L', 6]],
# [[0, 'N', 7], [5, 'L', 7], [4, 'R', 3], [5, 'R', 4], [3, 'L', 5], [2, 'N', 5], [3, 'N', 7], [8, 'N', 0], [8, 'L', 3]],
# [[3, 'L', 2], [7, 'N', 7], [5, 'R', 4], [3, 'R', 0], [3, 'N', 4], [8, 'N', 3], [6, 'L', 3], [2, 'N', 1], [1, 'L', 3]],
# [[0, 'R', 5], [6, 'N', 5], [7, 'R', 5], [0, 'N', 0], [1, 'R', 5], [4, 'N', 8], [7, 'R', 5], [2, 'N', 2], [1, 'N', 0]],
# [[3, 'L', 2], [6, 'L', 6], [2, 'L', 2], [2, 'R', 2], [1, 'R', 8], [0, 'L', 0], [1, 'R', 2], [4, 'L', 6], [3, 'R', 5]],
# [[2, 'N', 0], [7, 'L', 2], [3, 'N', 1], [1, 'L', 1], [3, 'R', 4], [6, 'L', 0], [5, 'L', 8], [6, 'N', 6], [0, 'R', 6]],
# [[7, 'L', 5], [1, 'N', 1], [6, 'N', 1], [2, 'N', 5], [1, 'L', 8], [4, 'R', 7], [3, 'R', 5], [6, 'L', 3], [6, 'L', 7]],
# [[6, 'N', 5], [3, 'N', 3], [0, 'N', 2], [8, 'N', 2], [8, 'N', 2], [0, 'R', 3], [8, 'N', 6], [1, 'L', 4], [1, 'N', 8]],
# [[7, 'L', 3], [7, 'L', 1], [0, 'N', 1], [4, 'N', 5], [2, 'L', 1], [3, 'N', 4], [3, 'L', 0], [6, 'R', 0], [7, 'N', 4]]
# ]

# Windows 9, 9
# [
# [[1, 'N', 6], [8, 'L', 0], [5, 'N', 2], [3, 'L', 7], [3, 'R', 6], [2, 'R', 1], [6, 'L', 5], [6, 'N', 1], [8, 'R', 5]],
# [[2, 'L', 5], [3, 'L', 7], [0, 'L', 2], [4, 'R', 3], [7, 'N', 2], [4, 'L', 0], [5, 'N', 0], [5, 'L', 2], [8, 'N', 5]],
# [[5, 'L', 3], [1, 'R', 2], [0, 'R', 7], [5, 'R', 6], [8, 'N', 6], [2, 'N', 0], [2, 'N', 8], [6, 'N', 5], [3, 'R', 8]],
# [[6, 'R', 4], [3, 'L', 7], [5, 'N', 0], [7, 'L', 2], [6, 'R', 0], [3, 'L', 1], [0, 'L', 8], [5, 'L', 0], [2, 'R', 3]],
# [[7, 'R', 5], [3, 'L', 4], [1, 'N', 8], [4, 'L', 0], [5, 'L', 7], [8, 'L', 4], [5, 'L', 0], [6, 'L', 0], [5, 'L', 2]],
# [[2, 'R', 4], [2, 'L', 1], [1, 'N', 5], [4, 'L', 2], [6, 'R', 4], [5, 'L', 6], [4, 'L', 2], [5, 'N', 7], [7, 'R', 2]],
# [[2, 'N', 0], [0, 'R', 5], [2, 'R', 7], [4, 'N', 4], [7, 'L', 4], [6, 'R', 6], [7, 'R', 0], [6, 'N', 2], [6, 'R', 5]],
# [[7, 'N', 0], [7, 'L', 1], [5, 'N', 7], [7, 'R', 4], [4, 'R', 1], [3, 'L', 6], [3, 'R', 4], [1, 'L', 7], [7, 'R', 6]],
# [[6, 'N', 8], [2, 'L', 7], [5, 'L', 4], [1, 'N', 1], [4, 'R', 6], [1, 'R', 0], [3, 'L', 4], [1, 'N', 4], [4, 'L', 3]]
# ]

import numpy as np
import math
import pygame
import random
from src.cell import CellShape
from src.grid import Grid

pygame.font.init()

WIN_WIDTH = 800
WIN_HEIGHT = 800
RANDOM = True

# Index: Ant state and Cell state
# Input 1: Ant state variation
# Input 2: Direction of turn
# Input 3: Cell state variation
ANT_STATES = 8
CELL_STATES = 7
LEGAL_MOVES = ['R', 'L', 'N', 'U']
POSSIBLES_MOVES = [[[7, 'N', 4], [0, 'U', 0], [5, 'U', 5], [4, 'L', 4], [2, 'R', 3], [3, 'U', 6], [6, 'U', 5]],
                   [[1, 'U', 2], [3, 'N', 1], [2, 'U', 0], [4, 'L', 1], [8, 'N', 6], [8, 'R', 6], [8, 'U', 4]],
                   [[3, 'U', 3], [7, 'N', 2], [4, 'R', 6], [3, 'N', 3], [1, 'U', 2], [4, 'N', 4], [4, 'N', 1]],
                   [[6, 'N', 4], [2, 'N', 4], [5, 'R', 1], [3, 'N', 7], [8, 'L', 5], [6, 'R', 7], [1, 'R', 0]],
                   [[4, 'L', 7], [8, 'R', 2], [1, 'L', 0], [4, 'U', 6], [3, 'R', 0], [4, 'L', 3], [4, 'U', 4]],
                   [[2, 'U', 1], [4, 'N', 4], [4, 'L', 2], [3, 'R', 4], [7, 'U', 3], [1, 'U', 4], [8, 'N', 0]],
                   [[8, 'U', 1], [4, 'R', 3], [8, 'N', 2], [3, 'U', 0], [6, 'U', 7], [4, 'N', 6], [2, 'N', 7]],
                   [[1, 'R', 4], [0, 'U', 3], [2, 'U', 4], [3, 'R', 2], [8, 'L', 1], [6, 'U', 3], [4, 'L', 6]]]

if RANDOM:
    POSSIBLES_MOVES = []

    for i in range(ANT_STATES):
        POSSIBLES_MOVES.append([])
        for j in range(CELL_STATES):
            POSSIBLES_MOVES[i].append([random.randint(0, ANT_STATES - 1), LEGAL_MOVES[random.randrange(0, 3)],
                                       random.randint(0, CELL_STATES - 1)])
    print(POSSIBLES_MOVES)

STAT_FONT = pygame.font.SysFont("comicsans", 50)

GRID_WIDTH = 500
GRID_HEIGHT = 500
ANT_START_X = GRID_WIDTH / 2
ANT_START_Y = GRID_HEIGHT / 2
CELL_DIMENSIONS = WIN_WIDTH / GRID_WIDTH

# COLOR_SCHEMES
ANT_COLOR = (255, 0, 0)
WHITE = (255, 255, 255)

STRENGTHS = []
for color in range(CELL_STATES):
    STRENGTHS.append(1 / (CELL_STATES - 1) * color)

COLOR_SCHEME = [ANT_COLOR]
for strength in STRENGTHS:
    value = int(255 * strength)
    COLOR_SCHEME.append((value, value, value))


class Ant:
    def __init__(self, x, y):
        self.pos = np.array([x, y])
        self.orientation = 0
        self.vel = np.zeros([])
        self.color = (255, 0, 0)
        self.state = 0

    def turn(self, grid):

        cell = grid.get_current_cell(self.pos[0], self.pos[1])
        grid.modified.append(cell)

        action = POSSIBLES_MOVES[self.state][cell.state]

        if action[1] == "L":
            self.orientation += 1
        elif action[1] == "R":
            self.orientation -= 1
        elif action[1] == "U":
            self.orientation += 2

        if self.orientation < 0:
            self.orientation += 4

        if self.orientation >= 4:
            self.orientation -= 4

        cell.state += action[2]
        if cell.state >= CELL_STATES:
            cell.state -= CELL_STATES
        self.state += action[0]
        if self.state >= ANT_STATES:
            self.state -= ANT_STATES

    def apply_turn(self):
        if self.orientation == 0:
            self.vel = [0, 1]
        elif self.orientation == 1:
            self.vel = [-1, 0]
        elif self.orientation == 2:
            self.vel = [0, -1]
        elif self.orientation == 3:
            self.vel = [1, 0]

    def move(self, grid):

        self.turn(grid)
        self.apply_turn()
        new_pos = np.add(self.pos, self.vel)
        new_pos %= GRID_WIDTH - 1
        self.pos = new_pos


def main():
    ant = Ant(ANT_START_X, ANT_START_Y)
    grid = Grid(CELL_DIMENSIONS, GRID_WIDTH, GRID_HEIGHT, CELL_STATES, CellShape.SQUARE)
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    score = 0

    running = True
    while running:
        # clock.tick(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ant.move(grid)
        score += 1

        size_of_step = 20
        if score % size_of_step == 0:
            pygame.display.set_caption("Super Langton Ant | Iteration " + str(score))
            grid.render(win, COLOR_SCHEME)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
