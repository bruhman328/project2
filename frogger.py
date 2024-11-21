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
        print(' '.join(i))


def move(file, frog_pos):
    direction = input('WASDJ')
    x_pos = frog_pos[0]
    y_pos = frog_pos[1]
    new_x_pos = x_pos
    new_y_pos = y_pos

    if direction == UP:
        if x_pos != 0 or file[x_pos - 1][y_pos] != 'X':
            new_x -= 1
        elif x_pos == 0 or file[x_pos - 1][y_pos] == 'X':
            return 'You cant move up'
    elif direction == DOWN:
        if x_pos != 0 or file[x_pos - 1][y_pos] != 'X':
            new_x -= 1
        elif x_pos == 0 or file[x_pos - 1][y_pos] == 'X':
            return 'You cant move up'
    elif direction == LEFT:
        new_y -= 1
    elif direction == RIGHT:
        new_y += 1
    display_board(file)
    pos_input = input('WASDJ')
    
    for i in range(len(file[2]) - 1):
        for j in range(len(file[i]) - 1):
            if pos_input.upper() == UP:
                if i == 0 or frog[i - 1][j] == 'X':  
                    return 'You cannot move up'
                elif i != 0 or frog[i - 1][j] != 'X':
                    return frog[i - 1][j]
                
            if pos_input.upper() == LEFT:
                if j == 0 or frog[i][j - 1] == 'X':  
                    return 'You cannot move left'
                elif i != 0 or frog[i][j - 1] != 'X':
                    return frog[i][j - 1]
                
            if pos_input.upper() == DOWN:
                if frog[i + 1][j] == 'X':  
                    return 'You cannot move down'
                elif frog[i + 1][j] != 'X':
                    return frog[i + 1][j]
            
            if pos_input.upper() == RIGHT:
                if j == (len(i) - 1) or frog[i][j + 1] == 'X':
                    return 'You cannot move right'
                elif j != (len(i) - 1) or frog[i][j + 1] != 'X':
                    return frog[i][j + 1]
                
            if JUMP in pos_input.upper():
                if file[0][2] == 0:
                    return 'You cannot jump anymore'
                elif file[0][2] != 0:
                    jump_input = pos_input.split()
                    if int(jump_input[1]) > (i + 1) or int(jump_input[1]) < (i - 1):
                        return 'You cannot jump that far'
                    elif int(jump_input[1]) == (i + 1) or int(jump_input[1]) == (i - 1):
                        file[0][2] -= 1
                        return frog[int(jump_input[1])][int(jump_input[2])]

            if i == len(file[2]):
                return 'The frog has lived to see another day'


def frogger_game(file):
    # for i in file[0:3]:
    #     print(i)
    
    # for i in file[2][::]:
    #     print(' '.join(i))
    frog = file[2][0][file[0][1] // 2]
    while True:
        move(file, frog)
     
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
            if board[0][1] % 2 == 1:
                start.append('_')
                end.append('_')
            elif board[0][1] % 2 == 0:
                start.remove('_')
                end.remove('_')
            if board[0][1] == 3:
                start.remove('_')
                end.remove('_')
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
            if board[0][1] % 2 == 1:
                start.append('_')
                end.append('_')
            elif board[0][1] % 2 == 0:
                start.remove('_')
                end.remove('_')
            if board[0][1] == 3:
                start.remove('_')
                end.remove('_')
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
            if board[0][1] % 2 == 1:
                start.append('_')
                end.append('_')
            elif board[0][1] % 2 == 0:
                start.remove('_')
                end.remove('_')
            if board[0][1] == 3:
                start.remove('_')
                end.remove('_')
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
