import sys

def display_divider_line():
    # print divider line 1
    for i in range(5):
        print("-", end="")
    print()

def display_board(board):
    print()
    num = 0
    divider = 0
    for row in board:
        for shape in row:
            print(shape, end="")
            if num < 2:
                print("|", end="")
                num += 1
        num = 0
        print()
        if divider < 2:
            display_divider_line()
            divider += 1
    print()

def val_player_input(player_input):

    if player_input[0] == "quit":
        sys.exit()

    row = int(player_input[0])
    col = int(player_input[1])

    while True:
        if 0 <= row <= 2 or 0 <= col <= 2:
            return row, col
        valid_input = input("Enter a valid comma separated value.\n").split(',')
        row = int(valid_input[0])
        col = int(valid_input[1])

def check_move(board, row, col):
    if board[row][col] != '_':
        print("Invalid move. Try again.")
        return True
    return False

def check_win(board):
    status = 1

    # check rows
    board_len = len(board)
    for row in range(board_len):
        if board[row][0] == board[row][1] and board[row][0] != '_':
            if board[row][1] == board[row][2]:
                print(f"Player {board[row][0]} is the winner!")
                status = 0

    # check columns
    for col in range(board_len):
        if board[0][col] == board[1][col]and board[0][col] != '_':
            if board[1][col] == board[2][col]:
                print(f"Player {board[0][col]} is the winner!")
                status = 0

    # check diagonal
    if board[0][0] == board[1][1] and board[0][0] != '_':
        if board[1][1] == board[2][2]:
            print(f"Player {board[0][0]} is the winner!")
            status = 0
    
    # check diagonal
    if board[0][2] == board[1][1] and board[0][2] != '_':
        if board[1][1] == board[2][0]:
            print(f"Player {board[0][2]} is the winner!")
            status = 0

    if status == 0:
        display_board(board)
        sys.exit()

    return

def play_game():
    board = [['_' for _ in range(3)] for _ in range(3)]
    current_move = 'x'
    player = ""

    #print game message

    while player != "quit":

        check_loop = True
        while check_loop:
            player = input("Make your move player " + current_move + "\n").split(',')

            row, col = val_player_input(player)

            # check if move is available
            check_loop = check_move(board, row, col)

        board[row][col] = current_move

        # check for win function
        check_win(board)

        if current_move == 'x':
            current_move = 'o'
        else:
            current_move = 'x'

        display_board(board)

play_game()
