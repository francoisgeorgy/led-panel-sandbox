EPSILON = 0.000001

width = 128-1
height = 64-1


def fx(y, m, b):
    """
    x = (y-b) / m
    """
    return (y - b) / (m + EPSILON)


def fy(x, m, b):
    return m * x + b

def get_scale_factors(dx, dy, dw, dh, zoom=1.0):
    return dw / dx * zoom, dh / dy * zoom

def scale_and_offset(x, y, sx, sy, x0=0, y0=0):
    """
    Scale and offset
    :param x: value to scale
    :param y: value to scale
    :param sx: scale x
    :param sy: scale y
    :param x0: destination value for x=0
    :param y0: destination value for y=0
    :return: scaled x and y
    """
    scaled_x = int(x * sx + 0.5)
    # print(x, sx, scaled_x)
    # if y_direction:
    #     # If y=0 is at the top, no change is needed as the screen coordinates work the same way.
    #     scaled_y = y * self.canvas.height
    # else:
    #     # If y=0 is at the bottom, invert the y coordinate.
    #     scaled_y = (1 - y) * self.canvas.height
    scaled_y = int(y * sy + 0.5)
    # scaled_y = (1 - y) * height
    return scaled_x + x0, height - (scaled_y + y0)


def constraint(x0, y0, x1, y1, fx, fy):
    """

    :param x0:
    :param y0:
    :param x1:
    :param y1:
    :return: two (x,y) points which are the crossing of the constraints
    """
    x_start, y_start, x_end, y_end = None, None, None, None
    x_left = x0
    y_left = fy(x_left, m, b)
    y_top = y0
    x_top = fx(y_top, m, b)
    x_right = x1
    y_right = fy(x_right, m, b)
    y_bottom = y1
    x_bottom = fx(y_bottom, m, b)
    print(x_left, y_left, x_top, y_top, x_right, y_right, x_bottom, y_bottom)
    if y0 <= y_left <= y1:
        x_start = x_left
        y_start = y_left
    if x0 <= x_top <= x1:
        print('a')
        if x_start is None:
            x_start = x_top
            y_start = y_top
        else:
            print('b')
            x_end = x_top
            y_end = y_top
    if (x_start is None or x_end is None) and (y0 <= y_right <= y1):
        print('c')
        if x_start is None:
            x_start = x_right
            y_start = y_right
        else:
            print('d')
            x_end = x_right
            y_end = y_right
    if (x_start is None or x_end is None) and (x0 <= x_bottom <= x1):
        print('e')
        if x_start is None:
            x_start = x_bottom
            y_start = y_bottom
        else:
            print('f')
            x_end = x_bottom
            y_end = y_bottom
    # print(x_start, y_start, x_end, y_end)
    return x_start, y_start, x_end, y_end


m = 5
b = 20

scale_x, scale_y = get_scale_factors(2.0, 2.0, 127, 63, 1.0)
x0, y0 = 63, 31

# x = -1.0
# y = fy(x, m, b)
# sx, sy = scale_and_offset(x, y, scale_x, scale_y, x0, y0)
# print(f'x,y {x:5.1f},{y:5.1f}, scaled {sx:5.1f},{sy:5.1f}')
#
# x = 1.0
# y = fy(x, m, b)
# sx, sy = scale_and_offset(x, y, scale_x, scale_y, x0, y0)
# print(f'x,y {x:5.1f},{y:5.1f}, scaled {sx:5.1f},{sy:5.1f}')
#
# y = 1.0
# x = fx(y, m, b)
# sx, sy = scale_and_offset(x, y, scale_x, scale_y, x0, y0)
# print(f'x,y {x:5.1f},{y:5.1f}, scaled {sx:5.1f},{sy:5.1f}')

m = -3
b = -3

x0, y0, x1, y1 = -2, -1, 2, 1
xs, ys, xe, ye = constraint(x0, y0, x1, y1, fx, fy)
print(f'(({xs},{ys}),({xe},{ye})')
print(f'({x0:5.1f},{y0:5.1f}),({x1:5.1f},{y1:5.1f}) --> ({xs:5.1f},{ys:5.1f}),({xe:5.1f},{ye:5.1f})')

