import numpy as np
import pygame
from src.cell import Cell


class Grid:
    def __init__(self, dims, width, height, state_count, shapes):
        self.width = width
        self.height = height
        self.nodes = self.get_grid(dims, shapes)
        self.state_count = state_count
        self.modified = []

    def modify_cell(self, cell):
        if not cell  in self.modified:
            self.modified.append(cell)

    def get_grid(self, dims, shape):
        nodes = []

        for row in range(self.width):
            current_row = []
            for col in range(self.height):
                cell = Cell(dims, row, col, shape)
                current_row.append(cell)
            nodes.append(current_row)

        return np.array(nodes)

    def get_current_cell(self, row, col):
        return self.nodes[int(row), int(col)]

    def render(self, win: pygame.display, color_scheme: list):
        """ Render the necessary cells in the grid """
        for cell in self.modified:
            vertices = cell.vertices()

            pygame.draw.polygon(win, color_scheme[cell.state],
                                vertices)

        pygame.display.update()
        self.modified.clear()
