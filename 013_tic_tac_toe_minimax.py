"""Program 013: Tic-Tac-Toe Minimax AI."""
def check_winner(board: list[str]) -> str | None:
    combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for a, b, c in combos:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    if "" not in board:
        return "Tie"
    return None

def minimax(board: list[str], is_maximizing: bool) -> int:
    winner = check_winner(board)
    if winner == "O":
        return 10
    elif winner == "X":
        return -10
    elif winner == "Tie":
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = ""
                best_score = max(score, best_score)
        return int(best_score)
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = ""
                best_score = min(score, best_score)
        return int(best_score)

def best_move(board: list[str]) -> int:
    best_score = -float("inf")
    move = -1
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                move = i
    return move

if __name__ == "__main__":
    print("--- 013: Tic-Tac-Toe Minimax ---")
    board = ["X", "O", "X",
             "X", "O", "",
             "",  "",  ""]
    m = best_move(board)
    print(f"Optimal AI ('O') move index: {m} (blocks or wins)")
