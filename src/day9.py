import re
from itertools import permutations

distances = {}
abbrs = ''

# read file and store key of uppercase letters in dictionary
text = open('input9.txt').read()
cities = re.findall('[A-Z]', text)
cities = [cities[i]+cities[i+1] for i in range(0, len(cities), 2)]
dist = re.findall(r'\d+', text)

# store values in dict
for i in range(len(cities)):
    distances[cities[i]] = int(dist[i])
    # store the first letter if not already in string for permutations
    if cities[i][0] not in abbrs:
        abbrs  += cities[i][0]
    # also store reverse
    cities[i] = cities[i][::-1]
    distances[cities[i]] = int(dist[i])
    if cities[i][0] not in abbrs:
        abbrs += cities[i][0]

# store prices for travel
prices = []

# find permutations and calculate total distances
for p in permutations(abbrs):
    price = 0
    for i in range(1, len(p)):
        # print(p[i-1], p[i]),
        locs = p[i-1] + p[i]
        locs.replace(' ', '')
        price += distances[locs]
        # print(locs, price)
    prices.append(price)

# find cheapest one
prices.sort()
'''part 1'''
print('part 1: ', prices[0])
'''part 2'''
print('part 2: ', prices[-1])
