import re

seuss = open('input16.txt').read().split('\n')
del(seuss[500])
the_real_sue = [0 for sue in seuss]
list_items = [['children: ', '3'], ['cats: ', '7'], ['samoyeds: ', '2'], ['pomeranians: ', '3'], ['akitas: ', '0'],
              ['vizslas: ', '0'], ['goldfish: ', '5'], ['trees: ', '3'], ['cars: ', '2'], ['perfumes: ', '1']]
# part 1
for i, sue in enumerate(seuss):
    # check each item
    for item in list_items:
        if re.search(item[0], sue):
            if re.search(item[0]+item[1], sue):
                the_real_sue[i] += 1
print(max(the_real_sue), the_real_sue.index(max(the_real_sue))+1)

# part 2
the_real_sue = [0 for sue in seuss]
for i, sue in enumerate(seuss):
    # check each item
    for item in list_items:
        if re.search(item[0], sue):
            if item[0] == 'cats: ' or item[0] == 'trees: ':
                if re.search(item[0]+r'(\d+)', sue):
                    p = re.search(item[0]+r'(\d+)', sue)
                    num = int(p.group(1))
                    if num > int(item[1]):
                        the_real_sue[i] += 1
            elif item[0] == 'goldfish: ' or item[0] == 'pomeranians: ':
                if re.search(item[0] + r'(\d+)', sue):
                    p = re.search(item[0] + r'(\d+)', sue)
                    num = int(p.group(1))
                    if num < int(item[1]):
                        the_real_sue[i] += 1
            else:
                if re.search(item[0]+item[1], sue):
                    the_real_sue[i] += 1
print(max(the_real_sue), the_real_sue.index(max(the_real_sue))+1)
