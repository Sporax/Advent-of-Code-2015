import re

text = '1113122113'
for x in range(50): # for part 1, replace with range(40)
    p = re.finditer(r'(\d)\1*', text)
    f = [x.group() for x in p]
    result = ''
    for i in f:
        result += str(len(i)) + i[0]
    text = result
print(len(text))

