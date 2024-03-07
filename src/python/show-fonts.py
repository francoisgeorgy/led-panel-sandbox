import os
import sys

from panel import Panel, color
import time

from panel.draw import draw_text, text_len
from panel.font import Font


def split_text(font, text, max_width):
    parts = []
    t = text
    while text_len(font, t) > max_width:
        # if ' ' in t:
        #     p = t.split(' ', 1)
        #     parts.append(p[0])
        #     t = p[1]
        # else:
        i = -1
        n = 0
        while n < max_width and i < len(t):
            i = i + 1
            n = n + font.CharacterWidth(ord(t[i]))
        parts.append(t[0:i])
        t = t[i:]
    parts.append(t)
    return parts


class App(Panel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        font = Font()
        while True:
            for f in os.listdir(self.args.fonts):
                if os.path.isfile(f'{self.args.fonts}/{f}') and f.endswith(".bdf"):
                    # print(f)
                    self.clear()
                    self.canvas.Fill(0, 0, 80)
                    try:
                        font.LoadFont(f'{self.args.fonts}/{f}')
                        # print(text, font.height, font.baseline, font)

                        text_width = text_len(font, self.args.text)
                        if text_width > self.width:
                            parts = split_text(font, self.args.text, self.width)
                            y = font.height
                            for p in parts:
                                draw_text(self, font, 0, y, color.WHITE, p)
                                y = y + font.height
                        else:
                            draw_text(self, font, 0, font.height, color.WHITE, self.args.text)
                        if self.args.saveto:
                            fname = f"{font.height:02}_{f.replace('.bdf', '')}.jpg"
                            self.canvas.draw_to_file(f"{self.args.saveto}/{fname}")
                        self.refresh()
                        time.sleep(0.5)
                        # input()
                    except Exception as inst:
                        print(inst)
            break


if __name__ == "__main__":
    sys.argv += ["--led-rows", "64", "--led-cols", "256"]
    s = App(add_args=[
        {'name': '--text', 'help': 'text to display', 'default': 'Sphinx of black quartz, judge my vow', 'type': str},
        {'name': '--fonts', 'help': 'path to the folder containings the fonts', 'default': '.', 'type': str},
        {'name': '--saveto', 'help': 'path to the folder where saving the images', 'default': None, 'type': str}
    ])
    try:
        s.run()
    except KeyboardInterrupt:
        s.clear()
