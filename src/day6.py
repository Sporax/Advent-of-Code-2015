import re

# check if all first nos are less than second nos.

s = open('input6.txt').read()
store = re.findall(r'\d+', s)  # store all integers
command = re.findall(r'(turn on|turn off|toggle)', s, re.I)  # store all commands
#print(len(command))

# convert all numbers to int format
for i in range(0, len(store)):
    store[i] = int(store[i])

board = []
# set up board
for i in range(1000):
    board.append([])
    for j in range(1000):
        board[i].append(0)


# define turn on
def turn_on(x_temp, y_temp):
    # print x_temp, y_temp
    for i in range(x_temp[0], x_temp[1] + 1):
        for j in range(y_temp[0], y_temp[1] + 1):
            board[i][j] += 1  # for part 1, change to '= 1'


# turn off
def turn_off(x_temp, y_temp):
    for i in range(x_temp[0], x_temp[1] + 1):
        for j in range(y_temp[0], y_temp[1] + 1):
            if board[i][j] > 0:    # comment out these three lines for part 1
                board[i][j] -= 1   #
            else:                  #
                board[i][j] = 0


# toggle
def toggle(x_temp, y_temp):
    for i in range(x_temp[0], x_temp[1] + 1):
        for j in range(y_temp[0], y_temp[1] + 1):
            # if board[i][j] == 1:
            #     board[i][j] = 0
            # else:
            #     board[i][j] = 1
            board[i][j] += 2

# check if all numbers are less than second numbers
def test():
    for i in range(0, len(store), 4):
        x = []
        y = []
        x.append(store[i])
        x.append(store[i + 2])
        y.append(store[i + 1])
        y.append(store[i + 3])
        # print command[i / 4], x, y

        if command[i // 4] == 'turn on':
            # print command[i / 4], x, y
            turn_on(x, y)
        elif command[i // 4] == 'turn off':
            turn_off(x, y)
        elif command[i // 4] == 'toggle':
            toggle(x, y)
        # # test
        # if x[0] > x[1] or y[0] > y[1]:
        #     cond = False
        #     print i
    # print cond

test()

# count squares that are on
count = 0
for row in range(0, 1000):
    for column in range(0, 1000):
        if board[row][column] > 0:
            count += board[row][column] # change to '+= 1' for part 1

print(count)
