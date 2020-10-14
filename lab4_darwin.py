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
count = getCount()
lights = get_lights(count)

def square():
  square = "\N{'WHITE SQUARE','BLACK SQUARE'}"

def get_lights(count):
  return [random.choice("\N{'WHITE SQUARE','BLACK SQUARE'}" for i in range(count)]

def getcount():
  while True:
    else:
      count=int(input('How many lights would you like to have? '))
            return count
 
def getLightToToggle(count):
    while True:
        else:
            index=int(input('Which light do you want to toggle (0 to quit)?  '))
            if 0<=index and index<=count:return index
            else:print('Index out of range')
                        
def toggleLights(index,lights):
    if lights[index - 1] == "\N{'WHITE SQUARE'}": lights[index - 1] = "\N{'BLACK SQUARE'}"
    else:lights[index - 1] = "\N{'WHITE SQUARE'}"

    if index ==1:
        if lights[1] == "\N{'WHITE SQUARE'}": lights[1] = "\N{'BLACK SQUARE'}"
        else: lights[1] = "\N{'WHITE SQUARE'}"
    elif index==len(lights):
        if lights[index-2] == "\N{'WHITE SQUARE'}": lights[index-2] = "\N{'BLACK SQUARE'}"
        else: lights[index-2] = "\N{'WHITE SQUARE'}"
    else:
        if lights[index-2]=="\N{'WHITE SQUARE'}":lights[index-2]="\N{'BLACK SQUARE'}"
        else:lights[index-2]="\N{'WHITE SQUARE'}"
        if lights[index]=="\N{'WHITE SQUARE'}":lights[index]="\N{'BLACK SQUARE'}"
        else:lights[index]="\N{'WHITE SQUARE'}"
                 
main()
