input_text = open('input1.txt').read()

countLeft = 0
countRight = 0

# part 1
print('part1: ', input_text.count('(') - input_text.count(')'))

# part 2 
i = 0
while i < len(input_text):
    if input_text[i] == '(':
        countLeft += 1
    else:
        countRight += 1
    if countLeft-countRight == -1:
        break
    i += 1


count = countLeft - countRight

print('part2: ', str(i+1))
