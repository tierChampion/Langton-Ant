import pygame
import random
from src.cell import CellShape
from src.grid import Grid
from src.general_ant import TriAnt, SquareAnt, HexAnt

WIN_WIDTH = 800
WIN_HEIGHT = 800
STEP_SIZE = 100
COLONY_SIZE = 1
SHAPE = CellShape.HEX
RANDOM = True
NORMAL = False
LEGAL_RULES = ["A", "B", "C", "D", "E", "F"]
TURMITE_STATES = 3
CELL_STATES = 5

GRID_WIDTH = 250
GRID_HEIGHT = 250
ANT_START_X = int(GRID_WIDTH / 2)
ANT_START_Y = int(GRID_HEIGHT / 2)
CELL_DIMENSIONS = WIN_WIDTH / GRID_WIDTH

# TODO: Check the rules if ok. comment code. Make options clearer and accessable from outside or during rendering.
# Stopping, resuming, speeding up, restarting the simulation

ant_states = 1 if NORMAL else TURMITE_STATES
rules = []

if not RANDOM:
    # Make sure this sequence respects the other params (size and letters)
    rules = [[[0, 'D', 1], [0, 'A', 1], [0, 'A', 1], [0, 'C', 1], [0, 'C', 1]]]

else:
    for i in range(ant_states):
        rules.append([])
        for j in range(CELL_STATES):
            rules[i].append([random.randint(1, ant_states) - 1,
                             LEGAL_RULES[random.randint(0, int(SHAPE) - 1)],
                             1 if NORMAL else random.randint(0, CELL_STATES - 1)])
    print(rules)

STRENGTHS = []
for color in range(CELL_STATES):
    STRENGTHS.append(1 / (CELL_STATES - 1) * color)

COLOR_SCHEME = []
for color in range(CELL_STATES):
    strength = 1 / (CELL_STATES - 1) * color
    value = int(255 * strength)
    COLOR_SCHEME.append((value, value, value))


def main():
    colony = []
    for i in range(COLONY_SIZE):

        x = ANT_START_X
        y = ANT_START_Y

        if i > 0:
            x += random.randint(-int(GRID_WIDTH / 2) + 1, int(GRID_WIDTH / 2) - 1)
            y += random.randint(-int(GRID_HEIGHT / 2) + 1, int(GRID_HEIGHT / 2) - 1)

        if SHAPE == CellShape.SQUARE:
            colony.append(SquareAnt(x, y, 0, ant_states, rules))
        elif SHAPE == CellShape.TRI:
            colony.append(TriAnt(x, y, 0, ant_states, rules))
        elif SHAPE == CellShape.HEX:
            colony.append(HexAnt(x, y, 0, ant_states, rules))

    grid = Grid(CELL_DIMENSIONS, GRID_WIDTH, GRID_HEIGHT, CELL_STATES, SHAPE)
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for ant in colony:
            ant.move(grid)

        score += 1

        # Only render every x amount of steps
        if score % STEP_SIZE == 0:
            pygame.display.set_caption("Langton Ant | Iteration " + str(score))
            grid.render(win, COLOR_SCHEME)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
