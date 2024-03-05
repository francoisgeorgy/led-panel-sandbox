import os

import time

from panel import Panel
from panel.color import Color
from panel.font import Font
from panel.draw import rectangle, text_scroller


# from panel.font import Font


class ScrollTextExample(Panel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        text = self.args.text

        fonts_path = f'{os.path.dirname(__file__)}/../../fonts'

        font = Font()
        font.LoadFont(f"{fonts_path}/10x20.bdf")

        font2 = Font()
        font2.LoadFont(f"{fonts_path}/7x13.bdf")

        scroller1 = text_scroller(self, font, text, Color(0, 255, 0),
                                  initial_offset=-80, wx=10, wy=20, wd=80,
                                  border=Color(200, 200, 200))
        scroller2 = text_scroller(self, font2, text, Color(255, 0, 0),
                                  initial_offset=-60, wx=16, wy=50, wd=60, speed=1.5,
                                  border=Color(0, 200, 200), wrap_around=True)
        scroller3 = text_scroller(self, font, text, Color(0, 255, 0),
                                  initial_offset=-40, wx=75, wy=32, wd=40, speed=0.5,
                                  border=Color(255, 200, 0), wrap_around=True)

        # color_callback=lambda xt: Color(xt/t_len*255, 100, 0))
        while True:
            self.clear()
            next(scroller1)
            next(scroller2)
            rectangle(self, 75, 32 - 16, 40, 20, Color.BLUE(), fill=True)
            next(scroller3)
            self.refresh()
            time.sleep(0.03)


if __name__ == "__main__":
    s = ScrollTextExample(add_args=[{'name': '--text', 'help': 'The text to scroll on the RGB LED panel', 'default': 'Hello World!', 'type': str}])
    try:
        s.run()
    except KeyboardInterrupt:
        s.clear()
