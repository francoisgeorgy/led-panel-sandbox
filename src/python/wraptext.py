#!/usr/bin/env python
# Display a runtext with double-buffering.
import os

from samplebase import SampleBase
from RGBMatrixEmulator import graphics, Color
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

def draw_text(canvas, font, x, y, color, text, window_width=-1, text_offset=0, wrap_around=False):
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
    :param x: window X
    :param y: window Y = text X
    :param color:
    :param text:
    :param window_width: len of text to print, default = canvas.width - x
    :param text_offset: text X offset, default = 0
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
    # bitmap_height = len(text_map[0]

    # length to print :
    if window_width < 0:
        print_width = canvas.width - x
    else:
        print_width = window_width

    print(f"print text from {text_offset} to {text_offset + print_width} at position {x}")

    if isinstance(color, tuple):
        c = Color(color.red, color.green, color.blue)
    else:
        c = color
    save_c = c

    for i in range(print_width):
        c = save_c
        # text X :
        xt = text_offset + i
        # print(f"{xt} : ", end='')
        if xt < 0:
            if wrap_around:
                # print(f"{xt} < 0", end='')
                # update xt
                xt = xt % total_width
                c = Color(255, 0, 0)
            else:
                # update xt
                continue
        elif xt >= total_width:
            if wrap_around:
                # print(f"{xt} >= {total_width}", end='')
                # update xt
                xt = xt % total_width
                c = Color(0, 0, 255)
            else:
                # update xt
                continue
        # print text column xt :
        # print(f' print text[{xt}] at {x+i}')
        j = 0
        for row in text_map:
            # set pixel at (x + i, y)
            if row[xt]:
                canvas.SetPixel(x + i, y + j + font_y_offset, c.red, c.green, c.blue)
            j = j + 1


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

        font_y_offset = -(font.headers['fbby'] + font.headers['fbbyoff'])
        print("font_y_offset:", font_y_offset)

        offscreen_canvas.Clear()

        wx = 10
        wy = 30
        wd = 80

        # offset = 30
        #
        # graphics.DrawLine(offscreen_canvas, wx-1, wy-1+20+font_y_offset, wx+0+wd, wy-1+20+font_y_offset, Color(200, 200, 200))
        # graphics.DrawLine(offscreen_canvas, wx-1, wy-1+0+font_y_offset, wx+0+wd, wy-1+0+font_y_offset, Color(200, 200, 200))
        # graphics.DrawLine(offscreen_canvas, wx-1, wy-1+0+font_y_offset, wx-1, wy-1+20+font_y_offset, Color(200, 200, 200))
        # graphics.DrawLine(offscreen_canvas, wx+0+wd, wy-1+0+font_y_offset, wx+0+wd, wy-1+20+font_y_offset, Color(200, 200, 200))
        #
        # draw_text(offscreen_canvas, font, wx, wy, text_color, my_text, text_offset=offset, window_width=wd, wrap_around=True)
        # offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
        # print("return to quit")
        # input()
        # return

        offset = 40
        while True:
            offscreen_canvas.Clear()
            graphics.DrawLine(offscreen_canvas, wx-1, wy-1+20+font_y_offset, wx+0+wd, wy-1+20+font_y_offset, Color(200, 200, 200))
            graphics.DrawLine(offscreen_canvas, wx-1, wy-1+0+font_y_offset, wx+0+wd, wy-1+0+font_y_offset, Color(200, 200, 200))
            graphics.DrawLine(offscreen_canvas, wx-1, wy-1+0+font_y_offset, wx-1, wy-1+20+font_y_offset, Color(200, 200, 200))
            graphics.DrawLine(offscreen_canvas, wx+0+wd, wy-1+0+font_y_offset, wx+0+wd, wy-1+20+font_y_offset, Color(200, 200, 200))

            draw_text(offscreen_canvas, font, wx, wy, text_color, my_text, text_offset=offset, window_width=wd, wrap_around=True)
            offset = (offset + 1) % t_len

            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
            # time.sleep(0.1)
            # break

        # print("done")
        # input()

        # pos = -offscreen_canvas.width
        # # pos = 150   # debug, gagner du temps
        # wrap = False
        # while True:
        #     offscreen_canvas.Clear()
        #
        #     draw_text(offscreen_canvas, font, 0, 30, text_color, my_text)
        #
        #     # len = graphics.DrawText(offscreen_canvas, font, pos, 30, text_color, my_text)
        #     t_len = draw_text(offscreen_canvas, font, 0, 30, text_color, my_text, text_offset=pos, wrap_around=wrap)
        #     # if pos < 0:
        #     pos += 1
        #
        #     # no wrap-around:
        #     # if pos >= t_len:
        #     #     pos = -offscreen_canvas.width
        #
        #     # input()
        #
        #     # wrap-around:
        #     if pos >= t_len:
        #         print(f"pos >= t_len {pos}")
        #         # pos = t_len - offscreen_canvas.width
        #         pos = 0
        #         wrap = True
        #
        #     # else:
        #     #     pos
        #     # if pos < 0:
        #     #     pos = offscreen_canvas.width
        #         # wrap = True
        #     # if pos + t_len < 0:
        #     #     pos = offscreen_canvas.width
        #
        #     time.sleep(0.05)
        #     offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if not run_text.process():
        run_text.print_help()
