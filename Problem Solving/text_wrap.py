import textwrap

def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width))

result = wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4)
print(result)