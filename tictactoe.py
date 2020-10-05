
def gameOver(game):
    x = 0
    while x < 9:
        if game[x] == '-':
            x = 9
        else:
            if x == 8:
                return True
        x += 1
    
    if game[0] == game[1] and game[1] == game[2] and game[0] != '-':
        return True
    if game[0] == game[3] and game[6] == game[0] and game[0] != '-':
        return True
    if game[0] == game[4] and game[4] == game[8] and game[0] != '-':
        return True
    if game[3] == game[4] and game[4] == game[5] and game[3] != '-':
        return True
    if game[6] == game[7] and game[7] == game[8] and game[6] != '-':
        return True
    if game[6] == game[4] and game[4] == game[2] and game[6] != '-':
        return True
    if game[1] == game[4] and game[7] == game[4] and game[1] != '-':
        return True
    if game[2] == game[5] and game[5] == game[8] and game[2] != '-':
        return True
    return False

def displayBoard(game):
    x = 0
    y = 1
    print ("  1   2   3")
    while x < 9:
        if x == 0 or x == 3 or x == 6:
            print(str(y), end = ' ')
            y += 1
        if game[x] == '-':
            print(' ', end = ' ')
        else:
            print(game[x], end = ' ')
        if x == 2 or x == 5:
            print()
            print ("  ---------")
        elif x != 8:
            print('|', end = ' ')
        x += 1

def nextMove(evenTurn, game):
    l = '-'
    x = 0
    y = 0
    if evenTurn:
        print("Player 2's turn:")
        l = 'x'
    else:
        print("Player 1's turn:")
        l = 'o'

    print()
    x = int(input("Enter a x coordinate: "))
    while x < 1 or x > 3:
        x = int(input("Enter a  VALID x coordinate: "))
    y = int(input("Enter a y coordinate: "))
    while y < 1 or y > 3:
        y = int(input("Enter a  VALID y coordinate: "))

    if x == 1:
        if y == 1: 
            game[0] = l
        if y == 2:
            game[3] = l
        if y == 3:
            game[6] = l
    if x == 2:
        if y == 1:
            game[1] = l
        if y == 2:
            game[4] = l
        if y == 3:
            game[7] = l
    if x == 3:
        if y == 1:
            game[2] = l
        if y == 2:
            game[5] = l
        if y == 3:
            game[8] = l
    
        

playAgain = True

while playAgain:
    game = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    turn = 1
    while not gameOver(game):
        displayBoard(game)
        nextMove(turn % 2 == 0, game)
        turn += 1
    
    displayBoard(game)
    print()
    if str(input("Play Again y/n: ")) == "n":
        playAgain = False



