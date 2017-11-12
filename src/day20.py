from math import sqrt
from itertools import chain,filterfalse

# check if this element is at least 34000000
# 10*1 + 10*2 + 10*3 + ... = 10 (1 + 2 + 3 + ... ) >= 34000000
#    --> (1 + 2 + 3 + ...) >= 3400000

# part 1
for n in range(1, 100000000):
    if sum(chain.from_iterable([i, n//i] for i in range(1, int(sqrt(n)+ 1)) if n % i == 0)) >= 3400000:
        break
print(n)

# part 2
limit = 34000000 / 11
for n in range(1, 100000000):
    if sum(filterfalse(lambda x: n // x > 50, chain.from_iterable([i, n//i] for i in range(1, int(sqrt(n)+ 1)) if n % i == 0))) >= limit:
        break
print(n)
