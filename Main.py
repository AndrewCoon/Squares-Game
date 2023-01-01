import sys
import random

rows, cols = 10, 10

# Player x, Player y
px, py = 1, 1

# Previous px, Previous py
ppx, ppy = 0, 0

# 0 - EMPTY
# 1 - PLAYER
# 2 - ENEMY

# Generate board as an aray
board = [[0]*rows]*cols

# print(f'px = {px}, py = {py}')


def charpos():
    global ppx, ppy, board
    board[px][py] = 1
    board[ppx][ppy] = 2
    ppx = px
    ppy = py


def render():
    global rows, cols, board
    rboard = zip(*board[::-1])
    for y in rboard:
        for x in y:
            print(x, end='')
        print()


print(board[0])
print(board[1][1])

board[1][1] = 1

print(board[0])
print(board[1][1])

print(board)

# Generate Character
# charpos()

# Render initial board
# render()

rboard = zip(*board[::-1])
for y in rboard:
    for x in y:
        print(x, end='')
    print()
