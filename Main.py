import os
import platform

from Enemy import Enemy
from Tile import Tile

SYSTEM = platform.system()
TEST = False

game_over = False
rows, cols = 10, 10

# player speed in tiles per turn
speed = 1
# Player x, Player y
player_x, player_y = 1, 1

# Previous x, Previous y
px, py = 0, 0

# 0 - EMPTY
# 1 - PLAYER
# 2 - ENEMY

# Generate board as an list [x][y]
board = [[Tile for i in range(cols)] for j in range(rows)]

enemy1 = Enemy()
enemies = {enemy1}


def set_charpos():
    global px, py, board, player_x, player_y
    if TEST:
        print(f'x = {player_x}, y = {player_y}\n')
    board[player_y][player_x].occupied = True
    board[player_y][player_x].state = 1
    if not board[py][px].occupied:
        board[py][px].state = 0
    px = player_x
    py = player_y


def pos():
    return player_x, player_y


def render():
    global rows, cols, board
    print('----------------------')
    for y in board:
        print(end='|')
        for x in y:
            # xi.update_state(xi)
            print(x.state, end=' ')
            # if xi.occupied:
            #     print(str(xi.state), end=' ')
            # else:
            #     print(' ', end=' ')

        print(end='|\n')
    print('----------------------', end='\n\n')


def move_up(dist):
    global rows, cols, player_y, player_x
    player_y -= dist


def move_down(dist):
    global rows, cols, player_y, player_x
    if player_y + dist < rows:
        player_y += dist


def move_left(dist):
    global rows, cols, player_y, player_x
    if player_x - dist >= 0:
        player_x -= dist


def move_right(dist):
    global rows, cols, player_y, player_x
    if player_x + dist < cols:
        player_x += dist


def attack_up(dist=1):
    global player_y, player_x, enemies
    for e in enemies:
        if player_x == e.x and player_y + dist == e.y:
            enemies.remove(e)


def attack_down(dist=1):
    global player_y, player_x, enemies
    for e in enemies:
        if player_x == e.x and player_y - dist == e.y:
            enemies.remove(e)


def attack_left(dist=1):
    global player_y, player_x, enemies
    for e in enemies:
        if player_y == e.y and player_x - dist == e.x:
            enemies.remove(e)


def attack_right(dist=1):
    global player_y, player_x, enemies
    for e in enemies:
        if player_y == e.y and player_x + dist == e.x:
            enemies.remove(e)


def clear_console():
    if SYSTEM == 'Windows':
        os.system('cls')
    elif SYSTEM == 'Linux':
        os.system('clear')
    else:
        print('\n' * 20)


def invalid():
    clear_console()
    render()
    print('Invalid move, try again')


def enemy_pos():
    global board, player_x, player_y

    for e in enemies:
        board[e.y][e.x].occupied = True
        board[e.y][e.x].state = 2
        if not board[e.prey][e.prex].occupied:
            board[e.prey][e.prex].state = 0
        e.prex = e.x
        e.prey = e.y


def enemy_move():
    global player_x, player_y
    for e in enemies:
        e.move(1, player_x, player_y)


def check_collisions():
    global player_x, player_y, enemies, board, game_over
    for e in enemies:
        if pos() == e.pos():
            render()
            game_over = True

    # Player Move Codes:
    # 0 - Up
    # 1 - Down
    # 2 - Left
    # 3 - Right

    # Player Attack Codes
    # 10 - Up
    # 11 - Down
    # 12 - Left
    # 13 - Right


def can_move(direction, dist):
    can = False
    if direction == 0:
        if player_y + dist >= 0:
            can = True
    elif direction == 1:
        if player_y - dist < rows:
            can = True
    elif direction == 2:
        if player_x - dist >= 0:
            can = True
    elif direction == 3:
        if player_y - dist > 0:
            can = True
    return can


def can_attack(direction, dist):
    can = False
    if direction == 0:
        if player_y + dist >= 0:
            can = True
    elif direction == 1:
        if player_y - dist < rows:
            can = True
    elif direction == 2:
        if player_x - dist >= 0:
            can = True
    elif direction == 3:
        if player_x + dist < cols:
            can = True
    if not can:
        invalid()
    return can


def player_action(move):
    if move == 0:
        move_up(speed)
    elif move == 1:
        move_down(speed)
    elif move == 2:
        move_left(speed)
    elif move == 3:
        move_right(speed)
    elif move == 10:
        attack_up(speed)
    elif move == 11:
        attack_down(speed)
    elif move == 12:
        attack_left(speed)
    elif move == 13:
        attack_right(speed)
    update()


def update():
    enemy_move()
    enemy_pos()
    set_charpos()
    check_collisions()
    clear_console()
    if not game_over:
        render()


# Initial update
update()


def turn():
    global game_over

    move = input(
        'Inputs are: \ns: down 1\nw: up 1\na: left 1\nd: right 1\n\nas: attack down 1\naw: attack up 1\naa: attack left '
        '1\nad: attack right 1\n')

    # Move
    if move == 'w':
        if can_move(0, speed):
            player_action(0)
    elif move == 's':
        if can_move(1, speed):
            player_action(1)
    elif move == 'a':
        if can_move(2, speed):
            player_action(2)
    elif move == 'd':
        if can_move(3, speed):
            player_action(3)
    # Attack
    elif move == 'aw':
        if can_move(10, speed):
            player_action(10)
    elif move == 'as':
        if can_move(11, speed):
            player_action(11)
    elif move == 'aa':
        if can_move(12, speed):
            player_action(12)
    elif move == 'ad':
        if can_move(13, speed):
            player_action(13)
    elif move == 'endgame':
        game_over = True
    else:
        invalid()


while not game_over:
    turn()

again = input('Game Over, play again? (Y/N): ')

if again == 'y' or again == 'Y':
    os.system('python ./Main.py')
