# Fourmie de Langton sur une grille hexagonale, donc avec 6 orientation possible

# Classic: 6, "D", "F", "E", "B", "E", "B"
# Super-spiral: 7, "A", "B", "F", "C", "B", "A", "E"
# Circular: 6, "E", "F", "F", "D", "E", "D"
# Spiral growth: 7, "D", "E", "F", "C", "E", "D", "B"
# Complex highway: 5, "B", "E", "B", "B", "B"
# Labyrinth: 3, "D", "B", "D"

# Islands: 10, ['F', 'D', 'D', 'C', 'A', 'F', 'F', 'E', 'A', 'A']
# Fractal-like: 10, ['C', 'C', 'F', 'D', 'B', 'D', 'F', 'C', 'C', 'C']

# [[[0, 'F', 12], [2, 'A', 1], [0, 'B', 4], [2, 'D', 3], [0, 'A', 11], [1, 'D', 7], [0, 'D', 4],
# [1, 'E', 12], [1, 'B', 4], [1, 'F', 4], [2, 'A', 10], [1, 'E', 8], [1, 'D', 5], [2, 'C', 10], [0, 'F', 9]],
# [[0, 'D', 2], [0, 'F', 9], [1, 'A', 5], [1, 'D', 11], [0, 'C', 3], [2, 'B', 4], [2, 'D', 12],
# [2, 'C', 12], [2, 'D', 14], [1, 'F', 1], [1, 'E', 4], [2, 'A', 10], [0, 'E', 9], [0, 'E', 5], [2, 'C', 4]],
# [[0, 'B', 14], [0, 'B', 3], [1, 'E', 14], [0, 'B', 14], [2, 'F', 5], [0, 'C', 7], [2, 'A', 4],
# [0, 'F', 14], [2, 'D', 4], [0, 'B', 14], [2, 'D', 13], [0, 'F', 13], [2, 'D', 3], [0, 'C', 10], [0, 'B', 1]]]

# [[[1, 'D', 1], [1, 'F', 1], [1, 'D', 2], [1, 'D', 2]], [[0, 'C', 2], [1, 'E', 1], [1, 'E', 1], [0, 'E', 2]]]

# [[[1, 'A', 1], [1, 'E', 1], [1, 'E', 1], [1, 'A', 3]], [[1, 'C', 1], [1, 'A', 3], [0, 'C', 1], [0, 'A', 3]]]

# [[[1, 'A', 3], [0, 'A', 2], [0, 'B', 1], [1, 'C', 1]], [[0, 'F', 3], [1, 'E', 1], [1, 'A', 1], [0, 'E', 1]]]

# [[[1, 'C', 1], [1, 'C', 1], [1, 'C', 1], [0, 'F', 2]], [[1, 'C', 2], [1, 'A', 1], [0, 'D', 2], [0, 'A', 1]]]

# [[[1, 'E', 2], [1, 'A', 1], [1, 'B', 2], [0, 'A', 1]], [[0, 'F', 2], [1, 'F', 3], [0, 'F', 3], [0, 'E', 2]]]

# [[[0, 'B', 2], [0, 'B', 3], [1, 'B', 3], [0, 'E', 3]], [[0, 'B', 3], [0, 'D', 3], [1, 'E', 2], [0, 'E', 2]]]

# HEX BUILDER:
# [[[0, 'E', 2], [1, 'F', 1], [0, 'B', 2], [0, 'C', 1]],
# [[0, 'E', 3], [0, 'A', 3], [1, 'F', 3], [1, 'A', 1]]]

# Filled Spiral:
# [[[1, 'E', 1], [1, 'C', 2], [0, 'D', 1], [0, 'C', 2]], [[0, 'F', 2], [0, 'A', 2], [1, 'F', 3], [1, 'B', 3]]]

# Spider web:
# [[[1, 'C', 1], [0, 'F', 1], [1, 'F', 3], [1, 'D', 1]], [[1, 'C', 2], [1, 'C', 2], [1, 'C', 3], [0, 'C', 2]]]

# Triple fill:
# [[[0, 'F', 2], [1, 'C', 3], [0, 'F', 3], [0, 'B', 3]], [[0, 'D', 3], [0, 'F', 3], [0, 'F', 3], [1, 'B', 1]]]

# Double Binary ant:
# [[[1, 'C', 2], [1, 'C', 1], [1, 'B', 3], [1, 'F', 2]], [[1, 'E', 2], [0, 'E', 3], [0, 'B', 2], [0, 'F', 3]]]

# Single binary ant:
# [[[0, 'C', 3], [0, 'F', 3], [0, 'C', 1], [0, 'F', 2]], [[1, 'B', 3], [0, 'D', 2], [0, 'E', 1], [1, 'E', 2]]]

# Loops:
# [[[0, 'D', 3], [0, 'F', 2], [1, 'F', 3], [1, 'D', 1]], [[1, 'D', 2], [0, 'E', 1], [0, 'D', 3], [1, 'A', 2]]]


import numpy as np
import random
import pygame
from src.cell import CellShape
from src.grid import Grid
from src.general_ant import HexAnt

pygame.font.init()

WIN_WIDTH = 800
WIN_HEIGHT = 800
RANDOM = True
NORMAL = False

# Either A (60 clockwise), B (120 clockwise), C (180), D (60 counter-clockwise), E (120 counter-clockwise), F (0)
STATES = 2
ANT_STATES = 1 if NORMAL else STATES
CELL_STATES = 4
LEGAL_MOVES = ["A", "B", "C", "D", "E", "F"]
POSSIBLES_MOVES = []

if RANDOM:
    for i in range(ANT_STATES):
        POSSIBLES_MOVES.append([])
        for j in range(CELL_STATES):
            POSSIBLES_MOVES[i].append([random.randint(1, ANT_STATES) - 1,
                                       LEGAL_MOVES[random.randint(0, 5)],
                                       1 if NORMAL else random.randint(1, CELL_STATES - 1)])
    print(POSSIBLES_MOVES)

else:
    POSSIBLES_MOVES = [[[0, "F", 1], [0, "F", 1], [0, "F", 1], [1, "F", 1]],
                       [[0, "B", 1], [1, "A", 3], [0, "E", 1], [1, "A", 2]]]

GRID_WIDTH = 100
GRID_HEIGHT = 100
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


def main():
    ant = HexAnt(ANT_START_X, ANT_START_Y, 0, 0, ANT_STATES, POSSIBLES_MOVES)
    grid = Grid(CELL_DIMENSIONS, GRID_WIDTH, GRID_HEIGHT, CELL_STATES, CellShape.HEX)
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    score = 0

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ant.move(grid)
        score += 1

        size_of_step = 1
        if score % size_of_step == 0:
            pygame.display.set_caption("Hexagonal Langton Ant | Iteration " + str(score))
            grid.render(win, COLOR_SCHEME)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
