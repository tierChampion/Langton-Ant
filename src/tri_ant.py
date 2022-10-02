import numpy as np
import random
import pygame
from src.cell import CellShape
from src.grid import Grid

# Planes: 10,
# ['A', 'B', 'B', 'A', 'A', 'A', 'C', 'A', 'B', 'C']

# Alternating: 10,
# ['C', 'B', 'A', 'A', 'C', 'B', 'A', 'C', 'A', 'B']


pygame.font.init()

WIN_WIDTH = 800
WIN_HEIGHT = 800
RANDOM = True

# Either A (60 clockwise), B (60 counter-clockwise), C (0)
STATES = 10
LEGAL_MOVES = ["A", "B", "C"]
POSSIBLES_MOVES = []

if RANDOM:
    for i in range(STATES):
        POSSIBLES_MOVES.append(LEGAL_MOVES[random.randint(0, 2)])
    print(POSSIBLES_MOVES)

else:
    POSSIBLES_MOVES = ["D", "B", "D"]

GRID_WIDTH = 50
GRID_HEIGHT = 50
ANT_START_X = GRID_WIDTH / 2
ANT_START_Y = GRID_HEIGHT / 2
CELL_DIMENSIONS = WIN_HEIGHT / GRID_HEIGHT

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

        if self.orientation < 0:
            self.orientation += 3

        if self.orientation >= 3:
            self.orientation -= 3

        cell.state += 1
        if cell.state >= STATES:
            cell.state = 0

    def apply_turn(self):

        flipped = -2 * ((self.pos[0] + self.pos[1]) % 2) + 1

        if self.orientation == 0:
            self.vel = ([1, 0])
        elif self.orientation == 1:
            self.vel = ([0, flipped])
        elif self.orientation == 2:
            self.vel = ([-1, 0])

    def move(self, grid):

        self.turn(grid)
        self.apply_turn()
        new_pos = np.add(self.pos, self.vel)
        new_pos %= GRID_WIDTH - 1

        self.pos = new_pos


def main():
    ant = Ant(ANT_START_X, ANT_START_Y)
    grid = Grid(CELL_DIMENSIONS, GRID_WIDTH, GRID_HEIGHT, CellShape.TRI)
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ant.move(grid)
        score += 1

        size_of_step = 40
        if score % size_of_step == 0:
            pygame.display.set_caption("Trianglular Langton Ant | Iteration " + str(score))
            grid.render(win, COLOR_SCHEME)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
