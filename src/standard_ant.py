# La fourmie de langton est une intelligence artificiel tres simple qui se deplace sur une grille
# Sur les cases blanches, elle tourne a droite et sur les cases noires, elle tourne a gauche
# Elle change la couleur de la case ou elle viens de tourner
# Vers environ 11 000 iterations, elle se met tourner a l'infini, ce qui s' appelle le 'highway'

# NORMAL: 2, "B", "A"
# CHAOS: 3, "B", "A", "B"
# Symmetric: 4, "A", "A", "B", "B"
# 3, ['B', 'B', 'A']
# Square: 9, "A", "B", "B", "B", "B", "B", "A", "A", "B"
# Triangle: 12, "B", "B", "A", "A", "A", "B", "A", "A", "A", "B", "B", "B"
# Weird Highway: 12, "A", "A", "B", "B", "B", "A", "B", "A", "B", "A", "A", "B"
# Multi-Highway: 4, "A", "B", "C", "D"
# Network: 12, "D", "B", "C", "D", "A", "A", "D", "C", "B", "B", "C", "A"
# Closing-doors: 30, 'D', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'D', 'A', 'B', 'B', 'D', 'A', 'B', 'D',
# 'D', 'D', 'A', 'D', 'A', 'A', 'D', 'A', 'B', 'B', 'B'

# [[[1, 'D', 1], [1, 'A', 0]], [[1, 'B', 0], [1, 'C', 1]]]

# A(L) B(R) C(U) D(0)

# [[[8, 'B', 3], [9, 'B', 3], [6, 'D', 6], [0, 'B', 9], [3, 'A', 6],
# [2, 'A', 2], [8, 'B', 3], [6, 'C', 0], [3, 'A', 6], [8, 'A', 6]],
# [[2, 'D', 9], [9, 'D', 1], [5, 'C', 9], [1, 'B', 1], [7, 'D', 8],
# [1, 'B', 8], [8, 'B', 6], [3, 'A', 6], [4, 'B', 7], [0, 'A', 8]],
# [[0, 'A', 7], [4, 'D', 0], [3, 'C', 1], [2, 'D', 2], [3, 'D', 5],
# [7, 'C', 0], [3, 'D', 0], [8, 'A', 2], [3, 'A', 5], [8, 'C', 9]],
# [[9, 'C', 5], [5, 'B', 1], [6, 'D', 5], [6, 'B', 1], [3, 'B', 5],
# [3, 'D', 4], [7, 'B', 3], [3, 'D', 8], [0, 'C', 3], [8, 'A', 1]],
# [[9, 'B', 7], [2, 'C', 0], [4, 'A', 6], [9, 'A', 0], [7, 'B', 1],
# [4, 'D', 8], [2, 'B', 8], [0, 'B', 7], [9, 'B', 1], [1, 'C', 0]],
# [[8, 'C', 1], [2, 'A', 0], [6, 'B', 1], [8, 'A', 7], [6, 'D', 0],
# [4, 'D', 2], [2, 'C', 2], [1, 'A', 4], [1, 'D', 4], [4, 'A', 1]],
# [[1, 'B', 6], [9, 'A', 9], [4, 'A', 0], [6, 'C', 3], [9, 'B', 3],
# [0, 'A', 1], [1, 'D', 6], [0, 'A', 3], [5, 'B', 6], [0, 'D', 9]],
# [[0, 'A', 7], [1, 'B', 0], [9, 'D', 1], [1, 'A', 6], [1, 'A', 7],
# [8, 'A', 9], [7, 'B', 4], [8, 'D', 8], [9, 'A', 4], [7, 'C', 0]],
# [[8, 'B', 2], [7, 'B', 1], [2, 'D', 1], [9, 'A', 9], [7, 'B', 6],
# [6, 'B', 6], [5, 'C', 2], [8, 'C', 9], [9, 'A', 3], [7, 'B', 5]],
# [[0, 'D', 6], [3, 'B', 2], [9, 'B', 4], [8, 'C', 3], [5, 'A', 1],
# [7, 'D', 0], [6, 'C', 0], [3, 'C', 7], [7, 'C', 3], [7, 'C', 7]]]

# [[[0, 'A', 1], [0, 'D', 1], [2, 'C', 2]],
# [[1, 'B', 0], [2, 'D', 0], [0, 'D', 0]],
# [[2, 'C', 1], [1, 'D', 1], [0, 'D', 0]]]

# TODO
# Merge all ants in one file. Comment the code

import numpy as np
import pygame
import random
from src.cell import CellShape
from src.grid import Grid
from src.general_ant import SquareAnt

pygame.font.init()

WIN_WIDTH = 800
WIN_HEIGHT = 800

RANDOM = True
NORMAL = False
LEGAL_MOVES = ["A", "B", "C", "D"]
SUPER_STATES = 3
ANT_STATES = 1 if NORMAL else SUPER_STATES
CELL_STATES = 3
POSSIBLE_MOVES = []

if not RANDOM:
    POSSIBLE_MOVES = [[[0, 'D', 1], [0, 'A', 1]]]
else:
    for i in range(ANT_STATES):
        POSSIBLE_MOVES.append([])
        for j in range(CELL_STATES):
            POSSIBLE_MOVES[i].append([random.randint(1, ANT_STATES) - 1,
                                      LEGAL_MOVES[random.randint(0, len(LEGAL_MOVES) - 1)],
                                      1 if NORMAL else random.randint(0, CELL_STATES - 1)])
    print(POSSIBLE_MOVES)

GRID_WIDTH = 200
GRID_HEIGHT = 200
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
    ant = SquareAnt(ANT_START_X, ANT_START_Y, 0, 0, ANT_STATES, POSSIBLE_MOVES)
    grid = Grid(CELL_DIMENSIONS, GRID_WIDTH, GRID_HEIGHT, CELL_STATES, CellShape.SQUARE)
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ant.move(grid)
        score += 1

        # Only render every x amount of steps
        size_of_step = 100
        if score % size_of_step == 0:
            pygame.display.set_caption("Standard Langton Ant | Iteration " + str(score))
            grid.render(win, COLOR_SCHEME)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
