from samplebase import SampleBase
from color import Color
import time


class App(SampleBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            self.clear()
            self.line(0, 4, 127, 54, Color.WHITE())
            self.line(0, 8, 127, 58, Color.WHITE())
            self.line(60, 0, 99, 63, Color.WHITE())
            self.line(64, 0, 103, 63, Color.WHITE())
            self.refresh()
            time.sleep(0.1)


if __name__ == "__main__":
    s = App()
    try:
        s.setup()
        s.run()
    except KeyboardInterrupt:
        s.clear()
