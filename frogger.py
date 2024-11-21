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

def move(file, frog):
    pos_input = input('WASDJ')
    for i in range(file[2]):
        for j in range(i):
            if pos_input.upper() == 'W':
                if i == 0 or frog[i - 1][j] == 'X':  
                    return 'You cannot move up'
                elif i != 0 or frog[i - 1][j] != 'X':
                    return move(file, frog[i - 1][j])
                
            if pos_input.upper() == 'A':
                if j == 0 or frog[i][j - 1] == 'X':  
                    return 'You cannot move left'
                elif i != 0 or frog[i][j - 1] != 'X':
                    return move(file, frog[i][j - 1])
                
            if pos_input.upper() == 'S':
                if frog[i + 1][j] == 'X':  
                    return 'You cannot move down'
                elif frog[i + 1][j] != 'X':
                    return move(file, frog[i + 1][j])
            
            if pos_input.upper() == 'D':
                if j == (len(i) - 1) or frog[i][j + 1] == 'X':
                    return 'You cannot move right'
                elif j != (len(i) - 1) or frog[i][j + 1] != 'X':
                    return move(file, frog[i][j + 1])
            if 'J' in pos_input.upper():
                if file[0][2] == 0:
                    return 'You cannot jump anymore'
                elif file[0][2] != 0:
                    jump_input = pos_input.split()
                    if int(jump_input[1]) > frog[i + 1]:
                        return 'You cannot jump that far'

                    

                
    
    pos_input = input('WASDJ')

    if pos_input.upper() == 'W':
        if pos[]
   
    
  


def frogger_game(file):
    pos_input = input('WASDJ')
    # for i in file[0:3]:
    #     print(i)
    
    # for i in file[2][::]:
    #     print(' '.join(i))
    display_board(file)
     
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
