import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.heurisitc = {}
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def take_heuristic_input(self):
        for node in self.graph:
            value = float(input("enter the h value: "))
            self.heurisitc[node] = value
    
    def greedy_bfs(self, start, goal):
        pq = []
        heapq.heappush(pq, (self.heurisitc[start], start))
        came_from = {}
        came_from[start] = None
        
        while pq:
            current = heapq.heappop(pq)[1]
            if current == goal:
                path = []
                while current is not None:
                    path.append(current)
                    current = came_from[current]
                return path[::-1]
            
            for n in self.graph[current]:
                if n not in came_from:
                    heapq.heappush(pq, (self.heurisitc[n], n))
                    came_from[n] = current
                    
                    
        return []

graph = Graph()

# Add edges
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(5, 6)

# Take heuristic values from the user
graph.take_heuristic_input()

# Define start and goal nodes
start_node = 1
goal_node = 6

# Run Greedy Best-First Search
path = graph.greedy_bfs(start_node, goal_node)

if path:
    print(f"Path from {start_node} to {goal_node}: {path}")
else:
    print(f"No path found from {start_node} to {goal_node}")