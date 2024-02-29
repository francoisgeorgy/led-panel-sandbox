from samplebase import SampleBase
from color import Color
import time


class Grid(SampleBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add additional command line options :
        self.parser.add_argument("--grid-size", help="Size of the grid in pixels", default=8)

    def draw_grid(self, size, color):
        for x in range(0, self.canvas.width, size):
            self.line(x, 0, x, self.canvas.height-1, color)
        for y in range(0, self.canvas.height, size):
            self.line(0, y, self.canvas.width-1, y, color)

    def run(self):
        grid_size = self.args.grid_size
        while True:
            self.clear()
            self.draw_grid(grid_size, Color.WHITE())
            self.refresh()
            time.sleep(0.1)


if __name__ == "__main__":
    s = Grid()
    try:
        s.setup()
        s.run()
    except KeyboardInterrupt:
        s.clear()
