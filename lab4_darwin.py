#dana hedman djh393@nau.edu
#darwin guglielmo rg797@nau.edu
#the objective is to create the game and be able to win it basically
import random 
#this will help us with the randomization
def main():
  board = []
  row = 5
  col = 5
  square = [["\N{'WHITE SQUARE'}" for i in range(col)] for j in range(row)]
  for row in square:
    print(row)
  
  def randomize(board):
    row = random
    col = random
    
  def touch(board, row, col):
    white_square = "\N{'WHITE SQUARE'}"
    black_square = "\N{'BLACK SQUARE'}"
    print(board[row][col])
    
    if board[row][col] == white_square:
      print(board[row][col]
    elif board[row][col] == black_square
            print('inserting black square')
    else:
            print('Oops! Try Again!')

randomize(board)
    moves = 0
    while not is_solved(board):
        show(board)
        (row, col) = solicit_row_and_col()
        touch(board, row, col)
        moves += 1
    show(board)
    print(f"You won with {moves} moves!")

main()
