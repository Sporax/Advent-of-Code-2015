from collections import Counter

f = open('input18.txt')
grid = f.read()
f.close()

grid = grid.split('\n')[:-1]
padded_grid = [[0 for _ in range(102)] for __ in range(102)]

for i in range(100):
    for j in range(100):
        padded_grid[i+1][j+1] = 1 if grid[i][j] == '#' else 0

# only do ops on indices (1..100)x(1..100)
def sum_grid(index, grid):
    ''' sum the elements around but not including the index tuple '''
    i1 = index[0]
    i2 = index[1]
    return sum(grid[i1-1][i2-1:i2+2]) + grid[i1][i2-1] + grid[i1][i2+1] + sum(grid[i1+1][i2-1:i2+2])

def round(grid, part=1):
    new_grid = [[0 for _ in range(102)] for __ in range(102)]
    for i in range(1,101):
        for j in range(1,101):
            if grid[i][j]:
                if sum_grid((i,j), grid) in [2,3]:  # stays on if the sum of surrounding is 2 or 3
                    new_grid[i][j] = 1
            else:
                if sum_grid((i,j), grid) == 3:
                    new_grid[i][j] = 1
            if part == 2 and (i,j) in [(1,1), (1,100), (100,1),(100,100)]:
                new_grid[i][j] = 1
    return new_grid

part1_grid = list(padded_grid)
for i in range(100):
    part1_grid = round(part1_grid)

# convert to string and count 1s
print(Counter([y for x in part1_grid for y in x])[1])

# part 2
# corners are always on
part2_grid = list(padded_grid)
for i in range(100):
    part2_grid = round(part2_grid, 2)
print(Counter([y for x in part2_grid for y in x])[1])
