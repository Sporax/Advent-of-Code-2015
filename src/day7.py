import re
from pprint import pprint

dictionary = {}
instructions = []

''' for part b, change input in text file of '19138 -> b' to '2797 -> b' '''

text = open('input7.txt').read()
text_store = re.findall('.+', text, re.I)

# initialize instructions
for i in range(len(text_store)):
    instructions.append(False)

# loop each line
cond = False
i = 0
while not cond:
    line = text_store[i]
    # print(line)

    # if true, skip instruction
    if instructions[i]:
        # check if all instructions are true
        count = 0
        for j in range(len(text_store)):
            if instructions[j]:
                count += 1
        if count == 339:
            cond = True
            break
        i += 1
        if i == 339:
            i = 0
        continue

    # AND
    if re.search('AND', line):
        # store three variables and check if first two have values
        var = re.findall('[a-z]+', line)
        if len(var) > 2:
            if var[0] in dictionary and var[1] in dictionary:
                dictionary[var[2]] = dictionary[var[0]] & dictionary[var[1]]
                if dictionary[var[2]] < 0:
                    dictionary[var[2]] += 65536
                instructions[i] = True
            # print(dictionary[var[0]], " ", dictionary[var[1]], " ", dictionary[var[0]] & dictionary[var[1]])
        elif len(var) == 2:
            if var[0] in dictionary:
                num = int(re.search(r'\d+', line).group())
                dictionary[var[1]] = dictionary[var[0]] & num
                if dictionary[var[1]] < 0:
                    dictionary[var[1]] += 65536
                instructions[i] = True

    # OR
    elif re.search('OR', line):
        # store three variables and check if first two have values
        var = re.findall('[a-z]+', line)
        if var[0] in dictionary and var[1] in dictionary:
            dictionary[var[2]] = dictionary[var[0]] | dictionary[var[1]]
            if dictionary[var[2]] < 0:
                dictionary[var[2]] += 65536
            instructions[i] = True
            # print(dictionary[var[0]], " ", dictionary[var[1]], " ", dictionary[var[0]] | dictionary[var[1]])

    # LSHIFT
    elif re.search('LSHIFT', line):
        # store three variables and check if first two have values
        var = re.findall('[a-z]+', line)
        num = int(re.search(r'\d+', line).group())
        if var[0] in dictionary:
            dictionary[var[1]] = dictionary[var[0]] << num
            if dictionary[var[1]] < 0:
                dictionary[var[1]] += 65536
            instructions[i] = True
            # print(dictionary[var[0]], " ", dictionary[var[1]], " ", dictionary[var[0]] << num)

    # RSHIFT
    elif re.search('RSHIFT', line):
        # store three variables and check if first two have values
        var = re.findall('[a-z]+', line)
        num = int(re.search(r'\d+', line).group())
        if var[0] in dictionary:
            dictionary[var[1]] = dictionary[var[0]] >> num
            if dictionary[var[1]] < 0:
                dictionary[var[1]] += 65536
            instructions[i] = True
            # print(dictionary[var[0]], " ", dictionary[var[1]], " ", dictionary[var[0]] >> num)

    # NOT
    elif re.search('NOT', line):
        # store three variables and check if first two have values
        var = re.findall('[a-z]+', line)
        if var[0] in dictionary:
            dictionary[var[1]] = ~dictionary[var[0]]
            if dictionary[var[1]] < 0:
                dictionary[var[1]] += 65536
            instructions[i] = True
            # print(dictionary[var[0]], " ", dictionary[var[1]])

    # ASSIGN (-->)
    else:
        # assign value to variable in dictionary
        var = re.findall('[a-z]+', line)
        if len(var) == 1:
            num = int(re.search(r'\d+', line).group())
            dictionary[var[0]] = num
            instructions[i] = True
            # print(dictionary[var[0]], ' ', num)
        elif len(var) == 2:
            if var[0] in dictionary:
                dictionary[var[1]] = dictionary[var[0]]
                instructions[i] = True
                # print(dictionary[var[0]], ' ', dictionary[var[1]])
    i += 1
    if i == 339:
        i = 0
    count = 0
#    print(len(dictionary))
    # for item in dictionary:
    #     if dictionary[item] > 0:
    #         count += 1
    # # pprint(dictionary)

print(dictionary["a"])
