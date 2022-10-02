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

# TODO
# Make the auto generator remove stopping sims as much as possible [0, x, 0] as first arg leeds to hard lock
# Have only one main with maybe menus in the pygame or a command line arg
# Comment the code more

import numpy as np
import pygame
import random
from src.cell import CellShape
from src.grid import Grid
from src.general_ant import SquareAnt

pygame.font.init()

WIN_WIDTH = 800
WIN_HEIGHT = 800

RANDOM = False
LEGAL_MOVES = ["A", "B", "C", "D"]
ANT_STATES = 2
CELL_STATES = 2
POSSIBLE_MOVES = []

if not RANDOM:
    POSSIBLE_MOVES = [[[0, 'B', 0], [1, 'A', 0]], [[0, 'A', 1], [1, 'C', 1]]]
else:
    for i in range(ANT_STATES):
        POSSIBLE_MOVES.append([])
        for j in range(CELL_STATES):
            POSSIBLE_MOVES[i].append([random.randint(0, ANT_STATES - 1),
                                      LEGAL_MOVES[random.randint(0, len(LEGAL_MOVES) - 1)],
                                      random.randint(0, CELL_STATES - 1)])
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
        pygame.time.wait(2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ant.move(grid)
        score += 1

        # Only render every x amount of steps
        size_of_step = 1
        if score % size_of_step == 0:
            pygame.display.set_caption("Standard Langton Ant | Iteration " + str(score))
            grid.render(win, COLOR_SCHEME)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
