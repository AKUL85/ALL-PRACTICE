N = 9

def find_empty(sudoku):
    """Find an empty cell in the Sudoku grid. Returns (row, col) or None if full."""
    for row in range(N):
        for col in range(N):
            if sudoku[row][col] == 0:
                return row, col
    return None

def is_safe(sudoku, row, col, num):
    """Check if it's safe to put num in sudoku[row][col]."""
    # Check row
    if num in sudoku[row]:
        return False

    # Check column
    for r in range(N):
        if sudoku[r][col] == num:
            return False

    # Check 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if sudoku[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(sudoku):
    """Solve Sudoku using backtracking."""
    empty = find_empty(sudoku)
    if not empty:
        return True  # Puzzle solved

    row, col = empty

    for num in range(1, 10):
        if is_safe(sudoku, row, col, num):
            sudoku[row][col] = num
            if solve_sudoku(sudoku):
                return True
            sudoku[row][col] = 0  # Backtrack

    return False

def print_sudoku(sudoku):
    for row in sudoku:
        print(" ".join(str(num) for num in row))

# =========================
# Main
# =========================

if __name__ == "__main__":
    # Input Sudoku grid
    sudoku = []
    print("Enter Sudoku puzzle row by row (0 for empty cells):")
    for _ in range(N):
        row = list(map(int, input().split()))
        sudoku.append(row)

    if solve_sudoku(sudoku):
        print("Solution exists:")
        print_sudoku(sudoku)
    else:
        print("No solution exists")
