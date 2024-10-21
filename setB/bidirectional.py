from collections import defaultdict, deque

# Class for Bidirectional Search


class BidirectionalSearch:
    def __init__(self):
        # Using defaultdict to store the adjacency list
        self.graph = defaultdict(list)

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Perform BFS in the forward direction
    def bfs(self, queue, visited, parent):
        current_node = queue.popleft()
        for neighbor in self.graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current_node
                queue.append(neighbor)

    # Check if the forward and backward searches meet at a common point
    def is_intersecting(self, visited_from_start, visited_from_goal):
        for node in visited_from_start:
            if node in visited_from_goal:
                return node
        return None

    # Reconstruct the path from start to goal using the parent dictionaries
    def construct_path(self, intersect_node, parent_from_start, parent_from_goal, start, goal):
        # Path from start to intersection
        path = []
        node = intersect_node
        while node is not None:
            path.append(node)
            node = parent_from_start.get(node)

        path = path[::-1]  # Reverse the start path to correct order

        # Path from intersection to goal
        node = parent_from_goal[intersect_node]
        while node is not None:
            path.append(node)
            node = parent_from_goal.get(node)

        return path

    # Bidirectional Search
    def bidirectional_search(self, start, goal):
        # Initialize BFS queues, visited sets, and parent dictionaries
        queue_from_start = deque([start])
        queue_from_goal = deque([goal])

        visited_from_start = {start}
        visited_from_goal = {goal}

        parent_from_start = {start: None}
        parent_from_goal = {goal: None}

        while queue_from_start and queue_from_goal:
            # BFS from start
            self.bfs(queue_from_start, visited_from_start, parent_from_start)
            # BFS from goal
            self.bfs(queue_from_goal, visited_from_goal, parent_from_goal)

            # Check for intersection
            intersect_node = self.is_intersecting(
                visited_from_start, visited_from_goal)
            if intersect_node:
                return self.construct_path(intersect_node, parent_from_start, parent_from_goal, start, goal)

        # If no path is found
        return None


# Example usage
graph = BidirectionalSearch()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(5, 6)

start_node = 1
goal_node = 6

path = graph.bidirectional_search(start_node, goal_node)
if path:
    print(f"Path between {start_node} and {goal_node}: {path}")
else:
    print(f"No path found between {start_node} and {goal_node}")

