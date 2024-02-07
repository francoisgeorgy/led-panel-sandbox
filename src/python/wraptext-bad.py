#!/usr/bin/env python
# Display a runtext with double-buffering.
import os

from samplebase import SampleBase
from RGBMatrixEmulator import graphics
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
    # character_widths = [__actual_width(font, letter) for letter in text]
    # return sum(character_widths)
    return sum([__actual_width(font, letter) for letter in text])

def draw_text(canvas, font, x, y, color, text, w=-1, o=0, wrap_around=False):
    """
        +-------------+     +-------------+
        |             |     |             |
    ABCDEFGHIJKLMNOPQRSTUVWXYZ  ABCDEFGHIJKLMNOPQRSTUVWXYZ
        |             |     |             |
        +-------------+     +-------------+
        x             x+w

        +-------------+     +-------------+     +-------------+     +-------------+
        |             |     |             |     |             |     |             |
        |             ABCDEFGHIJKLMNOPQRSTUVWXYZ  ABCDEFGHIJKLMNOPQRSTUVWXYZ  ABCDE...
        |             |     |             |     |             |     |             |
        +-------------+     +-------------+     +-------------+     +-------------+
        x             x+w

    idea : pass "x" and "w" params to define a "window" in which to draw the text.
           If the text ends before the end of the window, a zero or positive wrap-around value
           will tell to "wrap the text" after a space of "wrap-around" pixels.

           By default, the window width will be equal of (canvas.width - x) and the
           wrap-around value will be -1 to signify "no wrap-around".

    :param canvas:
    :param font:
    :param x: start X
    :param y: start Y
    :param color:
    :param text:
    :param w: len of text to print, default = canvas.width - x
    :param o: text X offset, default = 0
    :param wrap_around: default = false
    :return:
    """
    if len(text) == 0:
        return

    # Support multiple spacings based on device width
    character_widths = [__actual_width(font, letter) for letter in text]
    # first_char_width = character_widths[0]
    # max_char_width = max(character_widths)
    total_width = sum(character_widths)

    # FBBX : Font Bounding Box X
    line_limit = len(text) * (font.headers['fbbx'] + 1)

    text_map = font.bdf_font.draw(text, line_limit, missing=font.default_character).todata(2)
    font_y_offset = -(font.headers['fbby'] + font.headers['fbbyoff'])

    if w < 0:
        wd = canvas.width - x
    else:
        wd = w

    print(f"draw from {o} for {wd} at {x}")

    xi = -1
    for y2, row in enumerate(text_map):
        if y2 != 16:    # DEBUG
            continue
        for x2, value in enumerate(row):
            if value == 1:
                # print(f"x={x} o={o} x2={x2} wd={wd} xi={xi}")
                if x2 < o:
                    continue
                xi = x - o + x2
                if xi > wd:
                    # print("wrap?", x, o, x2, x - o + x2, wd)
                    # continue
                    break
                try:
                    # print(f"x={x} o={o} x2={x2} wd={wd} xi={x - o + x2}")
                    # if wrap_around:
                    #     pass
                        # xi = (x + x2) % canvas.width
                        # # print(total_width, x, x2, x+x2, xi)
                        # # break
                        # if xi < x + x2:
                        #     xi = x + x2
                    # else:
                    # xi = x - o + x2
                    if 0 <= xi < canvas.width:
                        # print(f"print! x2={x2} x={x} o={o} wd={wd} xi={xi}")
                        if isinstance(color, tuple):
                            canvas.SetPixel(xi, y + y2 + font_y_offset, *color)
                        else:
                            canvas.SetPixel(xi, y + y2 + font_y_offset, color.red, color.green, color.blue)
                except Exception:
                    pass

    if wrap_around and (x2 >= (total_width - 1)):
        # print(f"end: x2={x2}, xi={xi}")
        if xi < wd:
            # wrap around
            print(f"wrap around at xi={xi} x2={x2}")
            # o is replaced by xi
            for y2, row in enumerate(text_map):
                if y2 != 16:    # DEBUG
                    continue
                for x2, value in enumerate(row):
                    if value == 1:
                        # print(f"x={x} o={o} x2={x2} wd={wd} xi={xi}")
                        # if x2 < o:
                        #     continue
                        xj = x - xi + x2
                        if xj > wd:
                            # print("wrap?", x, o, x2, x - o + x2, wd)
                            # continue
                            break
                        try:
                            if 0 <= xj < canvas.width:
                                # print(f"print! x2={x2} x={x} o={o} wd={wd} xi={xi}")
                                if isinstance(color, tuple):
                                    canvas.SetPixel(xj, y + y2 + font_y_offset, *color)
                                else:
                                    canvas.SetPixel(xj, y + y2 + font_y_offset, color.red, color.green, color.blue)
                        except Exception:
                            pass

    return total_width


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):

        fonts_path = f'{os.path.dirname(__file__)}/../../fonts'

        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont(f"{fonts_path}/10x20.bdf")
        text_color = graphics.Color(255, 255, 0)
        my_text = self.args.text

        t_len = text_len(font, my_text)
        print("text length:", t_len)

        pos = -offscreen_canvas.width
        # pos = 150   # debug, gagner du temps
        wrap = False
        while True:
            offscreen_canvas.Clear()
            # len = graphics.DrawText(offscreen_canvas, font, pos, 30, text_color, my_text)
            t_len = draw_text(offscreen_canvas, font, 0, 30, text_color, my_text, o=pos, wrap_around=wrap)
            # if pos < 0:
            pos += 1

            # no wrap-around:
            # if pos >= t_len:
            #     pos = -offscreen_canvas.width

            # input()

            # wrap-around:
            if pos >= t_len:
                print(f"pos >= t_len {pos}")
                # pos = t_len - offscreen_canvas.width
                pos = 0
                wrap = True

            # else:
            #     pos
            # if pos < 0:
            #     pos = offscreen_canvas.width
                # wrap = True
            # if pos + t_len < 0:
            #     pos = offscreen_canvas.width

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if not run_text.process():
        run_text.print_help()
