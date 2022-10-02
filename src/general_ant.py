import numpy as np
from src.cell import CellShape

# Square ant


class SquareAnt:
    def __init__(self, x, y, orientation, state, state_count, moves):
        self.pos = np.array([x, y])
        self.orientation = orientation
        self.orientation_count = int(CellShape.SQUARE)
        self.vel = np.zeros([])
        self.state = state
        self.state_count = state_count
        self.moves = moves

    def turn(self, grid):

        cell = grid.get_current_cell(self.pos[0], self.pos[1])
        grid.modified.append(cell)

        action = self.moves[self.state][cell.state]

        # Rotation in degrees
        if action[1] == "A":
            self.orientation += 1
        elif action[1] == "B":
            self.orientation -= 1
        elif action[1] == "C":
            self.orientation += 2

        if self.orientation < 0:
            self.orientation += self.orientation_count

        if self.orientation >= self.orientation_count:
            self.orientation -= self.orientation_count

        print("or " + str(self.orientation))
        print("move " + str(self.moves[self.state][cell.state]))

        # Change the state of the cell and the ant
        cell.state += action[2]
        if cell.state >= grid.state_count:
            cell.state -= grid.state_count
        self.state += action[0]
        if self.state >= self.state_count:
            self.state -= self.state_count

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

        # Move and loop around the map if needed
        self.turn(grid)
        self.apply_turn()
        new_pos = np.add(self.pos, self.vel)
        new_pos %= grid.width - 1
        self.pos = new_pos
        print("POS = " + str(self.pos))
