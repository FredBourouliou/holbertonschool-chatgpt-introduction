def print_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:  # Don't print line after the last row
            print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True, row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True, board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True, board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True, board[0][2]

    return False, None

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_valid_input(prompt, valid_range):
    while True:
        try:
            value = int(input(prompt))
            if value in valid_range:
                return value
            else:
                print(f"Please enter a number between {min(valid_range)} and {max(valid_range)}")
        except ValueError:
            print("Invalid input! Please enter a number.")

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    winner = False
    
    print("Welcome to Tic-tac-toe!")
    print("Players take turns entering row and column numbers (0-2)")
    
    while not winner:
        print_board(board)
        print(f"Player {player}'s turn")
        
        while True:
            row = get_valid_input(f"Enter row (0-2) for player {player}: ", range(3))
            col = get_valid_input(f"Enter column (0-2) for player {player}: ", range(3))
            
            if board[row][col] == " ":
                break
            else:
                print("That spot is already taken! Try again.")
        
        board[row][col] = player
        winner, winning_player = check_winner(board)
        
        if winner:
            print_board(board)
            print(f"Congratulations! Player {winning_player} wins!")
            break
            
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
            
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    while True:
        tic_tac_toe()
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break
