import numpy as np
from src.grid import Grid
from src.cell import CellShape, Cell
from abc import ABC, abstractmethod


class GeneralAnt(ABC):
    """
    N-Turmite. Langton Ant with states and n legal moves. Abstract.
    """

    def __init__(self, x: int, y: int, orientation: int, orientation_count: int, state_count: int, moves: list):
        self.pos = np.array([x, y])
        self.orientation = orientation
        self.orientation_count = orientation_count
        self.vel = np.zeros([])
        self.state = 0
        self.state_count = state_count
        self.moves = moves

    def move(self, grid: Grid):
        """ Move the ant on the grid """

        self.turn(grid)
        self.apply_turn()
        new_pos = np.add(self.pos, self.vel)
        new_pos %= grid.width - 1
        self.pos = new_pos

    def clamp_orientation(self):
        """ Limit orientation to possible values """

        if self.orientation < 0:
            self.orientation += self.orientation_count

        if self.orientation >= self.orientation_count:
            self.orientation -= self.orientation_count

    def update_states(self, cell: Cell, grid: Grid, action: list):
        """ Update the ant and cell states """

        cell.state += action[2]
        if cell.state >= grid.state_count:
            cell.state -= grid.state_count
        self.state += action[0]
        if self.state >= self.state_count:
            self.state -= self.state_count

    @abstractmethod
    def turn(self, grid: Grid):
        """ Change the orientation of the ant """
        pass

    @abstractmethod
    def apply_turn(self):
        """ Set the velocity of the ant to the proper orientation """
        pass


class TriAnt(GeneralAnt):
    """ 3-Turmite. Move along a grid of isosceles triangles. Has states and 3 legal moves. """

    def __init__(self, x: int, y: int, orientation: int, state_count: int, moves: list):
        super().__init__(x, y, orientation, int(CellShape.TRI), state_count, moves)

    def turn(self, grid):

        cell = grid.get_current_cell(self.pos[0], self.pos[1])
        grid.modify_cell(cell)

        action = self.moves[self.state][cell.state]

        # Rotation in degrees
        if action[1] == "A":
            self.orientation += 1
        elif action[1] == "B":
            self.orientation += 2

        self.clamp_orientation()

        self.update_states(cell, grid, action)

    def apply_turn(self):
        flipped = -2 * ((self.pos[0] + self.pos[1]) % 2) + 1

        if self.orientation == 0:
            self.vel = ([1, 0])
        elif self.orientation == 1:
            self.vel = ([0, flipped])
        elif self.orientation == 2:
            self.vel = ([-1, 0])


class SquareAnt(GeneralAnt):
    """ 4-Turmite. Move along a grid of squares. Has states and 4 legal moves. """

    def __init__(self, x: int, y: int, orientation: int, state_count: int, moves: list):
        super().__init__(x, y, orientation, int(CellShape.SQUARE), state_count, moves)

    def turn(self, grid):

        cell = grid.get_current_cell(self.pos[0], self.pos[1])
        grid.modify_cell(cell)

        action = self.moves[self.state][cell.state]

        # Rotation in degrees
        if action[1] == "A":
            self.orientation += 1
        elif action[1] == "B":
            self.orientation -= 1
        elif action[1] == "C":
            self.orientation += 2

        self.clamp_orientation()

        self.update_states(cell, grid, action)

    def apply_turn(self):
        if self.orientation == 0:
            self.vel = [0, 1]
        elif self.orientation == 1:
            self.vel = [-1, 0]
        elif self.orientation == 2:
            self.vel = [0, -1]
        elif self.orientation == 3:
            self.vel = [1, 0]


class HexAnt(GeneralAnt):
    """ 6-Turmite. Move along a grid of hexagons. Has states and 6 legal moves. """

    def __init__(self, x, y, orientation, state_count, moves):
        super().__init__(x, y, orientation, int(CellShape.HEX), state_count, moves)

    def turn(self, grid):

        cell = grid.get_current_cell(self.pos[0], self.pos[1])
        grid.modify_cell(cell)

        action = self.moves[self.state][cell.state]

        # Rotation in degrees
        if action[1] == "A":
            self.orientation += 1
        elif action[1] == "B":
            self.orientation += 2
        elif action[1] == "C":
            self.orientation += 3
        elif action[1] == "D":
            self.orientation -= 1
        elif action[1] == "E":
            self.orientation -= 2

        self.clamp_orientation()

        self.update_states(cell, grid, action)

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
