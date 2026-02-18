import copy
import random
import chess
from chess import svg

def save_board_as_png(board_matrix):
    """Converts the matrix to FEN and saves as SVG."""
    chess_board = chess.Board()
    chess_board.clear()
    for r in range(8):
        for c in range(8):
            if board_matrix[r][c]:
                # In python-chess, square(0,0) is A1. 
                # Our matrix [r][c] maps to row r, col c.
                chess_board.set_piece_at(chess.square(c, r), chess.Piece(chess.QUEEN, chess.WHITE))
    
    boardsvg = chess.svg.board(board=chess_board)
    with open("output.svg", "w") as f:
        f.write(boardsvg)
    print("SVG File 'output.svg' created successfully")

def get_h_fast(queens):
    """
    Calculates heuristic in O(N) using frequency arrays.
    queens: list where index is row and value is column.
    """
    h = 0
    cols = [0] * 8
    diag1 = [0] * 15 # r + c
    diag2 = [0] * 15 # r - c + 7
    
    for r, c in enumerate(queens):
        h += cols[c] + diag1[r + c] + diag2[r - c + 7]
        cols[c] += 1
        diag1[r + c] += 1
        diag2[r - c + 7] += 1
    return h

def hill_climbing_fast(initial_queens):
    """Optimized Hill Climbing with Steepest Ascent and Sideways moves."""
    current_queens = list(initial_queens)
    current_h = get_h_fast(current_queens)
    n_steps = 0
    n_side_moves = 0

    while n_steps < 1000: # Safety break
        if current_h == 0:
            print(f"Goal reached in {n_steps} steps!")
            # Convert back to 2D matrix
            res_board = [[0]*8 for _ in range(8)]
            for r, c in enumerate(current_queens):
                res_board[r][c] = 1
            return res_board

        best_h = current_h
        neighbors = []

        for row in range(8):
            old_col = current_queens[row]
            for col in range(8):
                if col == old_col: continue
                
                current_queens[row] = col
                h = get_h_fast(current_queens)
                
                if h < best_h:
                    best_h = h
                    neighbors = [list(current_queens)] # Reset list with new best
                elif h == best_h:
                    neighbors.append(list(current_queens))
            
            current_queens[row] = old_col # Backtrack

        if best_h > current_h or not neighbors:
            # Local optimum, no sideways or better move
            return -1
        
        if best_h == current_h:
            n_side_moves += 1
            if n_side_moves > 100: return -1
        else:
            n_side_moves = 0
            
        # Randomly pick from equally good moves to avoid cycles
        current_queens = random.choice(neighbors)
        current_h = best_h
        n_steps += 1
    
    return -1

if __name__ == "__main__":
    print("Enter the 8x8 board (0s and 1s):")
    raw_board = []
    for _ in range(8):
        raw_board.append(list(map(int, input().split())))

    # Convert 2D board to 1D queen positions (row-wise distribution)
    # This assumes we want one queen per row.
    queens = []
    for r in range(8):
        if 1 in raw_board[r]:
            queens.append(raw_board[r].index(1))
        else:
            queens.append(0) # Default if row is empty

    solution = hill_climbing_fast(queens)

    if solution != -1:
        save_board_as_png(solution)
    else:
        print("Stuck in local optimum. Try a different starting position.")