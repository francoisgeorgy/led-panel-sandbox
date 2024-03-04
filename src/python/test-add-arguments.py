from samplebase import SampleBase
from color import Color
import time


class Foo(SampleBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add additional command line options :

        if kwargs['add_args']:
            print('add args found', kwargs['add_args'])
            for a in kwargs['add_args']:
                self.parser.add_argument(a['name'], help=a['help'], default=a['default'], type=a['type'])

        # self.parser.add_argument("--grid-size", help="Size of the grid in pixels", default=8, type=int)

    def run(self):
        print(self.args)


if __name__ == "__main__":
    s = Foo(add_args=[
        {
            'name': "--grid-size",
            'help': "Size of the grid in pixels",
            'default': 8,
            'type': int
        },
        {
            'name': "--text",
            'help': "Text to display",
            'default': '',
            'type': str
        }
    ])
    try:
        s.setup()
        s.run()
    except KeyboardInterrupt:
        s.clear()
