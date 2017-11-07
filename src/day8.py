import re

# # input file
# text = open('input8.txt').read()
# text_store = re.findall(r'.+', text)

print('part 1: ', sum(len(s[:-1]) - len(eval(s)) for s in open('input8.txt')))
print('part 2: ', sum(2+s.count('\\')+s.count('"') for s in open('input8.txt')))
