from panel import Panel


class Foo(Panel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
        s.run()
    except KeyboardInterrupt:
        s.clear()
