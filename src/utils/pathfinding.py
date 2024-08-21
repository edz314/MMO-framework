# src/utils/pathfinding.py

import heapq

def heuristic(a, b):
    """
    Calculate the heuristic for A* pathfinding (using Manhattan distance for a grid).
    :param a: The start point (x, y).
    :param b: The goal point (x, y).
    :return: The Manhattan distance between point a and point b.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar_search(start, goal, graph):
    """
    Perform A* search to find the shortest path from start to goal.
    :param start: The starting point (x, y).
    :param goal: The goal point (x, y).
    :param graph: A 2D grid representing the environment where each cell can be traversable or blocked.
    :return: A list of tuples representing the path from start to goal, or an empty list if no path is found.
    """
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        neighbors = get_neighbors(current, graph)
        for neighbor in neighbors:
            tentative_g_score = g_score[current] + 1  # Assuming each move has a cost of 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return []

def get_neighbors(position, graph):
    """
    Get the neighbors of a position in a 2D grid.
    :param position: The current position (x, y).
    :param graph: A 2D grid representing the environment.
    :return: A list of neighboring positions that are traversable.
    """
    x, y = position
    neighbors = []

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[nx][ny] == 0:
            neighbors.append((nx, ny))

    return neighbors

def reconstruct_path(came_from, current):
    """
    Reconstruct the path from the start to the goal.
    :param came_from: A dictionary mapping each node to its predecessor.
    :param current: The current node (goal node).
    :return: A list of tuples representing the path from start to goal.
    """
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]

def dijkstra_search(start, goal, graph):
    """
    Perform Dijkstra's algorithm to find the shortest path from start to goal.
    :param start: The starting point (x, y).
    :param goal: The goal point (x, y).
    :param graph: A 2D grid representing the environment where each cell can have a different traversal cost.
    :return: A list of tuples representing the path from start to goal, or an empty list if no path is found.
    """
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        current_cost, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        neighbors = get_neighbors(current, graph)
        for neighbor in neighbors:
            tentative_g_score = current_cost + graph[neighbor[0]][neighbor[1]]

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                heapq.heappush(open_set, (tentative_g_score, neighbor))

    return []

def breadth_first_search(start, goal, graph):
    """
    Perform Breadth-First Search (BFS) to find the shortest path from start to goal.
    :param start: The starting point (x, y).
    :param goal: The goal point (x, y).
    :param graph: A 2D grid representing the environment.
    :return: A list of tuples representing the path from start to goal, or an empty list if no path is found.
    """
    queue = [(start, [start])]
    visited = set()

    while queue:
        (current, path) = queue.pop(0)

        if current == goal:
            return path

        visited.add(current)

        neighbors = get_neighbors(current, graph)
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)

    return []

