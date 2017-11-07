from json import loads
import re

def n(j):
    if type(j) == int:
        return j
    if type(j) == list:
        return sum([n(j) for j in j])
    if type(j) != dict:
        return 0
    if 'red' in j.values():
        return 0
    return n(list(j.values()))

text = open('input12.txt').read()
print(sum([int(d) for d in re.findall(r'-?\d+', text)])) # part 1

# part 2
print(n(loads(text)))  # credit /u/marcelzo
