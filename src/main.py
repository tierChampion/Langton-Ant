import pygame
import random
from src.cell import CellShape
from src.grid import Grid
from src.rule import Rule, to_rules
from src.general_ant import TriTurmite, SquareTurmite, HexTurmite

WIN_WIDTH = 800
WIN_HEIGHT = 800
STEP_SIZE = 10
COLONY_SIZE = 1
SHAPE = CellShape.SQUARE
RANDOM = True
NORMAL = False
LEGAL_RULES = ["A", "B", "C", "D", "E", "F"]
TURMITE_STATES = 4
CELL_STATES = 6

GRID_WIDTH = 100
GRID_HEIGHT = 100
ANT_START_X = int(GRID_WIDTH / 2)
ANT_START_Y = int(GRID_HEIGHT / 2)
CELL_DIMENSIONS = WIN_WIDTH / GRID_WIDTH

# TODO: Check the rules if ok. comment code. Make options clearer and accessable from outside or during rendering.
# Speeding up, Restarting the simulation
# Save image of the screen

ant_states = 1 if NORMAL else TURMITE_STATES
rules = []

if not RANDOM:
    # Make sure this sequence respects the other params (size and letters)
    rules = to_rules([[[0, 'B', 1], [0, 'A', 1]]])

else:
    for i in range(ant_states):
        rules.append([])
        for j in range(CELL_STATES):
            rule = Rule(LEGAL_RULES[random.randint(0, int(SHAPE) - 1)],
                        random.randint(1, ant_states) - 1,
                        1 if NORMAL else random.randint(0, CELL_STATES - 1))

            rules[i].append(rule)


print("[")
for i in range(len(rules)):
    print("[", end="")
    for rule in rules[i]:
        print(str(rule) + ", ", end="")
    print("],")
print("]")


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
    for a in range(COLONY_SIZE):

        x = ANT_START_X
        y = ANT_START_Y

        if a > 0:
            x += random.randint(-int(GRID_WIDTH / 2) + 1, int(GRID_WIDTH / 2) - 1)
            y += random.randint(-int(GRID_HEIGHT / 2) + 1, int(GRID_HEIGHT / 2) - 1)

        if SHAPE == CellShape.SQUARE:
            colony.append(SquareTurmite(x, y, 0, ant_states, rules))
        elif SHAPE == CellShape.TRI:
            colony.append(TriTurmite(x, y, 0, ant_states, rules))
        elif SHAPE == CellShape.HEX:
            colony.append(HexTurmite(x, y, 0, ant_states, rules))

    grid = Grid(CELL_DIMENSIONS, GRID_WIDTH, GRID_HEIGHT, CELL_STATES, SHAPE)
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    score = 0

    running = True
    stopped = False

    while running:
        # Controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    stopped = not stopped

        if not stopped:
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
