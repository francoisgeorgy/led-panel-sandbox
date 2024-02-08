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


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):

        fonts_path = f'{os.path.dirname(__file__)}/../../fonts'
        font = graphics.Font()
        font.LoadFont(f"{fonts_path}/10x20.bdf")
        text = self.args.text

        t_len = text_len(font, text)
        print("text length:", t_len)

        # FBBX : Font Bounding Box X
        line_limit = len(text) * (font.headers['fbbx'] + 1)
        print("line_limit:", line_limit)

        text_map = font.bdf_font.draw(text, line_limit, missing=font.default_character).todata(2)
        print("text_map len:", len(text_map))
        print("text_map len [0]:", len(text_map[0]))
        for m in text_map:
            print(m)
        # font_y_offset = -(font.headers['fbby'] + font.headers['fbbyoff'])
        # bitmap_height = len(text_map[0]


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if not run_text.process():
        run_text.print_help()
