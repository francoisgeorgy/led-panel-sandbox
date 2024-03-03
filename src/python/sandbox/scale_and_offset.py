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


m = 0.5
b = 0.5

# scale_x = 127 / 2.0     # x and y are [-1..+1]
# scale_y = 63 / 2.0
scale_x, scale_y = get_scale_factors(2.0, 2.0, 127, 63, 1.0)
x0, y0 = 63, 31

# x, y = 0.5, 0.5
# sx, sy = scale_and_offset(x, y, scale_x, scale_y, x0, y0)
# print(f'x,y {x:5.1f},{y:5.1f}, scaled {sx:5.1f},{sy:5.1f}')
x, y = 0, 0
sx, sy = scale_and_offset(x, y, scale_x, scale_y, x0, y0)
print(f'x,y {x:5.1f},{y:5.1f}, scaled {sx:5.1f},{sy:5.1f}')
x, y = 1, 0
sx, sy = scale_and_offset(x, y, scale_x, scale_y, x0, y0)
print(f'x,y {x:5.1f},{y:5.1f}, scaled {sx:5.1f},{sy:5.1f}')
x, y = 1, 1
sx, sy = scale_and_offset(x, y, scale_x, scale_y, x0, y0)
print(f'x,y {x:5.1f},{y:5.1f}, scaled {sx:5.1f},{sy:5.1f}')
x, y = 0, 1
sx, sy = scale_and_offset(x, y, scale_x, scale_y, x0, y0)
print(f'x,y {x:5.1f},{y:5.1f}, scaled {sx:5.1f},{sy:5.1f}')
x, y = -1, 1
sx, sy = scale_and_offset(x, y, scale_x, scale_y, x0, y0)
print(f'x,y {x:5.1f},{y:5.1f}, scaled {sx:5.1f},{sy:5.1f}')
# x, y = -1, 0
# sx, sy = scale_and_offset(x, y, scale_x, scale_y, x0, y0)
# print(f'x,y {x:5.1f},{y:5.1f}, scaled {sx:5.1f},{sy:5.1f}')
# x, y = -1, -1
# sx, sy = scale_and_offset(x, y, scale_x, scale_y, x0, y0)
# print(f'x,y {x:5.1f},{y:5.1f}, scaled {sx:5.1f},{sy:5.1f}')
# x, y = 0, -1
# sx, sy = scale_and_offset(x, y, scale_x, scale_y, x0, y0)
# print(f'x,y {x:5.1f},{y:5.1f}, scaled {sx:5.1f},{sy:5.1f}')

# print()
# x = 0
# y = fy(x, m, b)
# sx, sy = scale_and_offset(x, y, scale_x, scale_y)
# print(f'x,y {x:5.1f},{y:5.1f}, scaled {sx:5.1f},{sy:5.1f}')
# x = 1
# y = fy(x, m, b)
# sx, sy = scale_and_offset(x, y, scale_x, scale_y)
# print(f'x,y {x:5.1f},{y:5.1f}, scaled {sx:5.1f},{sy:5.1f}')
# x = -1
# y = fy(x, m, b)
# sx, sy = scale_and_offset(x, y, scale_x, scale_y)
# print(f'x,y {x:5.1f},{y:5.1f}, scaled {sx:5.1f},{sy:5.1f}')
# x = -1
# y = fy(x, m, b)
# sx, sy = scale_and_offset(x, y, scale_x, scale_y, 64, 32)
# print(f'x,y {x:5.1f},{y:5.1f}, scaled {sx:5.1f},{sy:5.1f}')
