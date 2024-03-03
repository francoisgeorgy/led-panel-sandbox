import random
from math import sin, cos

from samplebase import SampleBase
from color import Color
import time


"""
    line eq : 
    
    ax + by + c = 0
    y = mx + b
    x = (y-b) / m
"""

EPSILON = 0.000001      # used to avoid division by zero


def fx(y, m, b):
    return (y - b) / (m + EPSILON)


def fy(x, m, b):
    return m * x + b


def get_scale_factors(dx, dy, dw, dh, zoom=1.0):
    return dw / dx * zoom, dh / dy * zoom


class App(SampleBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add additional command line options :
        self.parser.add_argument("--grid-size", help="Size of the grid in pixels", default=8)
        self.width = 0
        self.height = 0

    def rectangle(self, x, y, w, h, color, fill=False):
        if fill:
            for v in range(h):
                self.line(x, y+v, x+w-1, y+v, color)
        else:
            self.line(x, y, x+w-1, y, color)
            self.line(x+w-1, y, x+w-1, y+h-1, color)
            self.line(x, y+h-1, x+w-1, y+h-1, color)
            self.line(x, y, x, y+h-1, color)

    def draw_grid_random(self, size, positions, color):
        for (x, y) in positions:
            self.rectangle(x, y, size, size, color, fill=True)

    def get_random_positions(self, size):
        p = []
        for x in range(0, self.canvas.width, size):
            for y in range(0, self.canvas.height, size):
                if bool(random.getrandbits(1)):
                    p.append((x, y))
        return p

    def scale_and_offset(self, x, y, sx, sy, x0=0, y0=0):
        """
        Scale and offset
        :param x: value to scale
        :param y: value to scale
        :param sx: scale x
        :param sy: scale y
        :param x0: destination value for x=0
        :param y0: destination value for y=0
        :return: scaled x and y
        """
        scaled_x = int(x * sx + 0.5)
        scaled_y = int(y * sy + 0.5)
        return scaled_x + x0, self.height - (scaled_y + y0)

    def find_crossings(self, x0, y0, x1, y1, fx, fy):
        """
        Find the points where the function crosses the rectangle defined by (x0,y0) and (x1,y1)
        :param x0:
        :param y0:
        :param x1:
        :param y1:
        :return: two (x,y) points which are the crossings or None if no crossings
        """
        x_start, y_start, x_end, y_end = None, None, None, None
        x_left = x0
        y_left = fy(x_left)
        y_top = y0
        x_top = fx(y_top)
        x_right = x1
        y_right = fy(x_right)
        y_bottom = y1
        x_bottom = fx(y_bottom)
        if y0 <= y_left <= y1:
            x_start = x_left
            y_start = y_left
        if x0 <= x_top <= x1:
            if x_start is None:
                x_start = x_top
                y_start = y_top
            else:
                x_end = x_top
                y_end = y_top
        if (x_start is None or x_end is None) and (y0 <= y_right <= y1):
            if x_start is None:
                x_start = x_right
                y_start = y_right
            else:
                x_end = x_right
                y_end = y_right
        if (x_start is None or x_end is None) and (x0 <= x_bottom <= x1):
            if x_start is None:
                x_start = x_bottom
                y_start = y_bottom
            else:
                x_end = x_bottom
                y_end = y_bottom
        return x_start, y_start, x_end, y_end

    def run(self):
        grid_size = int(self.args.grid_size)
        p = self.get_random_positions(grid_size)

        # FIXME: move into setup()
        self.width = self.canvas.width - 1
        self.height = self.canvas.height - 1

        scale_x, scale_y = get_scale_factors(4.0, 2.0, 127, 63, 1.0)

        x_offset = 63
        y_offset = 31

        t = 0
        while True:
            self.clear()
            self.draw_grid_random(grid_size, p, Color.WHITE())

            m = (sin(t / 20) + cos(t / 11)) / 2
            b = sin(t / 30) / 1

            xs, ys, xe, ye = self.find_crossings(-2, -1, 2, 1, lambda y: fx(y, m, b), lambda x: fy(x, m, b))
            if xs is None or ys is None or xe is None or ye is None:
                continue

            x0, y0 = self.scale_and_offset(xs, ys, scale_x, scale_y, x_offset, y_offset)
            x1, y1 = self.scale_and_offset(xe, ye, scale_x, scale_y, x_offset, y_offset)

            self.line(x0, y0, x1, y1, Color.WHITE(), mode_xor=True)
            self.refresh()
            t = t + 1
            time.sleep(0.02)
            # if t % 50 == 0:
            #     time.sleep(2)


if __name__ == "__main__":
    s = App()
    try:
        s.setup()
        s.run()
    except KeyboardInterrupt:
        s.clear()
