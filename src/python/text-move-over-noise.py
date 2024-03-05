import os
import random
import time
from math import sin, cos

from panel import Panel, MODE_XOR, color
from panel.draw import line, rectangle, text_len, text_scroller
from panel.font import Font


class App(Panel):

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

        font = Font()
        fonts_path = f'{os.path.dirname(__file__)}/../../fonts'
        font.LoadFont(f"{fonts_path}/Helvetica_24.bdf")
        # font.LoadFont(f"{fonts_path}/Los_Angeles_24.bdf")

        scroller = text_scroller(self, font, self.args.text, color.WHITE,
                                 initial_offset=-127, wx=0, wy=44, wd=128,
                                 mode=MODE_XOR)

        while True:
            self.clear()
            self.grid_by_positions(grid_size, positions, color.WHITE)
            next(scroller)
            self.refresh()


if __name__ == "__main__":
    s = App(add_args=[
        {'name': '--grid-size', 'help': 'Size of the grid in pixels', 'default': 1, 'type': int},
        {'name': '--text', 'help': 'The text to scroll on the RGB LED panel', 'default': 'HOW WE SPEAK TO ROBOTS', 'type': str}
    ])
    try:
        s.run()
    except KeyboardInterrupt:
        s.clear()
