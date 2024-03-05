import time

from panel import Panel, color
from panel.draw import line


class App(Panel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        x0, y0 = 0, 0
        x1, y1 = self.x_max, self.y_max
        mx = 1
        while True:
            self.clear()
            line(self, x0, y0, x1, y1, color.WHITE)
            self.refresh()
            x0 = x0 + mx
            if x0 >= self.canvas.width:
                x0 = self.canvas.width - 1
                mx = -mx
            x1 = x1 - mx
            if x1 < 0:
                x1 = 0
            time.sleep(0.1)


if __name__ == "__main__":
    s = App()
    try:
        s.run()
    except KeyboardInterrupt:
        s.clear()
