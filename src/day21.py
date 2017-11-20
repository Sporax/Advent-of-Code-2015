from math import ceil
from itertools import combinations
# start by defining categories
# [cost, damage, armor]
weapons = [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]]
armor = [[0, 0, 0], [13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5]]
rings = [[0, 0, 0], [0, 0, 0], [25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]]
# add 0 attribute armor and rings because you can select no armor, no rings or only one ring

# select one weapon, one armor, zero rings
my = {'hp': 100, 'attack': 0, 'defense': 0}
boss = {'hp': 103, 'attack': 9, 'defense': 2}

mincost = 1000
maxcost = 0  # part 2
for weapon in weapons:
    for arm in armor:
        for r1,r2 in combinations(rings,2):
            # winning condition: (boss hp) / (max(1, my dmg - boss shield)) <= (my hp) / (max(1, boss dmg - my shield))
            cost = weapon[0]+arm[0]+r1[0]+r2[0]
            if ceil(boss['hp'] / max(1, (weapon[1]+arm[1]+r1[1]+r2[1]) - boss['defense'])) <= ceil(my['hp'] / max(1, boss['attack'] - (weapon[2]+arm[2]+r1[2]+r2[2]))):
                if cost < mincost:
                    mincost = cost
            else:  # losing condition, part 2
                if cost > maxcost:
                    maxcost = cost

print(mincost)
print(maxcost)
