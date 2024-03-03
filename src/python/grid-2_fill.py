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

    def draw_grid(self, size, color):
        b = True
        for x in range(0, self.canvas.width, size):
            b = not b
            for y in range(0, self.canvas.height, size):
                if b:
                    self.rectangle(x, y, size, size, color, True)
                b = not b

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
