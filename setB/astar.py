import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.heurisitc = {}
        self.cost = {}
        
    def add_edge(self, u, v, cost):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
        self.cost[(u, v)] = cost
        self.cost[(v, u)] = cost
        
        
    def take_heuristic_input(self):
        for node in self.graph:
            value = float(input("enter the h value: "))
            self.heurisitc[node] = value
            
    def astar(self, start, goal):
        pq = []
        heapq.heappush(pq, (self.heurisitc[start], start))
        came_from = {}
        came_from[start] = None
        
        g_score = {node: float('inf') for node in self.graph}
        g_score[start] = 0
        
        while pq:
            current = heapq.heappop(pq)[1]
            if current == goal:
                path = []
                while current is not None:
                    path.append(current)
                    current = came_from[current]
                return path[::-1]
            
            for n in self.graph[current]:
                tentative_score = g_score[current] + self.cost[(current, n)]
                
                if tentative_score < g_score[n]:
                    came_from[n] = current
                    g_score[n] = tentative_score
                    f_score = tentative_score + self.heurisitc[n]
                    heapq.heappush(pq, (f_score, n))    
        return []
    
graph = Graph()

# Add edges with optional costs
graph.add_edge(1, 2, cost=2)
graph.add_edge(1, 3, cost=4)
graph.add_edge(2, 4, cost=7)
graph.add_edge(3, 4, cost=1)
graph.add_edge(4, 5, cost=3)
graph.add_edge(5, 6, cost=2)

# Take heuristic values from the user
graph.take_heuristic_input()

# Define start and goal nodes
start_node = 1
goal_node = 6

# Run A* Search
path = graph.a_star(start_node, goal_node)

if path:
    print(f"Path from {start_node} to {goal_node}: {path}")
else:
    print(f"No path found from {start_node} to {goal_node}")