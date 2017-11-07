import re
from sys import argv

script = argv
filename = "input2.txt"
txt = open(filename)
print("Here's your file %r:" % filename)
# print txt.read()
input_text = txt.read()
# print input_text

p = re.findall(r'\d+', input_text)

feet = 0

print('Solve part one or part two?')
prompt = input('> ')

if prompt == '1' or prompt.lower() == 'one':
    def smallest_area(l, w, h):
        if l >= w and l >= h:  # length is the largest side
            return w * h
        elif w >= l and w >= h:  # width is the largest side
            return l * h
        else:                   # height is the largest side
            return w * l

    i = 0
    while i < len(p):
        length = int(p[i])
        width = int(p[i+1])
        height = int(p[i+2])
        feet += 2*length*width + 2*width*height + 2*height*length + smallest_area(length, width, height)
        i += 3

    print(str(feet)) # outputs the number of hits from the regex

elif prompt == '2' or prompt.lower() == 'two':
    # part 2

    def smallest_perimeter(l, w, h):
        if l >= w and l >= h:  # length is the largest side
            return 2 * (w + h)
        elif w >= l and w >= h:  # width is the largest side
            return 2 * (l + h)
        else:                   # height is the largest side
            return 2 * (w + l)

    i = 0
    while i < len(p):
        length = int(p[i])
        width = int(p[i + 1])
        height = int(p[i + 2])
        feet += length * width * height + smallest_perimeter(length, width, height)
        i += 3

    print(str(feet))  # outputs the number of hits from the regex
