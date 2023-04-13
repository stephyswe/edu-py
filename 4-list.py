from termcolor import colored
# LISTOR

# 1. Store 5 numbers in a list and print largest number


def largest_number():
    num_list = []
    for i in range(4):
        while True:
            try:
                num = int(input("Enter a number: "))
                num_list.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
    largest = max(num_list)
    print("The largest number is:", largest)

# 2. Chess board

def chess():
    board = []

    # populate board with spaces
    for i in range(8):
        row = [' ' for i in range(8)]
        board.append(row)

    # place black pawns on row 2
    for i in range(8):
        board[1][i] = colored('b', 'grey')

    # place white pawns on row 7
    for i in range(8):
        board[6][i] = colored('b', 'white')

    # print the checkerboard
    for row in board:
        for square in row:
            print(square, end=' ')
        print()

def chess_with_table():
    board = []

    # populate board with spaces
    for i in range(8):
        row = [' ' for i in range(8)]
        board.append(row)

    # place black pawns on row 2
    for i in range(8):
        board[1][i] = colored('b', 'grey')

    # place white pawns on row 7
    for i in range(8):
        board[6][i] = colored('b', 'white')

    # print the checkerboard
    print('  ', end='')
    for i in range(8):
        print(i, end=' ')
    print()
    for i, row in enumerate(board):
        print(i, end=' ')
        for square in row:
            print(square, end=' ')
        print()

"""
Complete Chess board without movement.
"""
def place_pawns(board, is_white):
    row = 6 if is_white else 1
    color = 'white' if is_white else 'grey'

    for col in range(8):
        board[row][col] = colored('♙', color)

def place_pieces(board, is_white):
    row = 7 if is_white else 0
    color = 'white' if is_white else 'grey'
    pieces = ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']
    for i in range(8):
        board[row][i] = colored(pieces[i], color)       

def print_board(board):
    cols = '   A B C D E F G H'
    print(cols)
    for i in range(8):
        print(i + 1, end='  ')
        print(' '.join(board[i]), end=' ')
        print(i + 1)
    print(cols)


def chess_without_movement():
        # create the initial board with spaces
    board = []
    for i in range(8):
        row = [' '] * 8
        board.append(row)

    # place white pieces
    place_pawns(board, True)
    place_pieces(board, True)

    # place black pieces
    place_pieces(board, False)
    place_pawns(board, False)

    # print the board
    print_board(board)

"""
Complete Chess board with movement.
"""
def print_board(board):
    cols = '   A B C D E F G H'
    print(cols)
    for i in range(8):
        print(i + 1, end='  ')
        print(' '.join(board[i]), end=' ')
        print(i + 1)
    print(cols)


def move_piece(board, from_pos, to_pos):
    # Convert from_pos and to_pos to (row, col) tuples
    from_row, from_col = ord(from_pos[1]) - ord('1'), ord(from_pos[0]) - ord('A')
    to_row, to_col = ord(to_pos[1]) - ord('1'), ord(to_pos[0]) - ord('A')
    
    # Move the piece
    piece = board[from_row][from_col]
    board[from_row][from_col] = ' '
    board[to_row][to_col] = piece


def get_user_move(is_white):
    player = 'White' if is_white else 'Black'
    while True:
        move = input(f"{player} player's move: ")
        if len(move) == 4 and move[0] in 'ABCDEFGH' and move[1] in '12345678' \
                and move[2] in 'ABCDEFGH' and move[3] in '12345678':
            return move
        else:
            print('Invalid move, please try again.')



def is_game_over(board, is_white_turn):
    king = '♚' if is_white_turn else '♔'

    # Find the location of the king
    king_location = None
    for i in range(8):
        for j in range(8):
            if board[i][j] == king:
                king_location = (i, j)
                break
        if king_location:
            break

    # If the king is not on the board, the game is over
    if not king_location:
        return True

    # Check if the king is in check
    # ...

    # Check if the game is in stalemate
    #if is_stalemate(board, is_white_turn):
        #return True

    # If the king is not in check and the game is not in stalemate, the game is not over
    return False

def play_chess():
    # create the initial board with spaces
    board = []
    for i in range(8):
        row = [' '] * 8
        board.append(row)

    # place white pieces
    place_pawns(board, True)
    place_pieces(board, True)

    # place black pieces
    place_pieces(board, False)
    place_pawns(board, False)

    # print the board
    print_board(board)

    # play the game
    is_white_turn = True
    while True:
        # Get the player's move
        move = get_user_move(is_white_turn)

        # Move the piece
        move_piece(board, move[:2], move[2:])

        # Print the board
        print_board(board)

        # Check if the game is over
        if is_game_over(board, is_white_turn):
            winner = 'White' if is_white_turn else 'Black'
            print(f"{winner} wins!")
            break

        # Switch turns
        is_white_turn = not is_white_turn

#3. Dictionary - Bank application
accounts = {}

def create_account():
    account_number = input("Enter account number: ")
    balance = float(input("Enter initial balance: "))
    accounts[account_number] = balance
    print("Account created successfully.")

def delete_account():
    account_number = input("Enter account number to delete: ")
    if account_number in accounts:
        del accounts[account_number]
        print("Account deleted successfully.")
    else:
        print("Account not found.")

def list_account_numbers():
    print("Account numbers:")
    for account_number in accounts:
        print(account_number)

def list_total_balance():
    total_balance = sum(accounts.values())
    print("Total balance:", total_balance)

def list_account_numbers_and_balances():
    print("Account numbers and balances:")
    for account_number, balance in accounts.items():
        print(account_number, balance)

def bank_app():
    while True:
        print("\nMenu:")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. List all Account Numbers")
        print("4. List Total Balance")
        print("5. List all Account Numbers and Balances")
        print("6. Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            delete_account()
        elif choice == "3":
            list_account_numbers()
        elif choice == "4":
            list_total_balance()
        elif choice == "5":
            list_account_numbers_and_balances()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    bank_app()
