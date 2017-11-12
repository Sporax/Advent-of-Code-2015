from itertools import combinations

containers = [33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42]

result = 0

# find the minimum size
min_size = len(containers)
for l in range(1, len(containers)):
    for c in combinations(containers, l):
        if sum(c) == 150:
            if l < min_size:
                min_size = l
            result += 1

print(result)

# part 2
result = 0
for c in combinations(containers, min_size):
    if sum(c) == 150:
        result += 1
print(result)
