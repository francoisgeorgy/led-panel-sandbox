import os

# Display a text with double-buffering.
#
# Example how to add additional commandline parameters


class RunText(Cube):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add additional command line options :
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello World!")

    def run(self):

        # font = load_font('10x20.bdf')

        fonts_path = f'{os.path.dirname(__file__)}/../../fonts'
        font = rgb_graphics.Font()
        font.LoadFont(f'{fonts_path}/swiss-36-vga.bdf')
        h = 64 - int((64 - font.height) / 1)

        pos = self.canvas.width
        my_text = self.args.text

        while True:
            self.canvas.Clear()
            self.canvas.Fill(0, 0, 60)
            n = rgb_graphics.DrawText(self.canvas, font, pos, h, Color.YELLOW(), my_text)
            pos -= 1
            if pos + n < 0:
                pos = self.canvas.width
            self.refresh()


if __name__ == "__main__":
    s = RunText()
    print("CTRL-C to quit", end="", flush=True)
    try:
        s.setup()
        s.run()
    except KeyboardInterrupt:
        print("\r\033[Kbye")  # \r : go to beginning of line; \033[K : clear from cursor to the end of the line
        s.clear()
