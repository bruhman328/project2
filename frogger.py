import os
root, directories, files = next(os.walk('.'))


UP = 'W'
LEFT = 'A'
DOWN = 'S'
RIGHT = 'D'
JUMP = 'J'
FROG = '\U0001318F'

def frogger_game(game_file):
   


def select_game_file():
   print("""[1]  	game1.frog
            [2]  	game2.frog
            [3]  	game3.frog
         """)
   file_selection = int(input('Enter an option or filename: '))
   board_lines = [[],
                  [],
                  []]
   if file_selection == 1 or file_selection == 'game1.frog':
      line = open("game1.frog", "r")
      for i in board_lines:
         for j in line[2:]:
            i.append(j.strip())
   elif file_selection == 2 or file_selection == 'game2.frog':
      line = open("game2.frog", "r")
      for i in board_lines:
         for j in line[2:]:
            i.append(j.strip())
   elif file_selection == 3 or file_selection == 'game3.frog':
      line = open("game3.frog", "r")
      for i in board_lines:
         for j in line[2:]:
            i.append(j.strip())
   else:
      print("Thats not a selection")
      return None
   return board_lines
   


if __name__ == '__main__':
   selected_game_file = select_game_file()
   frogger_game(selected_game_file)

