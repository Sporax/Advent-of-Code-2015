# recursive backtracking algorithm
# could use something else, but the tree has a maxdepth of 50, so shouldn't be too inefficient
cost = [53, 73, 113, 173, 229]

def findpath():
    # start recursion
    min_used = 1000000
    for i in range(5):
        tmp = helper(cost[i], str(i), 500 - cost[i], 50, 55, 0, 0, 0)
        if tmp < min_used:
            min_used = tmp
    return min_used

def helper(mana_used, path, mana, hp, boss_hp, shield, poison, recharge):
    # start user turn
#    print(path)
    hp -= 1
    if hp <= 0:
        return -1
    if poison:
        boss_hp -= 3
        poison -= 1
        if boss_hp <= 0:
            if mana_used == 1295:
                print(mana_used, path, hp)
            return mana_used
    if recharge:
        mana += 101
        recharge -= 1
    if shield:
        shield -= 1
    # user action
    if path[-1] == '0':
        boss_hp -= 4
    elif path[-1] == '1':
        boss_hp -= 2
        hp += 2
    elif path[-1] == '2':
        shield = 6
    elif path[-1] == '3':
        poison = 6
    elif path[-1] == '4':
        recharge = 5
    # boss turn
    if poison > 0:
        boss_hp -= 3
        poison -= 1
    if boss_hp <= 0:
        if mana_used == 1295:
            print(mana_used, path, hp)
        return mana_used
    if recharge > 0:
        mana += 101
        recharge -= 1
    if shield > 0:
        hp -= 1
        shield -= 1
    else:
        hp -= 8
    # check if player is alive
    if hp <= 0 or mana < 53:
        return -1
    
    min_used = 10000
    for i in range(5):
        if (i == 2 and shield > 0) or (i == 3 and poison > 0) or (i == 4 and recharge > 0):
            # can't stack actions
            continue
        tmp = helper(mana_used + cost[i], path + str(i), mana - cost[i], hp, boss_hp, shield, poison, recharge)
        if tmp != -1 and tmp < min_used:
            min_used = tmp
    return min_used

print(findpath())
        
