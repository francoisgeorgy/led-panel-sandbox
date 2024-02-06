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


def draw_text(canvas, font, x, y, color, text, wrap_around=False):
    """
        +-------------+     +-------------+
        |             |     |             |
    ABCDEFGHIJKLMNOPQRSTUVWXYZ  ABCDEFGHIJKLMNOPQRSTUVWXYZ
        |             |     |             |
        +-------------+     +-------------+
        x0          x0 + w

    idea : pass "x" and "w" params to define a "window" in which to draw the text.
           If the text ends before the end of the window, a zero or positive wrap-around value
           will tell to "wrap the text" after a space of "wrap-around" pixels.

           By default, the window width will be equal of (canvas.width - x) and the
           wrap-around value will be -1 to signify "no wrap-around".


    :param canvas:
    :param font:
    :param x:
    :param y:
    :param color:
    :param text:
    :param wrap_around:
    :return:
    """
    # Early return for empty string prevents bugs in bdfparser library
    # and makes good sense anyway
    if len(text) == 0:
        return

    # Support multiple spacings based on device width
    character_widths = [__actual_width(font, letter) for letter in text]
    first_char_width = character_widths[0]
    max_char_width = max(character_widths)
    total_width = sum(character_widths)

    # Offscreen to the left, adjust by first character width
    # if x < 0:
    #     adjustment = abs(x + first_char_width) // first_char_width
    #     text = text[adjustment:]
    #     if adjustment:
    #         x += first_char_width * adjustment

    # Offscreen to the right, rough adjustment by max width
    # if (total_width + x) > canvas.width:
    #     text = text[: ((canvas.width + 1) // max_char_width) + 2]

    # Draw the text!
    # Ensure text doesn't get drawn as multiple lines
    #
    # FBBX : Font Bounding Box X
    #
    line_limit = len(text) * (font.headers['fbbx'] + 1)

    text_map = font.bdf_font.draw(text, line_limit, missing=font.default_character).todata(2)
    font_y_offset = -(font.headers['fbby'] + font.headers['fbbyoff'])

    for y2, row in enumerate(text_map):
        for x2, value in enumerate(row):
            if value == 1:
                try:
                    if wrap_around:
                        xi = (x + x2) % canvas.width
                        # print(total_width, x, x2, x+x2, xi)
                        # break
                        if xi < x + x2:
                            xi = x + x2
                    else:
                        xi = x + x2
                    if 0 <= xi < canvas.width:
                        if isinstance(color, tuple):
                            canvas.SetPixel(xi, y + y2 + font_y_offset, *color)
                        else:
                            canvas.SetPixel(xi, y + y2 + font_y_offset, color.red, color.green, color.blue)
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

        pos = offscreen_canvas.width
        wrap = False
        while True:
            offscreen_canvas.Clear()
            # len = graphics.DrawText(offscreen_canvas, font, pos, 30, text_color, my_text)
            t_len = draw_text(offscreen_canvas, font, pos, 30, text_color, my_text, wrap)
            pos -= 1
            if pos < 0:
                pos = offscreen_canvas.width
                # wrap = True
            # if pos + t_len < 0:
            #     pos = offscreen_canvas.width

            time.sleep(0.04)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if not run_text.process():
        run_text.print_help()
