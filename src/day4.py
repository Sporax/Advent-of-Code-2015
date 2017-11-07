import hashlib

# store secret key
key = 'iwrupvqb'

# store append
key_append = -1

print('Solve part one or part two?')
prompt = input('> ')
check = '00000' if prompt.lower() == 'one' or prompt == '1' else '000000'

# loop until md5 hash starts with five 0s
condition = True
while condition:
    key_append += 1
    tempKey = key + str(key_append)
    m = hashlib.md5(tempKey.encode('utf-8')).hexdigest()
    condition = m[:5] != check

print(key_append)
