#include <bits/stdc++.h>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

class SudokuCSP {
public:
    vector<vector<int>> board;
    vector<pair<int, int>> variables;
    map<pair<int, int>, set<int>> domains;

    SudokuCSP(vector<vector<int>>& initial_board) : board(initial_board) {
        // Initialize variables
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                variables.push_back({r, c});
            }
        }
        // Initialize domains
        initializeDomains();
    }

    void initializeDomains() {
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] != 0) {
                    domains[{r, c}].insert(board[r][c]);
                } else {
                    for (int i = 1; i <= 9; i++) {
                        domains[{r, c}].insert(i);
                    }
                }
            }
        }
    }

    set<pair<int, int>> getNeighbors(const pair<int, int>& var) {
        set<pair<int, int>> neighbors;
        int r = var.first;
        int c = var.second;

        // Row and column
        for (int i = 0; i < 9; i++) {
            if (i != c) neighbors.insert({r, i});
            if (i != r) neighbors.insert({i, c});
        }

        // 3x3 box
        int box_r = 3 * (r / 3);
        int box_c = 3 * (c / 3);
        for (int i = box_r; i < box_r + 3; i++) {
            for (int j = box_c; j < box_c + 3; j++) {
                if ((i != r || j != c)) {
                    neighbors.insert({i, j});
                }
            }
        }

        return neighbors;
    }

    bool isConsistent(const pair<int, int>& var, int value) {
        for (const auto& neighbor : getNeighbors(var)) {
            if (domains[neighbor].size() == 1 && domains[neighbor].count(value)) {
                return false;
            }
        }
        return true;
    }

    pair<int, int> selectUnassignedVariable() {
        pair<int, int> best = {-1, -1};
        int min_domain_size = 10;

        for (const auto& var : variables) {
            if (domains[var].size() > 1 && domains[var].size() < min_domain_size) {
                min_domain_size = domains[var].size();
                best = var;
            }
        }
        return best;
    }

    pair<bool, vector<pair<pair<int, int>, int>>> forwardCheck(const pair<int, int>& var, int value) {
        vector<pair<pair<int, int>, int>> removed;

        for (const auto& neighbor : getNeighbors(var)) {
            if (domains[neighbor].count(value)) {
                domains[neighbor].erase(value);
                removed.push_back({neighbor, value});
                if (domains[neighbor].empty()) {
                    return {false, removed};
                }
            }
        }
        return {true, removed};
    }

    void restore(const vector<pair<pair<int, int>, int>>& removed) {
        for (const auto& item : removed) {
            domains[item.first].insert(item.second);
        }
    }

    bool backtrack() {
        // Check if all variables are assigned
        bool all_assigned = true;
        for (const auto& var : variables) {
            if (domains[var].size() != 1) {
                all_assigned = false;
                break;
            }
        }

        if (all_assigned) return true;

        auto var = selectUnassignedVariable();
        if (var.first == -1) return true;

        vector<int> values(domains[var].begin(), domains[var].end());
        sort(values.begin(), values.end());

        for (int value : values) {
            if (isConsistent(var, value)) {
                set<int> original_domain = domains[var];
                domains[var].clear();
                domains[var].insert(value);

                auto [success, removed] = forwardCheck(var, value);
                if (success && backtrack()) {
                    return true;
                }

                domains[var] = original_domain;
                restore(removed);
            }
        }

        return false;
    }

    vector<vector<int>> solve() {
        if (backtrack()) {
            vector<vector<int>> result(9, vector<int>(9));
            for (int r = 0; r < 9; r++) {
                for (int c = 0; c < 9; c++) {
                    result[r][c] = *domains[{r, c}].begin();
                }
            }
            return result;
        }
        return vector<vector<int>>();
    }
};

void printBoard(const vector<vector<int>>& board) {
    for (int r = 0; r < 9; r++) {
        for (int c = 0; c < 9; c++) {
            cout << board[r][c] << " ";
        }
        cout << "\n";
    }
}

int main() {
    // Example puzzle (0 = empty)
    vector<vector<int>> puzzle = {
        {5, 3, 0, 0, 7, 0, 0, 0, 0},
        {6, 0, 0, 1, 9, 5, 0, 0, 0},
        {0, 9, 8, 0, 0, 0, 0, 6, 0},
        {8, 0, 0, 0, 6, 0, 0, 0, 3},
        {4, 0, 0, 8, 0, 3, 0, 0, 1},
        {7, 0, 0, 0, 2, 0, 0, 0, 6},
        {0, 6, 0, 0, 0, 0, 2, 8, 0},
        {0, 0, 0, 4, 1, 9, 0, 0, 5},
        {0, 0, 0, 0, 8, 0, 0, 7, 9}
    };

    SudokuCSP solver(puzzle);
    vector<vector<int>> solution = solver.solve();

    if (!solution.empty()) {
        printBoard(solution);
    } else {
        cout << "No solution found\n";
    }

    return 0;
}
