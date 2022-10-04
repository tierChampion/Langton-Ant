import math
from enum import IntEnum


class CellShape(IntEnum):
    """ Possible Cell Shapes. Translates to the number of sides of the shape. """
    TRI = 3
    SQUARE = 4
    HEX = 6


class Cell:
    """ One cell of the grid. Carries a state represented by a color. """

    def __init__(self, dim: float, row: int, col: int, shape: CellShape):
        self.dimension = dim
        self.row = row
        self.col = col
        self.shape = shape
        self.state = 0

    def vertices(self):
        """ Calculate the vertices of the cell to render. """

        verts = []

        if self.shape == CellShape.HEX:

            radius = self.dimension / 2
            render_rad = radius * 1.25
            offset = self.col % 2
            x_offset = radius * offset

            # Offset the center of the hexagon for a tight fit
            center = (self.dimension * self.row + x_offset, self.dimension * self.col)

            # Hexagon vertices. Go around the circle for every 60 degrees.
            for i in range(int(CellShape.HEX)):
                verts.append((center[0] + math.cos(math.radians(30 + i * 60)) * render_rad,
                              center[1] + math.sin(math.radians(30 + i * 60)) * render_rad))

        elif self.shape == CellShape.SQUARE:

            # Square vertices. Arranged in clock-wise order.
            for i in range(CellShape.SQUARE):
                verts.append((self.dimension * (self.row + (i < 2)), self.dimension * (self.col + (i % 3 > 0))))

        elif self.shape == CellShape.TRI:

            flipped = (self.col + self.row) % 2

            # Triangle vertices. Move all of them by 1 to the left every triangle and flip the height.
            for i in range(int(CellShape.TRI)):
                verts.append((self.dimension * (self.row + i), self.dimension * (self.col + ((i + flipped) % 2))))

        return verts
