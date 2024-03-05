import time

from panel import Panel, MODE_XOR, color
from panel.draw import checkerboard, line


class Grid(Panel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        grid_size = self.args.grid_size
        x0, y0 = 0, 0
        x1, y1 = self.x_max, self.y_max
        while True:
            self.clear()
            checkerboard(self, grid_size, color.WHITE)
            line(self, x0, y0, x1, y1, color.WHITE, MODE_XOR)
            self.refresh()
            x0 = (x0 + 1) % self.width
            x1 = (x1 - 1) % self.width
            time.sleep(0.01)


if __name__ == "__main__":
    s = Grid(add_args=[{'name': '--grid-size', 'help': 'Size of the grid in pixels', 'default': 8, 'type': int}])
    try:
        s.run()
    except KeyboardInterrupt:
        s.clear()
