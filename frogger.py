import os

root, directories, files = next(os.walk('.'))    # dont know how to use this but program still works 

UP = 'W'
LEFT = 'A'
DOWN = 'S'
RIGHT = 'D'
JUMP = 'J'
FROG = '\U0001318F'

def display_board(file):
    for i in file[2][::]:
        print(i)
        print()
    

def cars(file, speed):
    display_board(file)

    return file[speed:] + file[:speed]
    

def move(file, frog_pos, jumps):
    direction = input('WASDJ')
    row_pos = frog_pos[0]
    col_pos = frog_pos[1]
    new_row_pos = row_pos
    new_col_pos = col_pos

    if direction == UP:
        if row_pos != 0 or file[row_pos - 1][col_pos] != 'X':
            new_row_pos -= 1
        elif row_pos == 0 or file[row_pos - 1][col_pos] == 'X':
            return 'You cant move up'
    elif direction == DOWN:
        if file[row_pos + 1][col_pos] != 'X':
            new_row_pos += 1
        elif file[row_pos + 1][col_pos] == 'X':
            return 'You cant move down'
    elif direction == LEFT:
        if col_pos != 0 or file[row_pos][col_pos - 1] != 'X':
            new_col_pos -= 1
        elif col_pos == 0 or file[row_pos][col_pos - 1] == 'X':
            return 'You cant move left'
    elif direction == RIGHT:
        if col_pos != file[0][1] or file[row_pos][col_pos + 1] != 'X':
            new_col_pos += 1
        elif col_pos == file[0][1] or file[row_pos][col_pos + 1] == 'X':
            return 'You cant move right'
    elif JUMP in direction:
        splitted = direction.split()
        if (int(splitted[1]) > (new_col_pos + 1) or int(splitted[1]) < (new_col_pos - 1)) and file[splitted[1][splitted[2]]] == 'X' or jumps == 0:
            return 'You cant jump anymore'
        elif (int(splitted[1]) == (new_col_pos + 1) or int(splitted[1]) == (new_col_pos - 1)) and file[splitted[1][splitted[2]]] != 'X' or jumps != 0:
            new_row_pos = splitted[1]
            new_col_pos = splitted[2]
            jumps -= 1
    if new_row_pos == (len(file[2]) - 1):
        print('The frog has lived to see another day')
        return False
    frog_pos[0] = new_row_pos
    frog_pos[1] = new_col_pos
    return frog_pos



def frogger_game(file):
   
    frog = file[2][0][file[0][1] // 2]
  
    while True:
        move(cars(file, file[0][1]), frog, file[0][2])



     
def select_game_file():
    print("""
            [1]  	game1.frog
            [2]  	game2.frog
            [3]  	game3.frog
         """)
    file_selection = input('Enter an option or filename: ')
    board = []
    new_row = []
    start = []
    end = []

    if file_selection == '1' or file_selection == 'game1.frog':
        with open('game1.frog', 'r') as file:
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
            # if board[0][1] % 2 == 0:
            #     start.append('_')
            #     end.append('_')
            # elif board[0][1] % 2 == 1:
            #     start.remove('_')
            #     end.remove('_')
            # if board[0][1] == 3:
            #     start.remove('_')
            #     end.remove('_')
            new_row.append(start)
            for i in range(2, len(board_lines)):  
                row = list(board_lines[i].strip())
                new_row.append(row)
            new_row.append(end)
            board.append(new_row)

    elif file_selection == '2' or file_selection == 'game2.frog':
        with open('game2.frog', 'r') as file:
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
            # if board[0][1] % 2 == 0:
            #     start.append('_')
            #     end.append('_')
            # elif board[0][1] % 2 == 1:
            #     start.remove('_')
            #     end.remove('_')
            # if board[0][1] == 3:
            #     start.remove('_')
            #     end.remove('_')
            new_row.append(start)
            for i in range(2, len(board_lines)):  
                row = list(board_lines[i].strip())
                new_row.append(row)
            new_row.append(end)
            board.append(new_row)

            board.append(new_row)
    elif file_selection == '3' or file_selection == 'game3.frog':
        with open('game3.frog', 'r') as file:
            board_lines = file.readlines()
            line = board_lines[0].split()
            lining = list(int(num) for num in line)
            board.append(lining)

            line1 = board_lines[1].split()
            lining1 = list(int(num) for num in line1)
            board.append(lining1)
            # board.append([])
            
            for i in range(board[0][1]):
                start.append('_')
                end.append('_')
            
            new_row.append(start)
            for i in range(2, len(board_lines)):  
                row = list(board_lines[i].strip())
                new_row.append(row)
            new_row.append(end)
            board.append(new_row)
    else:
        return "Not a selection"
    
    board[2][0][board[0][1] // 2] = FROG
    return board


if __name__ == '__main__':
    select = select_game_file()
    frogger_game(select)
    #print(frogger_game(select))
