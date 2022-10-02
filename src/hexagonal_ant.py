# Fourmie de Langton sur une grille hexagonale, donc avec 6 orientation possible

# Classic: 6, "D", "F", "E", "B", "E", "B"
# Super-spiral: 7, "A", "B", "F", "C", "B", "A", "E"
# Circular: 6, "E", "F", "F", "D", "E", "D"
# Spiral growth: 7, "D", "E", "F", "C", "E", "D", "B"
# Complex highway: 5, "B", "E", "B", "B", "B"
# Labyrinth: 3, "D", "B", "D"

# Islands: 10, ['F', 'D', 'D', 'C', 'A', 'F', 'F', 'E', 'A', 'A']
# Fractal-like: 10, ['C', 'C', 'F', 'D', 'B', 'D', 'F', 'C', 'C', 'C']

import numpy as np
import random
import pygame
from src.cell import CellShape
from src.grid import Grid

pygame.font.init()

WIN_WIDTH = 800
WIN_HEIGHT = 800
RANDOM = False

# Either A (60 clockwise), B (120 clockwise), C (180), D (60 counter-clockwise), E (120 counter-clockwise), F (0)
STATES = 7
LEGAL_MOVES = ["A", "B", "C", "D", "E", "F"]
POSSIBLES_MOVES = []

if RANDOM:
    for i in range(STATES):
        POSSIBLES_MOVES.append(LEGAL_MOVES[random.randint(0, 5)])
    print(POSSIBLES_MOVES)

else:
    POSSIBLES_MOVES = ["A", "B", "F", "C", "B", "A", "E"]

GRID_WIDTH = 100
GRID_HEIGHT = 100
ANT_START_X = GRID_WIDTH / 2
ANT_START_Y = GRID_HEIGHT / 2
CELL_DIMENSIONS = WIN_WIDTH / GRID_WIDTH

# COLOR_SCHEMES
ANT_COLOR = (255, 0, 0)
WHITE = (255, 255, 255)

STRENGTHS = []
for color in range(STATES):
    STRENGTHS.append(1 / (STATES - 1) * color)

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

    def turn(self, grid):

        cell = grid.get_current_cell(self.pos[0], self.pos[1])
        grid.modified.append(cell)

        if POSSIBLES_MOVES[cell.state] == "A":
            self.orientation += 1
        elif POSSIBLES_MOVES[cell.state] == "B":
            self.orientation += 2
        elif POSSIBLES_MOVES[cell.state] == "C":
            self.orientation += 3
        elif POSSIBLES_MOVES[cell.state] == "D":
            self.orientation -= 1
        elif POSSIBLES_MOVES[cell.state] == "E":
            self.orientation -= 2

        if self.orientation < 0:
            self.orientation += 6

        if self.orientation >= 6:
            self.orientation -= 6

        cell.state += 1
        if cell.state >= STATES:
            cell.state = 0

    def apply_turn(self):

        offset = self.pos[1] % 2

        if self.orientation == 0:
            self.vel = ([offset, 1])
        if self.orientation == 1:
            self.vel = ([offset - 1, 1])
        if self.orientation == 2:
            self.vel = ([-1, 0])
        if self.orientation == 3:
            self.vel = ([offset - 1, -1])
        if self.orientation == 4:
            self.vel = ([offset, -1])
        if self.orientation == 5:
            self.vel = ([1, 0])

    def move(self, grid):

        self.turn(grid)
        self.apply_turn()
        new_pos = np.add(self.pos, self.vel)
        new_pos %= GRID_WIDTH - 1

        self.pos = new_pos


def main():
    ant = Ant(ANT_START_X, ANT_START_Y)
    grid = Grid(CELL_DIMENSIONS, GRID_WIDTH, GRID_HEIGHT, CellShape.HEX)
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    score = 0

    running = True
    while running:

        #pygame.time.wait(10)

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
