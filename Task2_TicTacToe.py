board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print(board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("--+---+--")
    print()

def check_winner(player):
    win_combination = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for combo in win_combination: 
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True 
    return False 

def is_full(): 
    return " " not in board

def play_game():
    current_player = "X"

    while True:
        print_board() 
        move = int(input(f"player {current_player}, enter position (1-9): ")) -1

        if board[move] != " ":
            print("Position already taken! Try again.")
            continue

        board[move] = current_player

        if check_winner(current_player):
            print_board()
            print(f"player {current_player} wins!")
            break

        if is_full():
            print_board()
            print("It's a draw!")
            break

        current_player = "0" if current_player == "X" else "X"

play_game() 