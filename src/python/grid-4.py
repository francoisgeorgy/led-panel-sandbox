import random

from samplebase import SampleBase
from color import Color
import time


class Grid(SampleBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add additional command line options :
        self.parser.add_argument("--grid-size", help="Size of the grid in pixels", default=8)

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

    def run(self):
        grid_size = int(self.args.grid_size)
        p = self.get_random_positions(grid_size)
        while True:
            self.clear()
            self.draw_grid_random(grid_size, p, Color.WHITE())
            self.refresh()
            time.sleep(0.1)


if __name__ == "__main__":
    s = Grid()
    try:
        s.setup()
        s.run()
    except KeyboardInterrupt:
        s.clear()
