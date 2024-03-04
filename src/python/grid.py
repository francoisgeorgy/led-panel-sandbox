from panel import Panel
import color
import time

from panel.draw import line


class Grid(Panel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def grid(self, size, color):
        for x in range(0, self.canvas.width, size):
            line(self, x, 0, x, self.y_max, color)
        for y in range(0, self.canvas.height, size):
            line(self, 0, y, self.x_max, y, color)

    def run(self):
        grid_size = self.args.grid_size
        while True:
            self.clear()
            self.grid(grid_size, color.WHITE)
            self.refresh()
            time.sleep(0.1)


if __name__ == "__main__":
    s = Grid(add_args=[{'name': '--grid-size', 'help': 'Size of the grid in pixels', 'default': 8, 'type': int}])
    try:
        s.run()
    except KeyboardInterrupt:
        s.clear()
