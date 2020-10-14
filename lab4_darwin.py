#dana hedman djh393@nau.edu
#darwin guglielmo rg797@nau.edu
#the objective is to create the game and be able to win it basically
import random 
#this will help us with the randomization
def main():
  board = [
    [X, X, X, X, X],
    [X, X, X, X, X],
    [X, X, X, X, X],
    [X, X, X, X, X],
    [X, X, X, X, X]
]

randomize(board)
    moves = 0
    while not is_solved(board):
        show(board)
        (row, col) = solicit_row_and_col()
        touch(board, row, col)
        moves += 1
    show(board)
    print(f"You won with {moves} moves!")

def square():
  square = "\N{'WHITE SQUARE','BLACK SQUARE'}"
