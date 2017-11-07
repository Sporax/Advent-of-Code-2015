import re, itertools

people = {}
inputfile = open('input13.txt').read()
f = [s for s in inputfile if s.isupper()]
f = [''.join([f[s-1],f[s]]) for s in range(1, len(f), 2)]
n = re.findall(r'\d+', inputfile)
negative = re.findall(r'gain|lose', inputfile)
for i in range(len(negative)):
    if negative[i] == 'lose':
        n[i] = '-' + n[i]
people = {person: int(num) for person, num in zip(f, n)}

people['YA'] = people['AY'] = 0
people['YB'] = people['BY'] = 0
people['YC'] = people['CY'] = 0
people['YD'] = people['DY'] = 0         # remove for part 1
people['YE'] = people['EY'] = 0
people['YF'] = people['FY'] = 0
people['YG'] = people['GY'] = 0
people['YM'] = people['MY'] = 0

# find different permutations of seating
permute = itertools.permutations('ABCDEFGMY', 9)  # remove Y and make 9 --> 8 for part 1
cnt = []
for p in permute:
    count = 0
    for i in range(1, len(p)):
        count += people[p[i-1]+p[i]]
        count += people[p[i]+p[i-1]]
    # last element
    count += people[p[len(p)-1]+p[0]]
    count += people[p[0]+p[len(p)-1]]
    cnt.append(count)
print(max(cnt))
