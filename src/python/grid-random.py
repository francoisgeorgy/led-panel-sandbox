import random

from panel import Panel, color
import time

from panel.draw import line, rectangle


class Grid(Panel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def random_grid(self, size, color):
        for x in range(0, self.width, size):
            for y in range(0, self.height, size):
                if bool(random.getrandbits(1)):
                    rectangle(self, x, y, size, size, color, fill=True)

    def run(self):
        grid_size = self.args.grid_size
        while True:
            self.clear()
            self.random_grid(grid_size, color.WHITE)
            self.refresh()
            time.sleep(1.0)


if __name__ == "__main__":
    s = Grid(add_args=[{'name': '--grid-size', 'help': 'Size of the grid in pixels', 'default': 8, 'type': int}])
    try:
        s.run()
    except KeyboardInterrupt:
        s.clear()
