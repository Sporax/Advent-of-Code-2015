class Cookies:
    def __init__(self, capacity, durability, flavor, texture, calories):
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

Frosting = Cookies(4, -2, 0, 0, 5)
Candy = Cookies(0, 5, -1, 0, 8)
Butterscotch = Cookies(-1, 0, 5, 0, 6)
Sugar = Cookies(0, 0, -2, 2, 1)


def count_calories(lst, qty):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0
    for i in range(len(lst)):
        capacity += lst[i].capacity * qty[i]
        durability += lst[i].durability * qty[i]
        flavor += lst[i].flavor * qty[i]
        texture += lst[i].texture * qty[i]
        calories += lst[i].calories * qty[i]
    if capacity < 0: capacity = 0
    if durability < 0: durability = 0
    if flavor < 0: flavor = 0
    if texture < 0: texture = 0
    if calories == 500:
        return capacity * durability * flavor * texture
    else:
        return 0

cookies = [Frosting, Candy, Butterscotch, Sugar]
cals = list()

# find combinations:
for a in range(1, 101):
    for b in range(1, 101 - a): # 100 teaspoons
        for c in range(1, 101 - a - b):
            for d in range(1, 101-a-b-c):
                if (a + b + c + d) == 100:
                    qty = [a, b, c, d]
                    cals.append(count_calories(cookies, qty))

print(max(cals), cals.index(max(cals))+1)
