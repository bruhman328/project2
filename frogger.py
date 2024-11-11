import os

root, directories, files = next(os.walk('.'))

UP = 'W'
LEFT = 'A'
DOWN = 'S'
RIGHT = 'D'
JUMP = 'J'
FROG = '\U0001318F'


def select_game_file():
    print("""
            [1]  	game1.frog
            [2]  	game2.frog
            [3]  	game3.frog
         """)
    file_selection = int(input('Enter an option or filename: '))
    board = [[], [], []]
    if file_selection == 1 or file_selection == 'game1.frog':
        with open('game1.frog', 'r') as lines:
            board_lines = lines.readlines()
        for line in board_lines[0]:
            for lining in line.strip():
                if lining == 15:
                    board[0].append(15)
                else:
                    board[0].append(int(lining))
    elif file_selection == 2 or file_selection == 'game2.frog':
        with open('game2.frog', 'r') as lines:
            board_lines = lines.readlines()
        for line in board_lines:
            board.append(line.strip())
    elif file_selection == 3 or file_selection == 'game3.frog':
        with open('game3.frog', 'r') as lines:
            board_lines = lines.readlines()
        for line in board_lines:
            board.append(line.strip())
    else:
        print("Not a selection")
        return None

    return board


if __name__ == '__main__':
    print(select_game_file())
    # print(frogger_game(selected_game_file))
