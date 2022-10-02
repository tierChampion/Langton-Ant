import numpy as np
import random
import pygame
from src.cell import CellShape
from src.grid import Grid
from src.general_ant import TriAnt

# Planes: 10,
# ['A', 'B', 'B', 'A', 'A', 'A', 'C', 'A', 'B', 'C']

# Alternating: 10,
# ['C', 'B', 'A', 'A', 'C', 'B', 'A', 'C', 'A', 'B']

# ['C', 'B', 'C', 'B']

# ["A", "A", "B", "B"]

# ["C", "B", "C", "A"]

# ['B', 'C', 'A', 'C', 'B', 'B']


pygame.font.init()

WIN_WIDTH = 800
WIN_HEIGHT = 800
RANDOM = True
NORMAL = True

# Either A (60 clockwise), B (60 counter-clockwise), C (0)
STATES = 4
ANT_STATES = 1 if NORMAL else STATES
CELL_STATES = 10
LEGAL_MOVES = ["A", "B", "C"]
POSSIBLES_MOVES = []

if RANDOM:
    for i in range(ANT_STATES):
        POSSIBLES_MOVES.append([])
        for j in range(CELL_STATES):
            POSSIBLES_MOVES[i].append([random.randint(1, ANT_STATES) - 1,
                                       LEGAL_MOVES[random.randint(0, 2)],
                                       1 if NORMAL else random.randint(1, CELL_STATES - 1)])
    print(POSSIBLES_MOVES)

else:
    POSSIBLES_MOVES = [[[0, 'B', 1], [0, 'C', 1], [0, 'A', 1], [0, 'C', 1], [0, 'B', 1], [0, 'B', 1]]]

GRID_WIDTH = 200
GRID_HEIGHT = 200
ANT_START_X = GRID_WIDTH / 2
ANT_START_Y = GRID_HEIGHT / 2
CELL_DIMENSIONS = WIN_HEIGHT / GRID_HEIGHT

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
    ant = TriAnt(ANT_START_X, ANT_START_Y, 0, 0, ANT_STATES, POSSIBLES_MOVES)
    grid = Grid(CELL_DIMENSIONS, GRID_WIDTH, GRID_HEIGHT, CELL_STATES, CellShape.TRI)
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
            pygame.display.set_caption("Trianglular Langton Ant | Iteration " + str(score))
            grid.render(win, COLOR_SCHEME)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
