import numpy as np
import pygame
from src.cell import Cell, CellShape


class Grid:
    def __init__(self, dims: float, width: int, height: int, state_count: int, shapes: CellShape):
        self.width = width
        self.height = height
        self.nodes = self.get_grid(dims, shapes)
        self.state_count = state_count
        self.modified = []

    def modify_cell(self, cell: Cell):
        if cell not in self.modified:
            self.modified.append(cell)

    def get_grid(self, dims: float, shape: CellShape):
        nodes = []

        for row in range(self.width):
            for col in range(self.height):
                cell = Cell(dims, row, col, shape)
                nodes.append(cell)

        return np.array(nodes)

    def get_current_cell(self, row: int, col: int):
        return self.nodes[int(row) * int(self.width) + int(col)]

    def clear(self):
        for cell in self.nodes:
            if cell.state != 0:
                cell.state = 0
                self.modify_cell(cell)

    def render(self, win: pygame.display, color_scheme: list):
        """ Render the necessary cells in the grid """
        cell_with_ant = None
        for i in range(len(self.modified)):

            cell = self.modified[i]
            vertices = cell.vertices()

            if i == len(self.modified) - 1:
                pygame.draw.polygon(win, (255, 0, 0),
                                    vertices)
                cell_with_ant = cell
            else:
                pygame.draw.polygon(win, color_scheme[cell.state],
                                    vertices)

        pygame.display.update()
        self.modified.clear()
        self.modified.append(cell_with_ant)
