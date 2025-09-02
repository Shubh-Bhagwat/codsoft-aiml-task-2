import math

def print_board(board):
    for i in range(3):
        print(board[3*i], board[3*i+1], board[3*i+2])
    print()

def is_win(board, player):
    win_states = [
        [0,1,2], [3,4,5], [6,7,8],      # rows
        [0,3,6], [1,4,7], [2,5,8],      # columns
        [0,4,8], [2,4,6]                # diagonals
    ]
    return any(all(board[pos]==player for pos in state) for state in win_states)

def is_board_full(board):
    return all(cell != 0 for cell in board)

def minimax(board, depth, maximizing):
    if is_win(board, 1):         # AI wins
        return 10 - depth
    if is_win(board, 2):         # Human wins
        return depth - 10
    if is_board_full(board):
        return 0              # Draw

    if maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == 0:
                board[i] = 1
                score = minimax(board, depth + 1, False)
                board[i] = 0
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == 0:
                board[i] = 2
                score = minimax(board, depth + 1, True)
                board[i] = 0
                best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == 0:
            board[i] = 1
            score = minimax(board, 0, False)
            board[i] = 0
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def main():
    board = [0] * 9               # 0 for empty, 1 for AI(O), 2 for Human(X)
    current_player = 2          # Human starts
    while True:
        print_board(board)
        if current_player == 2:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] != 0:
                print("Invalid move! Try again.")
                continue
        else:
            move = find_best_move(board)
            print(f"AI chooses position {move + 1}")

        board[move] = current_player

        if is_win(board, current_player):
            print_board(board)
            print("Player", "O" if current_player == 1 else "X", "wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 1 if current_player == 2 else 2

if __name__ == "__main__":
    main()
