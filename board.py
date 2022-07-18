board = [["-" for i in range(3)] for j in range(3)]
def print_board():

dim = 3

def check_win(symbol,row,col):       
        if all_rows(col,symbol):
            return True

        if all_cols(row,symbol):
            return True

        if left_diag(row,col,symbol):
            return True

        if right_diag(row,col,symbol):
            return True

        return False

def all_rows(col,s):
    for row in range(dim):
        if board[row][col]!= s:
            return False
    return True

def all_cols(row,s):
    for col in range(dim):
        if board[row][col]!= s:
            return False
    return True

    print("Printing board")
def left_diag(row,col,s):
    if row != col:
        return False
    for i in range(dim):
        if board[i][i] != s:
            return False
    return True

def right_diag(row,col,s):
    if row+col != dim-1:
        return False
    j = dim -1
    for i in range(dim):
        if board[i][j] != s:
            return False
        j -=1
    return True



def print_board():   
    print("Printing board...")
    for row in board:
        print(row)



def check_mark(row,col):
    if row < 0 or row > 2 or col < 0 or col > 2:
        print("**** Invalid row or column. Please select row / col between values 0 to 2 ****")
        return False
    if board[row][col] != "-":
        print("**** Board[{}][{}] has already been selected. Please somewhere else on the board ****".format(row,col))
        return False
    return True

def add_mark(player, row, col):
    if player == 1:
        mark = "X"
    elif player == 2:
        mark = "O"
    board[row][col] = mark
    print ("\nPlayer {} added mark at the locatiion {},{}".format(player,row,col))
    if check_win(mark,row,col):
        return player



def play_game():
    pass



if __name__ == "__main__":
    print_board() 
    num = 0
    player = 1
    while num < 9:
        if num % 2 == 0:
            player = 1
        else:
            player = 2
        print_board()
        print("\nPlayer {}, make your move".format(player))
        row = int(input("Enter row nos (0-2):"))
        col = int(input("Enter col nos (0-2):"))
        if not check_mark(row,col):
            print("**** Invalid choice. Please mark again! ****")
            continue
        win  = add_mark(player, row, col)
        if win == 1:
            print("Player 1 wins!. Game Over!")
            break
        elif win == 2: 
            print("Player 2 wins!. Game Over!")
            break
        num+=1
