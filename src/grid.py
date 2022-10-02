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

    def render(self, win, color_scheme):
        # Redraw the grid. Only do so with modified cells
        to_redraw = None
        counter = 0
        for node in self.modified:

            vertices = node.vertices()

            if counter == len(self.modified) - 1:
                pygame.draw.polygon(win, color_scheme[0],
                                    vertices)
                counter += 1
                to_redraw = node
            else:
                pygame.draw.polygon(win, color_scheme[node.state + 1],
                                    vertices)
                counter += 1

        pygame.display.update()
        self.modified.clear()
        self.modified.append(to_redraw)