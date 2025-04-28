# tictactoe_ai.py

import math

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = (0, 0)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are 'X' and AI is 'O'\n")
    print_board(board)

    while True:
        # Human move
        row = int(input("Enter your move row (0-2): "))
        col = int(input("Enter your move column (0-2): "))
        if board[row][col] != " ":
            print("Cell already taken, try again.")
            continue
        board[row][col] = "X"
        print_board(board)

        if check_winner(board, "X"):
            print("You win! 🎉")
            break
        if is_board_full(board):
            print("It's a tie! 🤝")
            break

        # AI move
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = "O"
        print("AI has made its move:")
        print_board(board)

        if check_winner(board, "O"):
            print("AI wins! 🤖🏆")
            break
        if is_board_full(board):
            print("It's a tie! 🤝")
            break

if __name__ == "__main__":
    main()
