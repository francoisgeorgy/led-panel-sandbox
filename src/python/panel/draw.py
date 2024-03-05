from panel import MODE_OVERWRITE, rgb_graphics
from panel.color import Color


def line(panel, x0, y0, x1, y1, color, mode=MODE_OVERWRITE):
    '''
    Line drawing algorithm

    Source : https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm

    Parameters
    ----------
    x1, y1 : int            Starting position (row, column).
    x2, y2 : int            End position (row, column).

    See Also
    --------
    line_aa : Anti-aliased line generator
    :param panel:
    :param mode:
    :param y1:
    :param x1:
    :param y0:
    :param x0:
    :param mode_xor:
    :param color:
    '''
    x = x0
    y = y0
    xi = 1 if x0 < x1 else -1
    yi = 1 if y0 < y1 else -1
    dx = abs(x1 - x0)
    dy = -abs(y1 - y0)
    error = dx + dy
    while True:
        panel.pixel(x, y, color, mode)
        if x == x1 and y == y1:
            break
        e2 = 2 * error
        if e2 >= dy:
            if x == x1:
                break
            error = error + dy
            x = x + xi
        if e2 <= dx:
            if y == y1:
                break
            error = error + dx
            y = y + yi


def rectangle(panel, x, y, w, h, color, fill=False, mode=MODE_OVERWRITE):
    if w == 1 and h == 1:
        panel.pixel(x, y, color, mode)
    elif fill:
        for v in range(h):
            line(panel, x, y + v, x + w - 1, y + v, color, mode)
    else:
        line(panel, x, y, x + w - 1, y, color, mode)
        line(panel, x + w - 1, y, x + w - 1, y + h - 1, color, mode)
        line(panel, x, y + h - 1, x + w - 1, y + h - 1, color, mode)
        line(panel, x, y, x, y + h - 1, color, mode)


def checkerboard(panel, size, color):
    b = False
    for x in range(0, panel.canvas.width, size):
        for y in range(0, panel.canvas.height, size):
            if b:
                rectangle(panel, x, y, size, size, color, True)
            b = not b
        b = not b


def circle(panel, x0, y0, r, color, mode=MODE_OVERWRITE):
    rgb_graphics.DrawCircle(panel.canvas, x0, y0, r, color)


def text(panel, x, y, color, text, font, mode=MODE_OVERWRITE):
    rgb_graphics.DrawText(panel.canvas, font, x, y, color, text)


def __actual_width(font, letter):
    '''
    Returns the actual width of the letter in the font. If the font doesn't contain a glyph for this letter, it falls back to
    the width of the default character (?) to prevent division by 0.
    '''
    width = font.CharacterWidth(ord(letter))

    if width > 0:
        return width

    return font.CharacterWidth(font.default_character.cp())


def text_len(font, t):
    return sum([__actual_width(font, letter) for letter in t])


def draw_text(panel, font, x, y, color, text, window_width=-1, text_offset=0,
              wrap_around=False, wrap_positive_only=True,
              color_callback=None, mode=MODE_OVERWRITE):
    """

    :param panel:
    :param font:
    :param x: window X
    :param y: window Y = text X
    :param color:
    :param text:
    :param window_width: len of text to print, default = panel.width - x
    :param text_offset: text X offset, default = 0
    :param wrap_around: default = false
    :param wrap_positive_only:
    :param color_callback:
    :return:
    """
    if len(text) == 0:
        return

    # Support multiple spacings based on device width
    total_width = text_len(font, text)
    # FBBX : Font Bounding Box X
    line_limit = len(text) * (font.headers['fbbx'] + 1)
    text_map = font.bdf_font.draw(text, line_limit, missing=font.default_character).todata(2)
    font_y_offset = -(font.headers['fbby'] + font.headers['fbbyoff'])
    text_height = len(text_map)

    if window_width < 0:
        print_width = panel.width - x
    else:
        print_width = window_width

    if isinstance(color, tuple):
        c = Color(color.red, color.green, color.blue)
        # print("tuple", c)
    else:
        c = color
        # print("pas tuple", c, color.red, color.green, color.blue)
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
                # panel.SetPixel(x + i, y + j + font_y_offset, c.red, c.green, c.blue)
                panel.pixel(x + i, y + j + font_y_offset, c, mode=mode)
            j = j + 1

    return print_width, text_height


def text_scroller(panel, font, text, color, wx, wy, wd, initial_offset=0,
                  wrap_around=False,
                  wrap_when_pos_offset=True, speed=1.0,
                  border=None, #False, border_color=Color(0, 0, 0),
                  color_callback=None,
                  mode=MODE_OVERWRITE):

    t_len = text_len(font, text)
    y_offset = -(font.headers['fbby'] + font.headers['fbbyoff'])
    wrap_positive_only = wrap_when_pos_offset

    offset = initial_offset
    while True:
        ioffset = int(offset)

        w, h = draw_text(panel, font, wx, wy, color, text, text_offset=ioffset, window_width=wd,
                         wrap_around=wrap_around, wrap_positive_only=wrap_positive_only,
                         color_callback=color_callback, mode=mode)

        if border:
            line(panel, wx - 1, wy + y_offset + h, wx + w, wy + y_offset + h, border, mode)
            line(panel, wx - 1, wy + y_offset, wx + w, wy + y_offset, border, mode)
            line(panel, wx - 1, wy + y_offset, wx - 1, wy + y_offset + h, border, mode)
            line(panel, wx + w, wy + y_offset, wx + w, wy + y_offset + h, border, mode)

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
        # yield
        z = yield wx, wy
        if z is not None:
            wx, wy = z
