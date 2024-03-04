import os

from color import Color
from font import Font
import time

from panel import Panel
from panel.draw import text_len, draw_text, line, rectangle


class ScrollTextExample(Panel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def scroll_text(self, font, text, color, wx, wy, wd, initial_offset=0,
                    wrap_around=False,
                    wrap_when_pos_offset=True, speed=1.0,
                    border=False, border_color=Color(255, 255, 255),
                    color_callback=None):

        t_len = text_len(font, text)
        y_offset = -(font.headers['fbby'] + font.headers['fbbyoff'])
        wrap_positive_only = wrap_when_pos_offset

        offset = initial_offset
        while True:
            ioffset = int(offset)

            w, h = draw_text(self, font, wx, wy, color, text, text_offset=ioffset, window_width=wd,
                             wrap_around=wrap_around, wrap_positive_only=wrap_positive_only,
                             color_callback=color_callback)

            if border:
                line(self, wx - 1, wy + y_offset + h, wx + w, wy + y_offset + h, border_color)
                line(self, wx - 1, wy + y_offset, wx + w, wy + y_offset, border_color)
                line(self, wx - 1, wy + y_offset, wx - 1, wy + y_offset + h, border_color)
                line(self, wx + w, wy + y_offset, wx + w, wy + y_offset + h, border_color)

            offset = offset + 1 * speed

            if wrap_around and not wrap_positive_only and wrap_when_pos_offset and offset >= 0:
                wrap_positive_only = True

            if wrap_around:
                if offset > 0:
                    offset = offset % t_len
            else:
                # same behavior
                if offset >= t_len:
                    offset = initial_offset

            yield

    def run(self):

        text = self.args.text

        fonts_path = f'{os.path.dirname(__file__)}/../../fonts'

        # font = rgb_graphics.Font()
        font = Font()
        font.LoadFont(f"{fonts_path}/10x20.bdf")
        # t_len = text_len(font, text)

        font2 = Font()
        font2.LoadFont(f"{fonts_path}/7x13.bdf")

        self.clear()
        self.refresh()

        scroller1 = self.scroll_text(font, text, Color(0, 255, 0),
                                     initial_offset=-80, wx=10, wy=20, wd=80,
                                     wrap_around=False,
                                     border=True, border_color=Color(200, 200, 200))
        scroller2 = self.scroll_text(font2, text, Color(255, 0, 0),
                                     initial_offset=-60, wx=16, wy=50, wd=60, speed=1.5,
                                     wrap_around=True,
                                     border=True, border_color=Color(0, 200, 200))
        scroller3 = self.scroll_text(font, text, Color(0, 255, 0),
                                     initial_offset=-40, wx=75, wy=32, wd=40, speed=1.0,
                                     wrap_around=True,
                                     border=True, border_color=Color(255, 200, 0))

        # color_callback=lambda xt: Color(xt/t_len*255, 100, 0))
        while True:
            self.clear()
            next(scroller1)
            next(scroller2)
            rectangle(self, 75, 32-16, 75+40, 32+3, Color.BLUE(), fill=True)
            next(scroller3)
            self.refresh()
            time.sleep(0.03)


if __name__ == "__main__":
    s = ScrollTextExample(add_args=[{'name': '--text', 'help': 'The text to scroll on the RGB LED panel', 'default': 'Hello World!', 'type': str}])
    try:
        s.run()
    except KeyboardInterrupt:
        s.clear()
