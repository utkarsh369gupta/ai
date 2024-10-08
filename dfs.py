from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        
        visited.add(start)  # Mark the current node as visited
        print(start, end=" ")  # Print the current node

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Example usage
graph = Graph()

graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(3, 9)
graph.add_edge(3, 10)
graph.add_edge(4, 12)
graph.add_edge(4, 15)

graph.dfs(1)
