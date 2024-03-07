import os
import sys

from panel import Panel, color
import time

from panel.draw import draw_text
from panel.font import Font


class App(Panel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        font = Font()
        while True:
            for f in os.listdir(self.args.fonts):
                if os.path.isfile(f'{self.args.fonts}/{f}') and f.endswith(".bdf"):
                    self.clear()
                    self.canvas.Fill(0, 0, 80)
                    try:
                        font.LoadFont(f'{self.args.fonts}/{f}')
                        # print(text, font.height, font.baseline, font)
                        draw_text(self, font, 0, font.height, color.WHITE, self.args.text)
                        if self.args.saveto:
                            fname = f"{font.height:02}_{f.replace('.bdf', '')}.jpg"
                            # print(fname)
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
