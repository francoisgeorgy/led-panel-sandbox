import random
from math import sin, cos

from samplebase import SampleBase
from color import Color
import time


class App(SampleBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add additional command line options :
        # self.parser.add_argument("--grid-size", help="Size of the grid in pixels", default=8)

    # def rectangle(self, x, y, w, h, color, fill=False):
    #     if fill:
    #         for v in range(h):
    #             self.line(x, y+v, x+w-1, y+v, color)
    #     else:
    #         self.line(x, y, x+w-1, y, color)
    #         self.line(x+w-1, y, x+w-1, y+h-1, color)
    #         self.line(x, y+h-1, x+w-1, y+h-1, color)
    #         self.line(x, y, x, y+h-1, color)
    #
    # def draw_grid(self, size, color):
    #     b = True
    #     for x in range(0, self.canvas.width, size):
    #         b = not b
    #         for y in range(0, self.canvas.height, size):
    #             if b:
    #                 self.rectangle(x, y, size, size, color, True)
    #             b = not b

    def run(self):
        # grid_size = self.args.grid_size
        # x0, y0 = 0, 0
        x1, y1 = self.canvas.width - 1, self.canvas.height - 1
        t = 0
        while True:
            self.clear()
            # self.draw_grid(grid_size, Color.WHITE())
            x0 = int((sin(t / 20) + 1) / 2 * 127 + 0.5)
            x1 = int((cos(t / 30 + 3) + 1) / 2 * 127 + 0.5)
            # y0 = int((sin(t / 20) + 1) / 2 * 63 + 0.5)
            # y1 = int((cos(t / 30 + 3) + 1) / 2 * 63 + 0.5)

            # TODO:
            # compute line equation

            # print(mx0)
            self.line(x0, y0, x1, y1, Color.WHITE())
            self.refresh()
            t = t + 1
            time.sleep(0.01)


if __name__ == "__main__":
    s = App()
    try:
        s.setup()
        s.run()
    except KeyboardInterrupt:
        s.clear()
