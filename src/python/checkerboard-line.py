import color
import time

from panel import Panel, MODE_XOR
from panel.draw import checkerboard, line


class Grid(Panel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        grid_size = self.args.grid_size
        while True:
            self.clear()
            checkerboard(self, grid_size, color.WHITE)
            line(self, 0, 0, self.x_max, self.y_max, color.WHITE, MODE_XOR)
            self.refresh()
            time.sleep(0.1)


if __name__ == "__main__":
    s = Grid(add_args=[{'name': '--grid-size', 'help': 'Size of the grid in pixels', 'default': 8, 'type': int}])
    try:
        s.run()
    except KeyboardInterrupt:
        s.clear()
