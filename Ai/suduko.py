from copy import deepcopy

class SudokuCSP:
    def __init__(self, board):
        self.board = board
        self.variables = [(r, c) for r in range(9) for c in range(9)]
        self.domains = self.initialize_domains()

    def initialize_domains(self):
        domains = {}
        for r in range(9):
            for c in range(9):
                if self.board[r][c] != 0:
                    domains[(r, c)] = {self.board[r][c]}
                else:
                    domains[(r, c)] = set(range(1, 10))
        return domains

    def get_neighbors(self, var):
        r, c = var
        neighbors = set()

        # Row and column
        for i in range(9):
            if i != c:
                neighbors.add((r, i))
            if i != r:
                neighbors.add((i, c))

        # 3x3 box
        box_r, box_c = 3 * (r // 3), 3 * (c // 3)
        for i in range(box_r, box_r + 3):
            for j in range(box_c, box_c + 3):
                if (i, j) != var:
                    neighbors.add((i, j))

        return neighbors

    def is_consistent(self, var, value):
        for neighbor in self.get_neighbors(var):
            if len(self.domains[neighbor]) == 1:
                if value in self.domains[neighbor]:
                    return False
        return True

    def select_unassigned_variable(self):
        unassigned = [v for v in self.variables if len(self.domains[v]) > 1]
        return min(unassigned, key=lambda var: len(self.domains[var]), default=None)

    def forward_check(self, var, value):
        removed = []
        for neighbor in self.get_neighbors(var):
            if value in self.domains[neighbor]:
                self.domains[neighbor].remove(value)
                removed.append((neighbor, value))
                if not self.domains[neighbor]:
                    return False, removed
        return True, removed

    def restore(self, removed):
        for var, value in removed:
            self.domains[var].add(value)

    def backtrack(self):
        if all(len(self.domains[v]) == 1 for v in self.variables):
            return True

        var = self.select_unassigned_variable()
        if var is None:
            return True

        for value in sorted(self.domains[var]):
            if self.is_consistent(var, value):
                original_domain = deepcopy(self.domains[var])
                self.domains[var] = {value}

                success, removed = self.forward_check(var, value)
                if success and self.backtrack():
                    return True

                self.domains[var] = original_domain
                self.restore(removed)

        return False

    def solve(self):
        if self.backtrack():
            for r in range(9):
                for c in range(9):
                    self.board[r][c] = next(iter(self.domains[(r, c)]))
            return self.board
        return None


# Example puzzle (0 = empty)
puzzle = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

solver = SudokuCSP(puzzle)
solution = solver.solve()

for row in solution:
    print(row)