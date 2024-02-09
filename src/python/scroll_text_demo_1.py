import os

from color import Color
from font import Font
from samplebase import SampleBase
import time


def __actual_width(font, letter):
    '''
    Returns the actual width of the letter in the font. If the font doesn't contain a glyph for this letter, it falls back to
    the width of the default character (?) to prevent division by 0.
    '''
    width = font.CharacterWidth(ord(letter))

    if width > 0:
        return width

    return font.CharacterWidth(font.default_character.cp())


def text_len(font, text):
    return sum([__actual_width(font, letter) for letter in text])


def draw_text(canvas, font, x, y, color, text, window_width=-1, text_offset=0,
              wrap_around=False, wrap_positive_only=True,
              color_callback=None):
    """

    :param canvas:
    :param font:
    :param x: window X
    :param y: window Y = text X
    :param color:
    :param text:
    :param window_width: len of text to print, default = canvas.width - x
    :param text_offset: text X offset, default = 0
    :param wrap_around: default = false
    :param wrap_positive_only:
    :param color_callback:
    :return:
    """
    if len(text) == 0:
        return

    # Support multiple spacings based on device width
    character_widths = [__actual_width(font, letter) for letter in text]
    total_width = sum(character_widths)
    # FBBX : Font Bounding Box X
    line_limit = len(text) * (font.headers['fbbx'] + 1)
    text_map = font.bdf_font.draw(text, line_limit, missing=font.default_character).todata(2)
    font_y_offset = -(font.headers['fbby'] + font.headers['fbbyoff'])
    text_height = len(text_map)

    # if window_width < 0:
    #     print_width = canvas.width - x
    # else:
    print_width = window_width

    if isinstance(color, tuple):
        c = Color(color.red, color.green, color.blue)
    else:
        c = color
    save_c = c

    for i in range(print_width):
        xt = text_offset + i
        if color_callback:
            c = color_callback(xt)
        else:
            c = save_c
        if xt < 0:
            if wrap_around and not wrap_positive_only:
                xt = xt % total_width
            else:
                continue
        elif xt >= total_width:
            if wrap_around:
                xt = xt % total_width
            else:
                continue
        j = 0
        for row in text_map:
            if row[xt]:
                canvas.SetPixel(x + i, y + j + font_y_offset, c.red, c.green, c.blue)
            j = j + 1

    return print_width, text_height


class ScrollTextDemo(SampleBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add additional command line options :
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello World!")

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

            w, h = draw_text(self.canvas, font, wx, wy, color, text, text_offset=ioffset, window_width=wd,
                             wrap_around=wrap_around, wrap_positive_only=wrap_positive_only,
                             color_callback=color_callback)

            if border:
                self.line(wx - 1, wy + y_offset + h, wx + w, wy + y_offset + h, border_color)
                self.line(wx - 1, wy + y_offset, wx + w, wy + y_offset, border_color)
                self.line(wx - 1, wy + y_offset, wx - 1, wy + y_offset + h, border_color)
                self.line(wx + w, wy + y_offset, wx + w, wy + y_offset + h, border_color)

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
            self.rectangle(75, 32-16, 75+40, 32+3, Color.BLUE(), fill=True)
            next(scroller3)
            self.refresh()
            time.sleep(0.03)


if __name__ == "__main__":
    s = ScrollTextDemo()
    try:
        s.setup()
        s.run()
    except KeyboardInterrupt:
        s.clear()
