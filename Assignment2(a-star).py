import heapq


class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  # Cost from start node to current node
        self.h = h  # Heuristic estimate of cost from current node to goal node
        self.f = self.g + self.h  # Total estimated cost

    def __lt__(self, other):
        return self.f < other.f


def manhattan_distance(state, goal_state):
    """
    Calculate Manhattan distance heuristic between current state and goal state.
    """
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] != goal_state[i][j] and state[i][j] != 0:
                value = state[i][j]
                goal_position = [(row.index(value), row_num) for row_num, row in enumerate(goal_state) if value in row][
                    0]
                distance += abs(i - goal_position[1]) + abs(j - goal_position[0])
    return distance


def get_neighbors(node, goal_state):
    """
    Get neighboring states of the current state.
    """
    neighbors = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
    for dir in directions:
        new_state = move_blank(node.state, dir)
        if new_state:
            h = manhattan_distance(new_state, goal_state)
            neighbors.append(Node(new_state, node, node.g + 1, h))
    return neighbors


def move_blank(state, direction):
    """
    Move the blank tile (0) in the specified direction.
    """
    row, col = find_blank(state)
    new_row = row + direction[0]
    new_col = col + direction[1]
    if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]):
        new_state = [list(row) for row in state]
        new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
        return tuple(tuple(row) for row in new_state)  # Convert the list of lists to tuple of tuples
    else:
        return None


def find_blank(state):
    """
    Find the position of the blank tile (0) in the state.
    """
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 0:
                return i, j


def reconstruct_path(node):
    """
    Reconstruct the path from the goal node to the start node.
    """
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return tuple(path[::-1])


def a_star(start_state, goal_state):
    """
    A* algorithm to find the shortest path from start_state to goal_state.
    """
    start_node = Node(start_state, None, 0, manhattan_distance(start_state, goal_state))
    open_set = [start_node]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)
        if current_node.state == goal_state:
            return reconstruct_path(current_node)

        closed_set.add(current_node.state)
        neighbors = get_neighbors(current_node, goal_state)

        for neighbor in neighbors:
            if neighbor.state in closed_set:
                continue

            if neighbor not in open_set:
                heapq.heappush(open_set, neighbor)
            else:
                existing_neighbor = [n for n in open_set if n == neighbor][0]
                if neighbor.g < existing_neighbor.g:
                    existing_neighbor.g = neighbor.g
                    existing_neighbor.f = existing_neighbor.g + existing_neighbor.h
                    existing_neighbor.parent = neighbor.parent

    return None


def get_user_input():
    """
    Get user input for start state and goal state.
    """
    start_state = []
    goal_state = []
    print("Enter the start state (3x3 grid, use 0 to represent the blank tile):")
    for i in range(3):
        row = input(f"Enter row {i + 1}: ").strip().split()
        start_state.append(tuple(map(int, row)))
    print("Enter the goal state (3x3 grid, use 0 to represent the blank tile):")
    for i in range(3):
        row = input(f"Enter row {i + 1}: ").strip().split()
        goal_state.append(tuple(map(int, row)))
    return start_state, goal_state


if __name__ == "__main__":
    start_state, goal_state = get_user_input()
    start_state = tuple(map(tuple, start_state))  # Convert start state to tuple of tuples
    goal_state = tuple(map(tuple, goal_state))  # Convert goal state to tuple of tuples
    path = a_star(start_state, goal_state)
    if path:
        print("Path found:")
        for step in path:
            print(step)
    else:
        print("No path found.")

