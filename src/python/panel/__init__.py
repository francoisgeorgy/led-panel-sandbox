import importlib
import io
import argparse

from color import Color

MODE_OVERWRITE = 0
MODE_XOR = 1


def is_raspberrypi():
    try:
        with io.open('/sys/firmware/devicetree/base/model', 'r') as m:
            if 'raspberry pi' in m.read().lower():
                return True
    except Exception:
        pass
    return False


running_on_pi = is_raspberrypi()

# Dynamically import the appropriate module
if running_on_pi:
    rgb_matrix_lib = importlib.import_module('rgbmatrix')
    rgb_graphics = importlib.import_module('rgbmatrix.graphics')
else:
    rgb_matrix_lib = importlib.import_module('RGBMatrixEmulator')
    rgb_graphics = importlib.import_module('RGBMatrixEmulator.graphics')


class Panel:
    def __init__(self, *args, **kwargs):

        self.matrix = None
        self.canvas = None
        self.parser = argparse.ArgumentParser()

        # arguments common to RPi and emulator :
        self.parser.add_argument("-r", "--led-rows", action="store",
                                 help=f"Display rows. 16 for 16x32, 32 for 32x32. Default: 64", default=64, type=int)
        self.parser.add_argument("-l", "--led-cols", action="store",
                                 help=f"Panel columns. Typically 32 or 64. (Default: 128)", default=128, type=int)
        self.parser.add_argument("--led-show-refresh", action="store_true",
                                 help="Shows the current refresh rate of the LED panel")

        if running_on_pi:
            self.parser.add_argument("-c", "--led-chain", action="store",
                                     help=f"Daisy-chained boards. Default: 1.", default=1, type=int)
            self.parser.add_argument("-P", "--led-parallel", action="store",
                                     help=f"For Plus-models or RPi2: parallel chains. 1..3. Default: 1",
                                     default=1, type=int)
            self.parser.add_argument("-b", "--led-brightness", action="store",
                                     help=f"Sets brightness level. Default: 66. Range: 1..100",
                                     default=66, type=int)
            self.parser.add_argument("-p", "--led-pwm-bits", action="store",
                                     help="Bits used for PWM. Something between 1..11. Default: 11", default=11,
                                     type=int)
            self.parser.add_argument("-m", "--led-gpio-mapping",
                                     help="Hardware Mapping: regular, adafruit-hat, adafruit-hat-pwm",
                                     choices=['regular', 'regular-pi1', 'adafruit-hat', 'adafruit-hat-pwm'], type=str)
            self.parser.add_argument("--led-scan-mode", action="store",
                                     help="Progressive or interlaced scan. 0 Progressive, 1 Interlaced (default)",
                                     default=1, choices=range(2), type=int)
            self.parser.add_argument("--led-pwm-lsb-nanoseconds", action="store",
                                     help="Base time-unit for the on-time in the lowest significant bit in nanoseconds. Default: 130",
                                     default=130, type=int)
            self.parser.add_argument("--led-slowdown-gpio", action="store",
                                     help=f"Slow down writing to GPIO. Range: 0..5. Default: 4", default=4, type=int)
            self.parser.add_argument("--led-no-hardware-pulse", action="store",
                                     help="Don't use hardware pin-pulse generation")

            self.parser.add_argument("--led-rgb-sequence", action="store",
                                     help="Switch if your matrix has led colors swapped. Default: RGB", default="RGB",
                                     type=str)

            self.parser.add_argument("--led-pixel-mapper", action="store", help=f"Apply pixel mappers. Default: \"\"",
                                     default="", type=str)
            self.parser.add_argument("--led-row-addr-type", action="store",
                                     help="0 = default; 1=AB-addressed panels; 2=row direct; 3=ABC-addressed panels; 4 = ABC Shift + DE direct",
                                     default=0, type=int, choices=[0, 1, 2, 3, 4])
            self.parser.add_argument("--led-multiplexing", action="store",
                                     help="Multiplexing type: 0=direct; 1=strip; 2=checker; 3=spiral; 4=ZStripe; 5=ZnMirrorZStripe; 6=coreman; 7=Kaler2Scan; 8=ZStripeUneven... (Default: 0)",
                                     default=0, type=int)
            self.parser.add_argument("--led-panel-type", action="store",
                                     help="Needed to initialize special panels. Supported: 'FM6126A'", default="",
                                     type=str)
            self.parser.add_argument("--led-no-drop-privs", dest="drop_privileges",
                                     help="Don't drop privileges from 'root' after initializing the hardware.",
                                     action='store_false')
            self.parser.set_defaults(drop_privileges=True)
        else:
            self.parser.add_argument("-c", "--led-chain", action="store",
                                     help=f"Daisy-chained boards. Default: 1.",
                                     default=1, type=int)
            self.parser.add_argument("-P", "--led-parallel", action="store",
                                     help=f"For Plus-models or RPi2: parallel chains. 1..3. Default: 1",
                                     default=1, type=int)
            self.parser.add_argument("-b", "--led-brightness", action="store",
                                     help=f"Sets brightness level. Default: 100. Range: 1..100",
                                     default=100, type=int)

        if kwargs['add_args']:
            for a in kwargs['add_args']:
                self.parser.add_argument(a['name'], help=a['help'], default=a['default'], type=a['type'])

        self.args = self.parser.parse_args()

        options = rgb_matrix_lib.RGBMatrixOptions()

        options.rows = self.args.led_rows
        options.cols = self.args.led_cols
        options.chain_length = self.args.led_chain
        options.parallel = self.args.led_parallel
        options.brightness = self.args.led_brightness
        options.show_refresh_rate = 1 if self.args.led_show_refresh else 0

        if running_on_pi:
            options.hardware_mapping = self.args.led_gpio_mapping
            options.row_address_type = self.args.led_row_addr_type
            options.multiplexing = self.args.led_multiplexing
            options.pwm_bits = self.args.led_pwm_bits
            options.pwm_lsb_nanoseconds = self.args.led_pwm_lsb_nanoseconds

            # options.led_rgb_sequence = "RGB"
            options.led_rgb_sequence = "BGR"

            options.pixel_mapper_config = self.args.led_pixel_mapper
            if self.args.led_slowdown_gpio is not None:
                options.gpio_slowdown = self.args.led_slowdown_gpio
            if self.args.led_no_hardware_pulse:
                options.disable_hardware_pulsing = True
            if not self.args.drop_privileges:
                options.drop_privileges = False
        else:
            # options.pixel_mapper_config = ""
            options.panel_type = ""
            options.show_refresh_rate = 1

        self.matrix = rgb_matrix_lib.RGBMatrix(options=options)
        self.canvas = self.matrix.CreateFrameCanvas()
        self.rw_canvas = [[[0, 0, 0] for i in range(self.canvas.width)] for j in range(self.canvas.height)]
        self.x_max = self.canvas.width-1
        self.y_max = self.canvas.height-1
        self.width = self.canvas.width
        self.height = self.canvas.height

    def clear(self):
        self.canvas.Clear()
        self.rw_canvas = [[[0, 0, 0] for i in range(self.canvas.width)] for j in range(self.canvas.height)]

    def refresh(self):
        self.canvas = self.matrix.SwapOnVSync(self.canvas)

    def pixel(self, x, y, color, mode=MODE_OVERWRITE):
        if x < 0 or x > self.x_max or y < 0 or y > self.y_max:
            return
        if mode == MODE_OVERWRITE:
            self.canvas.SetPixel(x, y, color.red, color.green, color.blue)
            try:
                self.rw_canvas[y][x] = [color.red, color.green, color.blue]
            except IndexError as e:
                print(f'index error: [{y}][{x}]', len(self.rw_canvas), len(self.rw_canvas[0]))
        elif mode == MODE_XOR:
            # Does not change the rw_canvas pixel
            c = self.get_pixel(x, y)
            self.canvas.SetPixel(x, y, color.red ^ c[0], color.green ^ c[1], color.blue ^ c[2])
        else:
            raise ValueError('Unsupported pixel mode')

    def get_pixel(self, x: int, y: int) -> tuple[int, int, int]:
        return self.rw_canvas[y][x]

    # def line0(self, x0, y0, x1, y1, color, mode=MODE_OVERWRITE):
    #     # rgb_graphics.DrawLine(self.canvas, x0, y0, x1, y1, color)
    #     # see https://github.com/ty-porter/RGBMatrixEmulator/blob/main/RGBMatrixEmulator/graphics/__init__.py#L75 as example
    #     '''
    #     Line drawing algorithm
    #
    #     Extracted from scikit-image:
    #     https://github.com/scikit-image/scikit-image/blob/00177e14097237ef20ed3141ed454bc81b308f82/skimage/draw/_draw.pyx#L44
    #
    #     Generate line pixel coordinates.
    #
    #     Parameters
    #     ----------
    #     x1, y1 : int            Starting position (row, column).
    #     x2, y2 : int            End position (row, column).
    #
    #     Returns
    #     -------
    #     rr, cc : (N,) ndarray of int
    #         Indices of pixels that belong to the line.
    #         May be used to directly index into an array, e.g.
    #         ``img[rr, cc] = 1``.
    #
    #     See Also
    #     --------
    #     line_aa : Anti-aliased line generator
    #     :param y1:
    #     :param x1:
    #     :param y0:
    #     :param x0:
    #     :param mode_xor:
    #     :param color:
    #     '''
    #     steep = 0
    #     x = x0
    #     y = y0
    #     dx = abs(x1 - x0)
    #     dy = abs(y1 - y0)
    #
    #     xi = 1 if x0 < x1 else -1
    #     # if (x1 - x) > 0:
    #     #     xi = 1
    #     # else:
    #     #     xi = -1
    #
    #     yi = 1 if y0 < y1 else -1
    #     # if (y1 - y) > 0:
    #     #     yi = 1
    #     # else:
    #     #     yi = -1
    #
    #     if dx > dy:
    #         steep = 1
    #         y, x = x, y
    #         dy, dx = dx, dy
    #         yi, xi = xi, yi
    #     d = (2 * dx) - dy
    #
    #     for i in range(dy):
    #         if steep:
    #             px, py = y, x
    #             # self.pixel(c, r, color)
    #         else:
    #             px, py = x, y
    #             # self.pixel(r, c, color)
    #
    #         pixel_color = color
    #         if mode_xor:
    #             p = self.get_pixel(px, py)
    #             if p == [color.red, color.green, color.blue]:
    #                 pixel_color = Color.BLACK()
    #
    #         self.pixel(px, py, pixel_color)
    #
    #         while d >= 0:
    #             x = x + xi
    #             d = d - (2 * dy)
    #         y = y + yi
    #         d = d + (2 * dx)
    #
    #     self.pixel(x1, y1, color)
    #
    # def line(self, x0, y0, x1, y1, color, mode=MODE_OVERWRITE):
    #     '''
    #     Line drawing algorithm
    #
    #     Source : https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
    #
    #     Parameters
    #     ----------
    #     x1, y1 : int            Starting position (row, column).
    #     x2, y2 : int            End position (row, column).
    #
    #     See Also
    #     --------
    #     line_aa : Anti-aliased line generator
    #     :param mode:
    #     :param y1:
    #     :param x1:
    #     :param y0:
    #     :param x0:
    #     :param mode_xor:
    #     :param color:
    #     '''
    #     x = x0
    #     y = y0
    #     xi = 1 if x0 < x1 else -1
    #     yi = 1 if y0 < y1 else -1
    #     dx = abs(x1 - x0)
    #     dy = -abs(y1 - y0)
    #     error = dx + dy
    #     while True:
    #         self.pixel(x, y, color, mode)
    #         if x == x1 and y == y1:
    #             break
    #         e2 = 2 * error
    #         if e2 >= dy:
    #             if x == x1:
    #                 break
    #             error = error + dy
    #             x = x + xi
    #         if e2 <= dx:
    #             if y == y1:
    #                 break
    #             error = error + dx
    #             y = y + yi

    # def rectangle(self, x, y, w, h, color, fill=False, mode=MODE_OVERWRITE):
    #     if w == 1 and h == 1:
    #         self.pixel(x, y, color, mode, mode)
    #     elif fill:
    #         for v in range(h):
    #             self.line(x, y+v, x+w-1, y+v, color, mode)
    #     else:
    #         self.line(x, y, x+w-1, y, color, mode)
    #         self.line(x+w-1, y, x+w-1, y+h-1, color, mode)
    #         self.line(x, y+h-1, x+w-1, y+h-1, color, mode)
    #         self.line(x, y, x, y+h-1, color, mode)

    # def rectangle(self, x0, y0, x1, y1, color, fill=False, mode=MODE_OVERWRITE):
    #     if x1 - x0 == 1 and y1 - y0 == 1:
    #         self.pixel(x0, y0, color, mode)
    #     elif fill:
    #         for y in range(y0, y1 + 1):
    #             self.line(x0, y, x1, y, color, mode)
    #     else:
    #         self.line(x0, y0, x1, y1, color, mode)
    #         self.line(x1, y0, x1, y1, color, mode)
    #         self.line(x0, y1, x0, y1, color, mode)
    #         self.line(x0, y0, x0, y1, color, mode)

    # def run(self):
    #     print("Running")

    # def process(self):
    #     self.args = self.parser.parse_args()
    #
    #     options = RGBMatrixOptions()
    #
    #     if self.args.led_gpio_mapping is not None:
    #         options.hardware_mapping = self.args.led_gpio_mapping
    #     options.rows = self.args.led_rows
    #     options.cols = self.args.led_cols
    #     options.chain_length = self.args.led_chain
    #     options.parallel = self.args.led_parallel
    #     options.row_address_type = self.args.led_row_addr_type
    #     options.multiplexing = self.args.led_multiplexing
    #     options.pwm_bits = self.args.led_pwm_bits
    #     options.brightness = self.args.led_brightness
    #     options.pwm_lsb_nanoseconds = self.args.led_pwm_lsb_nanoseconds
    #     options.led_rgb_sequence = self.args.led_rgb_sequence
    #     options.pixel_mapper_config = self.args.led_pixel_mapper
    #     options.panel_type = self.args.led_panel_type
    #
    #     if self.args.led_show_refresh:
    #         options.show_refresh_rate = 1
    #
    #     if self.args.led_slowdown_gpio != None:
    #         options.gpio_slowdown = self.args.led_slowdown_gpio
    #     if self.args.led_no_hardware_pulse:
    #         options.disable_hardware_pulsing = True
    #     if not self.args.drop_privileges:
    #         options.drop_privileges = False
    #
    #     self.matrix = RGBMatrix(options=options)
    #
    #     try:
    #         # Start loop
    #         print("Press CTRL-C to stop sample")
    #         self.run()
    #     except KeyboardInterrupt:
    #         print("Exiting\n")
    #         sys.exit(0)
    #
    #     return True
