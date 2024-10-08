import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, cost):
        self.graph[u].append((v, cost))  

    def ucs(self, start, goal):
        priority_queue = [(0, start)]
        visited = {start: 0}
        parent = {start: None}

        while priority_queue:
            current_cost, current_node = heapq.heappop(priority_queue)

            if current_node == goal:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = parent[current_node]
                return path[::-1], current_cost

            for neighbor, edge_cost in self.graph[current_node]:
                new_cost = current_cost + edge_cost

                if neighbor not in visited or new_cost < visited[neighbor]:
                    visited[neighbor] = new_cost
                    parent[neighbor] = current_node
                    heapq.heappush(priority_queue, (new_cost, neighbor))

        return None, float('inf')  # Return None if no path is found

graph = Graph()

# Add edges (node1, node2, cost)
graph.add_edge(1, 2, 1)
graph.add_edge(1, 3, 4)
graph.add_edge(2, 3, 2)
graph.add_edge(2, 4, 6)
graph.add_edge(3, 4, 3)

start_node = 1
goal_node = 4

path, total_cost = graph.ucs(start_node, goal_node)
if path:
    print(f"Path from {start_node} to {goal_node}: {path} with total cost: {total_cost}")
else:
    print(f"No path found from {start_node} to {goal_node}")
