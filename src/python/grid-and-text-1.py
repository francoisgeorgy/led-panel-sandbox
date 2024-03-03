import os
import random

from samplebase import SampleBase
from color import Color
from font import Font


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


class App(SampleBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add additional command line options :
        self.parser.add_argument("--grid-size", help="Size of the grid in pixels", default=8)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello World!")
        self.width = 0
        self.height = 0

    def draw_text_mode(self, font, x, y, color, text, window_width=-1, text_offset=0,
                       wrap_around=False, wrap_positive_only=True,
                       color_callback=None, mode_xor=True):
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
        # character_widths = [__actual_width(font, letter) for letter in text]
        # total_width = sum(character_widths)
        total_width = text_len(font, text)
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
                    pixel_color = color
                    if mode_xor:
                        p = self.get_pixel(x + i, y + j + font_y_offset)
                        if p == [color.red, color.green, color.blue]:
                            pixel_color = Color.BLACK()
                    self.pixel(x + i, y + j + font_y_offset, pixel_color)
                    # canvas.SetPixel(x + i, y + j + font_y_offset, c.red, c.green, c.blue)
                j = j + 1
        return print_width, text_height

    def scroll_text(self, font, text, color, wx, wy, wd, initial_offset=0,
                    wrap_around=False,
                    wrap_when_pos_offset=True, speed=1.0):

        t_len = text_len(font, text)
        y_offset = -(font.headers['fbby'] + font.headers['fbbyoff']) - 1
        wrap_positive_only = wrap_when_pos_offset

        offset = initial_offset
        while True:
            ioffset = int(offset)

            w, h = self.draw_text_mode(font, wx, wy, color, text, text_offset=ioffset, window_width=wd,
                                       wrap_around=wrap_around, wrap_positive_only=wrap_positive_only)

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

            z = yield wx, wy
            if z is not None:
                wx, wy = z

    def rectangle(self, x, y, w, h, color, fill=False):
        if fill:
            for v in range(h):
                self.line(x, y+v, x+w-1, y+v, color)
        else:
            self.line(x, y, x+w-1, y, color)
            self.line(x+w-1, y, x+w-1, y+h-1, color)
            self.line(x, y+h-1, x+w-1, y+h-1, color)
            self.line(x, y, x, y+h-1, color)

    def draw_grid_random(self, size, positions, color):
        for (x, y) in positions:
            if size == 1:
                self.pixel(x, y, color)
            else:
                self.rectangle(x, y, size, size, color, fill=True)

    def get_random_positions(self, size):
        p = []
        for x in range(0, self.canvas.width, size):
            for y in range(0, self.canvas.height, size):
                if bool(random.getrandbits(1)):
                    p.append((x, y))
        return p

    def run(self):
        grid_size = int(self.args.grid_size)
        p = self.get_random_positions(grid_size)

        text = self.args.text

        font = Font()
        fonts_path = f'{os.path.dirname(__file__)}/../../fonts'
        # font.LoadFont(f"{fonts_path}/Helvetica_24.bdf")
        # font.LoadFont(f"{fonts_path}/New_York_36.bdf")
        font.LoadFont(f"{fonts_path}/Los_Angeles_24.bdf")
        t_len = text_len(font, "HOW TO SPEAK TO ROBOTS?")

        scroller = self.scroll_text(font, "HOW TO SPEAK TO ROBOTS?", Color.WHITE(),
                                    initial_offset=-127, wx=0, wy=44, wd=128,
                                    wrap_around=False)

        while True:
            self.clear()
            self.draw_grid_random(grid_size, p, Color.WHITE())
            next(scroller)
            self.refresh()


if __name__ == "__main__":
    s = App()
    try:
        s.setup()
        s.run()
    except KeyboardInterrupt:
        s.clear()
