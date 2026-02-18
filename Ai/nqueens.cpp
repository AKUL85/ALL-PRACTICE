#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <fstream>

using namespace std;

// Calculate heuristic in O(N) using frequency arrays
int getHFast(const vector<int>& queens) {
    int h = 0;
    vector<int> cols(8, 0);
    vector<int> diag1(15, 0);  // r + c
    vector<int> diag2(15, 0);  // r - c + 7

    for (int r = 0; r < 8; r++) {
        int c = queens[r];
        h += cols[c] + diag1[r + c] + diag2[r - c + 7];
        cols[c]++;
        diag1[r + c]++;
        diag2[r - c + 7]++;
    }
    return h;
}

// Save board as text file
void saveBoardAsText(const vector<vector<int>>& board) {
    ofstream file("output.txt");
    for (int r = 0; r < 8; r++) {
        for (int c = 0; c < 8; c++) {
            file << board[r][c] << " ";
        }
        file << "\n";
    }
    file.close();
    cout << "Board saved to 'output.txt'\n";
}

// Print board to console
void printBoard(const vector<vector<int>>& board) {
    for (int r = 0; r < 8; r++) {
        for (int c = 0; c < 8; c++) {
            cout << board[r][c] << " ";
        }
        cout << "\n";
    }
    cout << "\n";
}

// Hill Climbing with Steepest Ascent and Sideways moves
vector<vector<int>> hillClimbingFast(vector<int> initial_queens) {
    vector<int> current_queens = initial_queens;
    int current_h = getHFast(current_queens);
    int n_steps = 0;
    int n_side_moves = 0;

    while (n_steps < 1000) {
        if (current_h == 0) {
            cout << "Goal reached in " << n_steps << " steps!\n";
            // Convert back to 2D matrix
            vector<vector<int>> res_board(8, vector<int>(8, 0));
            for (int r = 0; r < 8; r++) {
                res_board[r][current_queens[r]] = 1;
            }
            return res_board;
        }

        int best_h = current_h;
        vector<vector<int>> neighbors;

        for (int row = 0; row < 8; row++) {
            int old_col = current_queens[row];
            for (int col = 0; col < 8; col++) {
                if (col == old_col) continue;

                current_queens[row] = col;
                int h = getHFast(current_queens);

                if (h < best_h) {
                    best_h = h;
                    neighbors.clear();
                    neighbors.push_back(current_queens);
                } else if (h == best_h) {
                    neighbors.push_back(current_queens);
                }
            }
            current_queens[row] = old_col;
        }

        if (best_h > current_h || neighbors.empty()) {
            return vector<vector<int>>();
        }

        if (best_h == current_h) {
            n_side_moves++;
            if (n_side_moves > 100) return vector<vector<int>>();
        } else {
            n_side_moves = 0;
        }

        // Randomly pick from equally good moves
        current_queens = neighbors[rand() % neighbors.size()];
        current_h = best_h;
        n_steps++;
    }

    return vector<vector<int>>();
}

int main() {
    srand(time(0));

    cout << "Enter the 8x8 board (0s and 1s):\n";
    vector<vector<int>> raw_board(8, vector<int>(8));

    for (int r = 0; r < 8; r++) {
        for (int c = 0; c < 8; c++) {
            cin >> raw_board[r][c];
        }
    }

    // Convert 2D board to 1D queen positions
    vector<int> queens(8);
    for (int r = 0; r < 8; r++) {
        int pos = 0;
        for (int c = 0; c < 8; c++) {
            if (raw_board[r][c] == 1) {
                pos = c;
                break;
            }
        }
        queens[r] = pos;
    }

    vector<vector<int>> solution = hillClimbingFast(queens);

    if (!solution.empty()) {
        printBoard(solution);
        saveBoardAsText(solution);
    } else {
        cout << "Stuck in local optimum. Try a different starting position.\n";
    }

    return 0;
}
