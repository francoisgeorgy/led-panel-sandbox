
def f(i, j):
    for n in range(i, j):
        yield n


def scroll_text(text, start, width):
    # exception if start > width
    i = start
    while True:
        t = ''
        for n in range(width):
            k = (i+n) % len(text)
            t = t + text[k]
        i = (i + 1) % len(text)
        yield t


# a = f(0, 10)
# t = scroll_text("0123456789", 0, 10)
t = scroll_text("0123456789", 5, 5)
while True:
    s = next(t)
    print(s)
    input()

