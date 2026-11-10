"""Mission 1 starter, created in student_submission/mission_1/planners.py.

Open that submission file in your editor and implement the four functions.
The guide creates it automatically and never overwrites an existing file.

Each function receives ctx with start, goal, grid, heuristic(cell) and
expand(cell, frontier_size). Return a list of (row, column) cells including
start and goal, or [] after exhausting the search. Call ctx.expand once per
expanded node. Record the actual frontier size, not the number of visited cells.
The runner enforces an expansion budget and a separate process time limit.
Use only the Python standard library. Do not import planning.reference_path.
When a free start is already the goal, return the single starting cell with
zero moves. No expansion is required for that case. Use the six small checks
on the Mission 1 page before running the full canonical-map evaluation.
"""
from collections import deque
from heapq import heappush, heappop
from planning.core import reconstruct


def bfs(ctx):
    """FIFO queue. Mark discovered cells when enqueuing and store parents.
    Use ctx.expand(current, len(frontier)+1) to obtain neighbours.
    BFS minimizes number of unit-cost edges, not execution time on a robot.
    """
    "We first get the starting location and end location"
    start = ctx.start
    end = ctx.goal

    "If we are already at the end location, we return to the start"
    if start == end:
        return [start]

    "Creates the queue that stores only the starting location"
    queue = deque([start])

    "Creates the parent dictionary to remember which cells we already discovered"
    parent = {start: None}

    "This while loop will continue until there are no cells left to explore"
    while queue:
        "Remove oldest cell"
        current = queue.popleft()

        "Checks if we made it to the end location and returns the path from start to finish"
        if current == end:
            return reconstruct(parent, end)

        "Finds the neighboring cells"
        neighbors = ctx.expand(current, len(queue) + 1)

        "Loops through each neighbor"
        for neighbor in neighbors:
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)

    "Returns an empty list if no path exists"
    return []


def dfs(ctx):
    """LIFO stack. Track discovered cells and parents to avoid cycles.
    A valid DFS path need not be shortest. Keep the supplied neighbour order.
    """
    start = ctx.start
    end = ctx.goal

    if start == end:
        return [start]

    "Creates python list with starting location"
    stack = [start]

    parent = {start: None}

    "This while loop keeps searching while the stack is not empty"
    while stack:
        "Removes the last element in the list and stores it in current"
        current = stack.pop()

        if current == end:
            return reconstruct(parent, end)

        neighbors = ctx.expand(current, len(stack) + 1)

        for neighbor in neighbors:
            if neighbor not in parent:
                parent[neighbor] = current
                stack.append(neighbor)

    return []


def iddfs(ctx):
    """Run depth-limited DFS with bounds 0, 1, 2, ... .
    Prevent cycles on the current path. Do not keep a global visited set across
    depth limits. Count expansions again on every iteration. Return [] only
    after exhaustive failure. Catch no budget exceptions. The runner records
    resource_limit honestly if this expensive method reaches its budget.
    """
    start = ctx.start
    end = ctx.goal

    if start == end:
        return [start]

    "Calculates the maximum search depth"
    max_depth = sum(row.count(0) for row in ctx.grid) - 1

    "This for loop repeatedly runs a depth search increasing its limits"
    for limit in range(max_depth + 1):

        "Creates the stack with three pieces of information"
        stack = [(start, [start], 0)]

        "Renives the newest entry"
        while stack:
            current, path, depth = stack.pop()

            if current == end:
                return path

            "If the depth hits its limit, stop"
            if depth == limit:
                continue

            neighbors = ctx.expand(current, len(stack) + 1)

            for neighbor in neighbors:
                if neighbor not in path:
                    new_path = path + [neighbor]
                    stack.append((neighbor, new_path, depth + 1))

    return []


def astar(ctx):
    """Use a heap ordered by g + ctx.heuristic(cell).
    Keep best g costs and parents. Ignore outdated heap entries. Each edge
    costs 1. Stop when the goal is removed from the priority queue.
    """
    start = ctx.start
    end = ctx.goal

    if start == end:
        return [start]

    "Explores cell with lowest estimated total cost"
    frontier = []
    heappush(frontier, (ctx.heuristic(start), 0, start))

    "Records the smallest known number of moves to reach each cell and records where we came from to reconstruct"
    g_cost = {start: 0}
    parent = {start: None}

    while frontier:
        "Removes the cell with the lowest estimated total cost"
        f, g, current = heappop(frontier)

        "If a new shorter route is found, it will skip the more expensive one"
        if g > g_cost[current]:
            continue

        if current == end:
            return reconstruct(parent, end)

        neighbors = ctx.expand(current, len(frontier) + 1)

        "This for loop is used to calculate the new A* formula f(n)=g(n)+h(n)"
        for neighbor in neighbors:
            new_g = g + 1

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                parent[neighbor] = current

                new_f = new_g + ctx.heuristic(neighbor)

                heappush(frontier, (new_f, new_g, neighbor))

    return []

