import re

pswd = 'hepxcrrq'
pswd = pswd[::-1]
condition = False


def increment(string, index):
    """ increments the character at given index """
    if string[index] == 'z':
        string = string[:index] + 'a' + string[index+1:]
        return increment(string, index + 1)
    else:
        if string[index] in ['h', 'n', 'k']:
            a = chr(ord(string[index]) + 2)  # skip these chars
        else:
            a = chr(ord(string[index]) + 1)
        string = string[:index] + a + string[index+1:]
    return string

count = 0
while not condition:
    # increment the last letter
    pswd = increment(pswd, 0)
    if pswd.__contains__('o') or pswd.__contains__('l') or pswd.__contains__('i'):  # skip these letters
        pswd = increment(pswd, 0)
        continue
    check_pswd = pswd[::-1]
    if re.search(r'([a-z])\1\w*([a-z])\2', check_pswd):  # contains one repitition
        for i in range(2, len(check_pswd)):
            if ord(check_pswd[i-1]) - ord(check_pswd[i-2]) == ord(check_pswd[i]) - ord(check_pswd[i-1]) == 1:
                print(check_pswd)
                count += 1
                if count == 2:
                    exit()
