import os

root, directories, files = next(os.walk('.'))

UP = 'W'
LEFT = 'A'
DOWN = 'S'
RIGHT = 'D'
JUMP = 'J'
FROG = '\U0001318F'

def frogger_game(file):

    pos_input = input('WASDJ')
    for i in file[0:2]:
        print(i)
    for i in file[2:]:
        print(i)

     
def select_game_file():
    print("""
            [1]  	game1.frog
            [2]  	game2.frog
            [3]  	game3.frog
         """)
    file_selection = input('Enter an option or filename: ')
    board = []
    if file_selection == '1' or file_selection == 'game1.frog':
        with open('game1.frog', 'r') as file:
            board_lines = file.readlines()
            line = board_lines[0].split()
            lining = list(int(num) for num in line)
            board.append(lining)

            line1 = board_lines[1].split()
            lining1 = list(int(num) for num in line1)
            board.append(lining1)
            board.append([])

            new_row = []
            for i in range(2, len(board_lines)):  
                row = list(board_lines[i].strip())
                new_row.append(row)

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
            board.append([])

            new_row = []
            for i in range(2, len(board_lines)):  
                row = list(board_lines[i].strip())
                new_row.append(row)

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
            board.append([])
            
            new_row = []
            for i in range(2, len(board_lines)):  
                board_row = list(board_lines[i].strip())
                new_row.append(board_row)

            board.append(new_row)
    else:
        return "Not a selection"

    for i in range(board[0][1]):
        board[2].append(' ')
    board[2][len(board[2]) // 2] = FROG

    return board


if __name__ == '__main__':
    select = select_game_file()
    frogger_game(select)
    #print(frogger_game(select))
