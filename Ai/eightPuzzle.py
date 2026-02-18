import heapq

# Goal state
GOAL = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 0))   # 0 represents blank (_)


# Manhattan Distance Heuristic
def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance


# Find position of blank (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


# Generate neighbors
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors


# A* Algorithm
def a_star(start):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_cost = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == GOAL:
            return reconstruct_path(came_from, current)

        for neighbor in get_neighbors(current):
            temp_g = g_cost[current] + 1

            if neighbor not in g_cost or temp_g < g_cost[neighbor]:
                g_cost[neighbor] = temp_g
                f_cost = temp_g + manhattan(neighbor)
                heapq.heappush(open_list, (f_cost, neighbor))
                came_from[neighbor] = current

    return None


# Reconstruct path
def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


# Print state
def print_state(state):
    for row in state:
        print(" ".join(str(x) if x != 0 else "_" for x in row))
    print()


# Initial state
start_state = ((1, 0, 2),
               (4, 5, 3),
               (7, 8, 6))


# Run A*
solution = a_star(start_state)

if solution:
    print("Solution found in", len(solution) - 1, "moves\n")
    for step in solution:
        print_state(step)
else:
    print("No solution found")