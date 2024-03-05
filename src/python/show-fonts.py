import os

from panel import Panel, color
import time

from panel.draw import line, draw_text
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
                    print(f, font.baseline, font.height)
                    font.LoadFont(f'{self.args.fonts}/{f}')
                    draw_text(self, font, 0, font.height, color.WHITE, f)   #, window_width=self.width)
                    self.refresh()
                    time.sleep(0.5)
                    # input()


if __name__ == "__main__":
    s = App(add_args=[{'name': '--fonts', 'help': 'path to the folder containings the fonts', 'default': '.', 'type': str}])
    try:
        s.run()
    except KeyboardInterrupt:
        s.clear()
