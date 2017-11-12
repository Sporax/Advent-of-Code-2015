import re

f = open('input19.txt', 'r')
finput = f.read()
f.close()

# make a dict out of input
finput = finput.split('\n')
molecule = finput[-2]
finput = finput[:-3]

transformations = dict()
for l in finput:
    l = l.split(' => ')
    if not l[0] in transformations:
        transformations[l[0]] = list()
    transformations[l[0]].append(l[1])

def single_step_transformation(input_set):
    results = set()
    for s in input_set:
        if len(s) <= len(molecule):
            # find each molecule that can be transformed, transform it, then add the result to a set
            for k in transformations.keys():
                for obj in re.finditer(k, s):
                    for v in transformations[k]:
                        results.add(s[:obj.start()] + v + s[obj.end():])
    return results

# part 1:
print(len(single_step_transformation({molecule})))

def multi_step_transformations():
    # step starting from set('e') until the desired set is reached
    steps = 0
    transformed = {'e'}
    while molecule not in transformed:
        transformed = single_step_transformation(transformed)
        steps += 1
#        print(steps,transformed)
    return steps

outputs = set(re.findall(r'[A-Z][a-z]?', ''.join([x for y in transformations.values() for x in y])))
inputs = set(transformations.keys())
print('inputs', inputs)
print('outputs', outputs)
print('diff', outputs - inputs)

# try to determine patterns:
# e -> XX
# X -> XX
# X -> X Rn X Ar, X Rn X Y X Ar, X Rn X Y X Y X Ar
## X --> X(X), X(X,X), X(X,X,X)
## X -> X(X) === X -> XX + "()"
## X -> X(X,X) === X -> XX + "()" + ",X"
## X -> X(X,X,X) == X(X n*',X') === X -> XX + "()" + n*",X"
# X -> XX takes n-1 steps to backtrack

# result = number of elements - number of parentheses - number of commas * 2 - 1
print(len(re.findall('|'.join(outputs), molecule)) - molecule.count('Ar') - molecule.count('Rn') - 2*molecule.count('Y') - 1)
# brute force is too slow
