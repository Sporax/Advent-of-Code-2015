def _1(a,b):
    if a == 1:
        _2(a,b)
    a = 19683*a+26623
    _3(a,b)

def _2(a,b):
    a = 19683 * a + 12228
    _3(a,b)

def _3(a,b):
    while a != 1:
        b += 1
        if a % 2 == 0:
            a //=2
        else:
            a = 3*a+1
    print(a,b)

# part 1
_1(0,0)
# part 2
_1(1,0)
