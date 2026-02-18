#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>
#include <cmath>
#include <set>

using namespace std;

typedef tuple<int, int, int, int, int, int, int, int, int> State;

const State GOAL = make_tuple(1, 2, 3, 4, 5, 6, 7, 8, 0);

// Convert state to string for hashing
string stateToString(const State& state) {
    string result;
    for (int i = 0; i < 9; i++) {
        result += to_string(get<i>(state)) + ",";
    }
    return result;
}

// Manhattan Distance Heuristic
int manhattan(const State& state) {
    int distance = 0;
    for (int i = 0; i < 9; i++) {
        int value = get<i>(state);
        if (value != 0) {
            int current_x = i / 3;
            int current_y = i % 3;
            int goal_x = (value - 1) / 3;
            int goal_y = (value - 1) % 3;
            distance += abs(current_x - goal_x) + abs(current_y - goal_y);
        }
    }
    return distance;
}

// Find position of blank (0)
int findBlank(const State& state) {
    for (int i = 0; i < 9; i++) {
        if (get<i>(state) == 0) {
            return i;
        }
    }
    return -1;
}

// Generate neighbors
vector<State> getNeighbors(const State& state) {
    vector<State> neighbors;
    int blank_pos = findBlank(state);
    int x = blank_pos / 3;
    int y = blank_pos % 3;

    int moves[][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    for (auto& move : moves) {
        int nx = x + move[0];
        int ny = y + move[1];
        if (nx >= 0 && nx < 3 && ny >= 0 && ny < 3) {
            State new_state = state;
            int new_pos = nx * 3 + ny;
            swap(get<blank_pos>(new_state), get<new_pos>(new_state));
            neighbors.push_back(new_state);
        }
    }
    return neighbors;
}

// Reconstruct path
vector<State> reconstructPath(unordered_map<string, string>& came_from, const State& current) {
    vector<State> path;
    string current_str = stateToString(current);
    path.push_back(current);

    while (came_from.find(current_str) != came_from.end()) {
        // Convert string back to state (simplified - just for tracking)
        current_str = came_from[current_str];
    }
    return path;
}

// Print state
void printState(const State& state) {
    for (int i = 0; i < 9; i++) {
        if (i != 0 && i % 3 == 0) cout << "\n";
        cout << (get<i>(state) == 0 ? "_" : to_string(get<i>(state))) << " ";
    }
    cout << "\n\n";
}

// A* Algorithm
vector<State> aStar(const State& start) {
    priority_queue<pair<int, State>, vector<pair<int, State>>, greater<pair<int, State>>> open_list;
    open_list.push({manhattan(start), start});

    unordered_map<string, string> came_from;
    unordered_map<string, int> g_cost;
    g_cost[stateToString(start)] = 0;

    while (!open_list.empty()) {
        auto [f, current] = open_list.top();
        open_list.pop();

        if (current == GOAL) {
            vector<State> result;
            result.push_back(current);
            return result;
        }

        vector<State> neighbors = getNeighbors(current);
        int current_g = g_cost[stateToString(current)];

        for (const State& neighbor : neighbors) {
            int temp_g = current_g + 1;
            string neighbor_str = stateToString(neighbor);

            if (g_cost.find(neighbor_str) == g_cost.end() || temp_g < g_cost[neighbor_str]) {
                g_cost[neighbor_str] = temp_g;
                int f_cost = temp_g + manhattan(neighbor);
                open_list.push({f_cost, neighbor});
                came_from[neighbor_str] = stateToString(current);
            }
        }
    }

    return vector<State>();
}

int main() {
    State start_state = make_tuple(1, 0, 2, 4, 5, 3, 7, 8, 6);

    vector<State> solution = aStar(start_state);

    if (!solution.empty()) {
        cout << "Solution found in " << solution.size() - 1 << " moves\n\n";
        for (const State& step : solution) {
            printState(step);
        }
    } else {
        cout << "No solution found\n";
    }

    return 0;
}
