import random

from panel import Panel, color
import time

from panel.draw import rectangle


class Grid(Panel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def grid_by_positions(self, size, positions, c):
        for (x, y) in positions:
            rectangle(self, x, y, size, size, c, fill=True)

    def get_random_positions(self, size):
        p = []
        for x in range(0, self.canvas.width, size):
            for y in range(0, self.canvas.height, size):
                if bool(random.getrandbits(1)):
                    p.append((x, y))
        return p

    def run(self):
        grid_size = self.args.grid_size
        positions = self.get_random_positions(grid_size)
        while True:
            self.clear()
            self.grid_by_positions(grid_size, positions, color.WHITE)
            self.refresh()
            time.sleep(1.0)


if __name__ == "__main__":
    s = Grid(add_args=[{'name': '--grid-size', 'help': 'Size of the grid in pixels', 'default': 8, 'type': int}])
    try:
        s.run()
    except KeyboardInterrupt:
        s.clear()
