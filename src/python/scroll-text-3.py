import os
from math import sin

from panel.color import Color
from panel.font import Font
import time

from panel import Panel
from panel.draw import text_len, rectangle, text_scroller


class ScrollTextExample(Panel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def fill_bg(self):
        for y in range(self.canvas.height):
            for x in range(self.canvas.width):
                self.pixel(x, y, Color(x / 128 * 180, y / 64 * 180, 80))

    def run(self):
        text = self.args.text

        fonts_path = f'{os.path.dirname(__file__)}/../../fonts'

        font = Font()
        font.LoadFont(f"{fonts_path}/Helvetica_24.bdf")
        t_len = text_len(font, "Hello World!")

        font2 = Font()
        font2.LoadFont(f"{fonts_path}/7x13.bdf")

        font3 = Font()
        font3.LoadFont(f"{fonts_path}/Times-Italic_18.bdf")

        wx3, wy3 = 44, 32

        scroller1 = text_scroller(self, font, "Hello World!", Color(0, 255, 0),
                                     initial_offset=-127, wx=0, wy=24, wd=128,
                                     color_callback=lambda xt: Color(0, max(xt/t_len*215+40, 0), 0))
        scroller2 = text_scroller(self, font2, "Faster! ", Color(255, 0, 0),
                                     initial_offset=-107, wx=10, wy=54, wd=107, speed=2.4,
                                     wrap_around=True)
        scroller3 = text_scroller(self, font3, "Let's move... ", Color(0, 255, 0),
                                     initial_offset=-50, wx=wx3, wy=wy3, wd=50, speed=1.0,
                                     wrap_around=True)

        t = 0
        w3 = None   # because the first value sent to a generator must be None if the generator has not been started yet
        while True:
            self.clear()
            self.fill_bg()
            next(scroller1)
            rectangle(self, 10, 54 - 10, 107, 12, Color.BLACK(), fill=True)
            next(scroller2)
            rectangle(self, wx3, wy3-14, 50, 18, Color.BLUE(), fill=True)
            scroller3.send(w3)
            wx3 = round(44 + sin(t/37) * 50)
            wy3 = round(38 + sin(t/31+3) * 20)
            w3 = (wx3, wy3)
            t = t + 1
            self.refresh()
            time.sleep(0.04)


if __name__ == "__main__":
    s = ScrollTextExample(add_args=[
        {'name': '--text', 'help': 'The text to scroll on the RGB LED panel', 'default': 'Hello World!', 'type': str}])
    try:
        s.run()
    except KeyboardInterrupt:
        s.clear()
