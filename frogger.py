
 # Adjust for multiple rotations if needed
import os

_, _, files = next(os.walk('.')) 
UP = 'W'
LEFT = 'A'
DOWN = 'S'
RIGHT = 'D'
JUMP = 'J'
FROG = '\U0001318F'

def display_board(file):
    for i in file[:]:
        print(i)
        print()
def cars(file, speed):
    display_board(file)

    return file[2][speed:] + file[:speed]
def get_board(file):
    return file[2]

def get_frog_pos(file):
    for i in range(len(file)):
        for j in range(len(file[i])):
            if file[i][j] == FROG:
                return [i, j]
            
def move(board, frog_row, frog_col, direction, jumps):
    row_pos = frog_row
    col_pos = frog_col
    jumping = direction.split()
    if direction == UP:
        if row_pos != 0:
            row_pos -= 1
    elif direction == DOWN:
        row_pos += 1
    elif direction == LEFT:
        if col_pos != 0:
            col_pos -= 1
    elif direction == RIGHT:
        if col_pos != (len(board[1]) - 1):
            col_pos += 1
    elif JUMP in jumping:
        if jumps != 0:
            row_pos = jumping[1]
            col_pos = jumping[2]
        elif jumps == 0:
            print('You cannot jump anymore')
    board[frog_row][frog_col] = '_'
    board[row_pos][col_pos] = FROG

    return [board, frog_row, frog_col]

def select_game_file():
    for i in range(len(files)):
        print(i, files[i])
    selection = int(input(f'Enter a option 0-{len(files) - 1} '))
    
    if 0 <= selection < len(files):
        board = []
        new_row = []
        start = []
        end = []
        selection = files[selection]
        with open(selection, 'r') as file:
            board_lines = file.readlines()
            line = board_lines[0].split()
            lining = list(int(num) for num in line)
            board.append(lining)

            line1 = board_lines[1].split()
            lining1 = list(int(num) for num in line1)
            board.append(lining1)
            
            for i in range(board[0][1]):
                start.append('_')
                end.append('_')

            new_row.append(start)
            for i in range(2, len(board_lines)):  
                row = list(board_lines[i].strip())
                new_row.append(row)
            new_row.append(end)
            board.append(new_row)
    elif selection < 0 or selection > len(files) - 1:
        print('That is not a option')
        return select_game_file()
    board[2][0][board[0][1] // 2] = FROG
    
    return board


def frogger_game(file):
    for i in range(1, len(file[2]) - 1):
        file[2][i] = cars(file, file[1][i - 1])
    
    while True:

    return display_board(file)

print(display_board(get_board(select_game_file())))
# print(frogger_game(select))

# lis = ['X', 'X', 'X', '_', '_', 'X', 'X', '_', '_', '_', 'X', 'X', '_', '_', '_', '_']
# # new = cars(lis, -2)
# what = [[], [], [[1, 2, 3]]]
# what2 = what[2]
# what3 = what2[0]
# for i in what3:
#     i == 4
# print(what)

# lis2 = ['_', '_', '_', '_']
# lis2.remove('_')
# print(lis2)

FROG = '\U0001318F'

def get_frog_pos(file):
    for i in range(len(file)):
        for j in range(len(file[i])):
            if file[i][j] == FROG:
                return [i, j]
game_board = [
    ['_', '_', '_', '_', '_'],
    ['_', '_', '𓆏', '_', '_'],
    ['_', '_', '_', '_', '_']
]
