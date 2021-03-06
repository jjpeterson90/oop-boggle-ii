# You should re-use and modify your old BoggleBoard class to support the new requirements

import random

class BoggleBoard:

      def __init__(self):
            self.game_board =  [ ['', '', '' ,''], ['', '', '', ''], ['', '', '', ''], ['', '', '', ''] ]
            self.display_board = [ ['', '', '' ,''], ['', '', '', ''], ['', '', '', ''], ['', '', '', ''] ]
            # self.dice = [ ['', '', '' ,''], ['', '', '', ''], ['', '', '', ''], ['', '', '', ''] ]
            self.dice = [ '', '', '' ,'', '', '', '', '', '', '', '', '', '', '', '', '' ]
            self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            self.set_initial_tiles()
            
            # initiate a dictionary of keys called 'row1'-row4, 'col1'-'col4', and diag1-2, all assigned to empty string value
            self.words_to_check = {}
            for row in range(4):
                  for col in range(4):
                        self.words_to_check[f'row{row}'] = ''
                        self.words_to_check[f'col{col}'] = ''
            self.words_to_check['diag1'] = ''
            self.words_to_check['diag2'] = ''

      # initial empty board setup
      def set_initial_tiles(self):
            for row in range(4):
                  for col in range(4):
                        self.game_board[row][col] = '_'

      # change the 6 letter values on each of the 16 dice
      def new_dice(self):
            for this_dice in range(len(self.dice)):
                  while len(self.dice[this_dice]) < 6:
                        new_letter = random.choice(self.alphabet)
                        # prevent duplicate letters on the same dice
                        if new_letter not in self.dice[this_dice]:
                              self.dice[this_dice] += random.choice(self.alphabet)
                        else:
                              new_letter = random.choice(self.alphabet)
            print(f'dice faces: \n {self.dice}')

      # shake the board - randomize which dice face is "face-up"
      def shake(self):
            random.shuffle(self.dice)
            count = 0
            for row in range(4):
                  for col in range(4):
                        self.game_board[row][col] = random.choice(self.dice[count])
                        # print(f'{self.game_board[row][col]}, {self.dice[count]}, {count}')
                        count += 1
                        if self.game_board[row][col] == 'Q':
                              self.game_board[row][col] = 'Qu'
                        
            # self.test_solution()

      # check the words in each row/col/diag against the desired word (forward and backward) for a match
      def include_word(self, desired_word):
            self.find_possible_words()
            for key in self.words_to_check:
                  if self.words_to_check[key] == desired_word or reversed(self.words_to_check[key]) == desired_word:
                        return print('Found a match!')
            return print('Sorry, no word match.')
      
      # create a dictionary of all the 4-letter words in each row, col, and both diagonal cases
      def find_possible_words(self):
            for row in range(4):
                  for col in range(4):
                        self.words_to_check[f'row{row}'] += self.game_board[row][col]
                        self.words_to_check[f'col{col}'] += self.game_board[row][col]
                        if row == col:
                              self.words_to_check['diag1'] += self.game_board[row][col]
                        if row + col == 3:
                              self.words_to_check['diag2'] += self.game_board[row][col]
            # print(self.words_to_check)
            
      # def test_solution(self):
      #       self.game_board[2][0] = 'R'
      #       self.game_board[2][1] = 'O'
      #       self.game_board[2][2] = 'A'
      #       self.game_board[2][3] = 'D'
            
      def __str__(self):
            # pad the letters on dice face with spaces to give the board an evenly spaced look
            for row in range(4):
                  for col in range(4):
                        self.display_board[row][col] = self.game_board[row][col]
                        while (len(self.display_board[row][col]) < 3):
                              self.display_board[row][col] += ' '
            return (f"""
    Boggle!
  {self.display_board[0][0]}{self.display_board[0][1]}{self.display_board[0][2]}{self.display_board[0][3]}
  {self.display_board[1][0]}{self.display_board[1][1]}{self.display_board[1][2]}{self.display_board[1][3]}
  {self.display_board[2][0]}{self.display_board[2][1]}{self.display_board[2][2]}{self.display_board[2][3]}
  {self.display_board[3][0]}{self.display_board[3][1]}{self.display_board[3][2]}{self.display_board[3][3]}
  """)


game = BoggleBoard()
print(game)
game.new_dice()
game.shake()
print(game)

game.include_word('ROAD')


"""
      def find_possible_words(self):
            for row in range(4):
                  for col in range(4):
                        self.words_to_check[f'row{row}'] += self.game_board[row][col]
                        self.words_to_check[f'col{col}'] += self.game_board[row][col]
                        if row == col:
                              self.words_to_check['diag1'] += self.game_board[row][col]
                        if row + col == 3:
                              self.words_to_check['diag2'] += self.game_board[row][col]

                        
  A1  A2  A3  A4  
  B1  B2  B3  B4  
  C1  C2  C3  C4  
  D1  D2  D3  D4  
  
  for row in range(4):
        for col in range(4):
              r = 0, col = 0   >   'row0' +=            'col1' += 
              r = 0, col = 1   >   'row0' +=            'col2' +=
              r = 0, col = 2   >   'row0' +=            'col3' +=
              r = 0, col = 3   >   'row0' +=            'col4' +=
              r = 1, col = 0   >   'row1' +=            'col1' +=
              r = 1, col = 1   >   'row1' +=            'col2' +=
              r = 1, col = 2   >   'row1' +=            'col3' +=
              r = 1, col = 3   >   'row1' +=            'col4' +=
              r = 2, col = 0   >   'row2' +=            'col1' +=
              r = 2, col = 1   >   'row2' +=            'col2' +=
              r = 2, col = 2   >   'row2' +=            'col3' +=
              r = 2, col = 3   >   'row2' +=            'col4' +=
              r = 3, col = 0   >   'row3' +=            'col1' +=
              r = 3, col = 1   >   'row3' +=            'col2' +=
              r = 3, col = 2   >   'row3' +=            'col3' +=
              r = 3, col = 3   >   'row3' +=            'col4' +=


"""