from math import sin, cos

import time

from panel import Panel, color
from panel.draw import line


class App(Panel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        x0, y0 = 0, 0
        x1, y1 = self.x_max, self.y_max
        t = 0
        while True:
            self.clear()
            x0 = int((sin(t / 20) + 1) / 2 * 127 + 0.5)
            x1 = int((cos(t / 30 + 3) + 1) / 2 * 127 + 0.5)
            line(self, x0, y0, x1, y1, color.WHITE)
            self.refresh()
            t = t + 1
            time.sleep(0.01)


if __name__ == "__main__":
    s = App()
    try:
        s.run()
    except KeyboardInterrupt:
        s.clear()
