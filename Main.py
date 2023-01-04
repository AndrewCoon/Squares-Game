import sys
from random import random
import os
import platform
from Enemy import Enemy

SYSTEM = platform.system()
TEST = False

gameover = False
rows, cols = 10, 10

# Player x, Player y
px, py = 1, 1

# Previous px, Previous py
ppx, ppy = 0, 0

# 0 - EMPTY
# 1 - PLAYER
# 2 - ENEMY

# Generate board as an list [x][y]
board = [[0 for i in range(cols)] for j in range(rows)]

enemy1 = Enemy()
enemies = {enemy1}


def charpos():
    global ppx, ppy, board, px, py
    if (TEST):
        print(f'px = {px}, py = {py}\n')
    board[py][px] = 1
    board[ppy][ppx] = 0
    ppx = px
    ppy = py


def render():
    global rows, cols, board
    print('----------------------')
    for y in board:
        print(end='|')
        for x in y:
            if (x == 0):
                print(' ', end=' ')
            else:
                print(x, end=' ')
        print(end='|\n')
    print(print('----------------------'), end='\n\n')


def moveup(dist):
    global rows, cols, py, px
    if (py-dist >= 0):
        py -= dist
        return True
    else:
        return False


def movedown(dist):
    global rows, cols, py, px
    if (py+dist < rows):
        py += dist
        return True
    else:
        return False


def moveleft(dist):
    global rows, cols, py, px
    if (px-dist >= 0):
        px -= dist
        return True
    else:
        return False


def moveright(dist):
    global rows, cols, py, px
    if (px+dist < cols):
        px += dist
        return True
    else:
        return False


def clear_console():
    if (SYSTEM == 'Windows'):
        os.system('cls')
    elif (SYSTEM == 'Linux'):
        os.system('clear')


def invalid():
    clear_console()
    render()
    print('Invalid move, try again')


def enemypos():
    global board, px, py

    for e in enemies:
        board[e.y][e.x] = 2
        board[e.prey][e.prex] = 0
        e.prex = e.x
        e.prey = e.y


def enemymove():
    global px, py
    for e in enemies:
        e.move(1, px, py)


def checkcollisions():
    global px, py, enemies, board, gameover
    for e in enemies:
        if (e.x == px and e.y == py):
            render()
            gameover = True


def update():
    enemymove()
    enemypos()
    charpos()
    checkcollisions()
    clear_console()
    if not gameover:
        render()


# Initial update
update()


while (not gameover):
    move = input(
        'Inputs are: \ns: down 1\nw: up 1\na: left 1\nd: right 1\n')

    if (move == 's'):
        if (movedown(1)):
            update()
        else:
            invalid()
    elif (move == 'w'):
        if (moveup(1)):
            update()
        else:
            invalid()
    elif (move == 'a'):
        if (moveleft(1)):
            update()
        else:
            invalid()
    elif (move == 'd'):
        if (moveright(1)):
            update()
        else:
            invalid()
    elif (move == 'endgame'):
        gameover = True
    else:
        invalid()

again = input('Game Over, play again? (Y/N): ')

if (again == 'y' or again == 'Y'):
    os.system('python .\Main.py')
