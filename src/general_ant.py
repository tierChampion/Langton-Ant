import numpy as np
from src.grid import Grid
from src.cell import CellShape, Cell
from src.rule import Rule
from abc import ABC, abstractmethod


class GeneralTurmite(ABC):
    """
    N-Turmite. Langton Ant with states and n legal moves. Abstract.
    """

    def __init__(self, x: int, y: int, orientation: int, orientation_count: int, state_count: int, rules: list):
        self.pos = np.array([x, y])
        self.orientation = orientation
        self.orientation_count = orientation_count
        self.vel = np.zeros([])
        self.state = 0
        self.state_count = state_count
        self.rule_set = rules

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

    def update_states(self, cell: Cell, grid: Grid, rule: Rule):
        """ Update the ant and cell states """

        cell.state += rule.d_cell
        if cell.state >= grid.state_count:
            cell.state -= grid.state_count
        self.state += rule.d_turmite
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


class TriTurmite(GeneralTurmite):
    """ 3-Turmite. Move along a grid of isosceles triangles. Has states and 3 legal moves. """

    def __init__(self, x: int, y: int, orientation: int, state_count: int, rules: list):
        super().__init__(x, y, orientation, int(CellShape.TRI), state_count, rules)

    def turn(self, grid: Grid):

        cell = grid.get_current_cell(self.pos[0], self.pos[1])
        grid.modify_cell(cell)

        rule = self.rule_set[self.state][cell.state]

        # Left
        if rule.move == "A":
            self.orientation += 1
        # Right
        elif rule.move == "B":
            self.orientation += 2

        self.clamp_orientation()
        self.update_states(cell, grid, rule)

    def apply_turn(self):
        flipped = -2 * ((self.pos[0] + self.pos[1]) % 2) + 1

        # Check if ok (flipped the sides)

        # Right side
        if self.orientation == 0:
            self.vel = ([flipped, 0])
        # Base
        elif self.orientation == 1:
            self.vel = ([0, flipped])
        # Left side
        elif self.orientation == 2:
            self.vel = ([-flipped, 0])


class SquareTurmite(GeneralTurmite):
    """ 4-Turmite. Move along a grid of squares. Has states and 4 legal moves. """

    def __init__(self, x: int, y: int, orientation: int, state_count: int, rules: list):
        super().__init__(x, y, orientation, int(CellShape.SQUARE), state_count, rules)

    def turn(self, grid: Grid):

        cell = grid.get_current_cell(self.pos[0], self.pos[1])
        grid.modify_cell(cell)

        rule = self.rule_set[self.state][cell.state]

        # Left
        if rule.move == "A":
            self.orientation += 1
        # Right
        elif rule.move == "B":
            self.orientation -= 1
        # U-turn
        elif rule.move == "C":
            self.orientation += 2

        self.clamp_orientation()
        self.update_states(cell, grid, rule)

    def apply_turn(self):

        # Up
        if self.orientation == 0:
            self.vel = [0, 1]
        # Left
        elif self.orientation == 1:
            self.vel = [-1, 0]
        # Down
        elif self.orientation == 2:
            self.vel = [0, -1]
        # Right
        elif self.orientation == 3:
            self.vel = [1, 0]


class HexTurmite(GeneralTurmite):
    """ 6-Turmite. Move along a grid of hexagons. Has states and 6 legal moves. """

    def __init__(self, x: int, y: int, orientation: int, state_count: int, rules: list):
        super().__init__(x, y, orientation, int(CellShape.HEX), state_count, rules)

    def turn(self, grid: Grid):

        cell = grid.get_current_cell(self.pos[0], self.pos[1])
        grid.modify_cell(cell)

        rule = self.rule_set[self.state][cell.state]

        # 1x Clockwise
        if rule.move == "A":
            self.orientation += 1
        # 2x Clockwise
        elif rule.move == "B":
            self.orientation += 2
        # 3x Clockwise
        elif rule.move == "C":
            self.orientation += 3
        # 1x Counter-clockwise
        elif rule.move == "D":
            self.orientation -= 1
        # 2x Counter-clockwise
        elif rule.move == "E":
            self.orientation -= 2

        self.clamp_orientation()
        self.update_states(cell, grid, rule)

    def apply_turn(self):

        offset = self.pos[1] % 2

        # Up left
        if self.orientation == 0:
            self.vel = ([offset, 1])
        # Up right
        if self.orientation == 1:
            self.vel = ([offset - 1, 1])
        # Right
        if self.orientation == 2:
            self.vel = ([-1, 0])
        # Down right
        if self.orientation == 3:
            self.vel = ([offset - 1, -1])
        # Down left
        if self.orientation == 4:
            self.vel = ([offset, -1])
        # Left
        if self.orientation == 5:
            self.vel = ([1, 0])
