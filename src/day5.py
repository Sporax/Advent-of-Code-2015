import re

filename = 'input5.txt'

txt = open(filename)
text = txt.read()

list_words = re.findall(r'[a-z]+', text)  # find all words and store in list

# search each list_word for the required hits:
""" 1. requires three vowels: [aeiou]+                      elegant soln: (.*[aeiou]){3}
    2. one letter that repeats twice in a row: ([a-z])\1    elegant soln: (.)\1
    3. Does *not* contain ab, cd, pq or xy: ab|cd|pq|xy     elegant soln: (ab|cd|pq|xy) """
count = 0

for word in list_words:
    if len(re.findall("ab|cd|pq|xy", word)) == 0:
        if len(re.findall(r'([a-z])\1', word)) > 0:
            if len(re.findall('[aeiou]', word)) > 2:
                # print('Hit, string: ', word)
                count += 1
print(count)

# part 2
""" 1. sequence of two letters repeated twice in a string: \w*([a-z]{2})\w*\1
    2. sandwich sequence (eg. axa): a[a-z]a|b[a-z]b|c[a-z]c|d[a-z]d|e[a-z]e|f[a-z]f|g[a-z]g|h[a-z]h|i[a-z]i|j[a-z]j|k[a-z]k|l[a-z]l|m[a-z]m|n[a-z]n|o[a-z]o|p[a-z]p|q[a-z]q|r[a-z]r|s[a-z]s|t[a-z]t|u[a-z]u|v[a-z]v|w[a-z]w|x[a-z]x|y[a-z]y|z[a-z]z

    elegant solutions:
    1. (..).*\1
    2. (.).\1 """

count = 0
for word in list_words:
    if len(re.findall(r'(..).*\1', word)) > 0:
        if len(re.findall(r'(.).\1', word)) > 0:
            # print('Hit, string: ', word)
            count += 1
print(count)
