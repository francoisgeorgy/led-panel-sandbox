from samplebase import SampleBase
from color import Color
import time

"""
Draw a line
"""

class DrawLine(SampleBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add additional command line options :
        self.parser.add_argument("--grid-size", help="Size of the grid in pixels", default=8)

    def draw_line(self, x1, y1, x2, y2, color):
        '''
        Line drawing algorithm

        Extracted from scikit-image:
        https://github.com/scikit-image/scikit-image/blob/00177e14097237ef20ed3141ed454bc81b308f82/skimage/draw/_draw.pyx#L44

        Generate line pixel coordinates.

        Parameters
        ----------
        x1, y1 : int            Starting position (row, column).
        x2, y2 : int            End position (row, column).

        Returns
        -------
        rr, cc : (N,) ndarray of int
            Indices of pixels that belong to the line.
            May be used to directly index into an array, e.g.
            ``img[rr, cc] = 1``.

        See Also
        --------
        line_aa : Anti-aliased line generator
        '''
        steep = 0
        r = x1
        c = y1
        dr = abs(x2 - x1)
        dc = abs(y2 - y1)

        rr = [0] * (max(dc, dr) + 1)
        cc = [0] * (max(dc, dr) + 1)

        if (y2 - c) > 0:
            sc = 1
        else:
            sc = -1
        if (x2 - r) > 0:
            sr = 1
        else:
            sr = -1
        if dr > dc:
            steep = 1
            c, r = r, c
            dc, dr = dr, dc
            sc, sr = sr, sc
        d = (2 * dr) - dc

        for i in range(dc):
            if steep:
                rr[i] = c
                cc[i] = r
                self.pixel(c, r, color)
            else:
                rr[i] = r
                cc[i] = c
                self.pixel(r, c, color)
            while d >= 0:
                r = r + sr
                d = d - (2 * dc)
            c = c + sc
            d = d + (2 * dr)

        rr[dc] = x2
        cc[dc] = y2
        self.pixel(x2, y2, color)

        # print(rr, cc)

        return rr, cc

    def draw_grid(self, size, color):
        for x in range(0, self.canvas.width, size):
            self.line(x, 0, x, self.canvas.height-1, color)
        for y in range(0, self.canvas.height, size):
            self.line(0, y, self.canvas.width-1, y, color)

    def run(self):
        grid_size = self.args.grid_size
        while True:
            self.clear()
            # self.draw_grid(grid_size, Color.WHITE())
            self.draw_line(0, 0, 9, 9, Color.YELLOW())
            self.refresh()
            time.sleep(0.1)


if __name__ == "__main__":
    s = DrawLine()
    try:
        s.setup()
        s.run()
    except KeyboardInterrupt:
        s.clear()
