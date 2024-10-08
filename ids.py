from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        
    def ids(self, start, goal, max_depth):
        for depth in range(max_depth + 1):
            path = []
            print(f"Depth: {depth}")  # To indicate the current depth level
            if self.dls_recursion(start, goal, depth, path):
                return path
        return None
    
    def dls_recursion(self, node, goal, limit, path):
        path.append(node)
        
        if node == goal:
            return True
        
        if limit <= 0:
            path.pop()
            return False
        
        for neighbor in self.graph[node]:
            if self.dls_recursion(neighbor, goal, limit-1, path):
                return True
        
        path.pop()
        return False

# Example usage
graph = Graph()

# Adding edges to the graph
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 5)
graph.add_edge(2, 6)

start_node = 0
goal_node = 5
max_depth = 3

# Perform Iterative Deepening Search
path = graph.ids(start_node, goal_node, max_depth)

if path:
    print(f"Path from {start_node} to {goal_node}: {path}")
else:
    print(f"No path found from {start_node} to {goal_node}")
