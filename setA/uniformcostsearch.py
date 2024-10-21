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

        return None, float('inf')


if __name__ == "__main__":
    graph = Graph()
    n = int(input("Enter the number of edges: "))
    for i in range(n):
        u, v, cost = map(int, input(f"Enter edge {i + 1} (u, v, cost): ").split())
        graph.add_edge(u, v, cost)

    start_node = int(input("Enter the starting node: "))
    goal_node = int(input("Enter the goal node: "))

    path, total_cost = graph.ucs(start_node, goal_node)
    if path:
        print(f"Path from {start_node} to {goal_node}: {path} with total cost: {total_cost}")
    else:
        print(f"No path found from {start_node} to {goal_node}")
