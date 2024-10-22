import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.heuristic = {}  # Fixed the typo (heurisitc -> heuristic)
        self.cost = {}
        
    def add_edge(self, u, v, cost):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.cost[(u, v)] = cost
        self.cost[(v, u)] = cost
        
    def take_heuristic_input(self):
        for node in self.graph:
            value = float(input(f"Enter the heuristic value (h) for node {node}: "))
            self.heuristic[node] = value
            
    def astar(self, start, goal):
        pq = []
        heapq.heappush(pq, (self.heuristic[start], start))
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
            
            for neighbor in self.graph[current]:
                tentative_score = g_score[current] + self.cost[(current, neighbor)]
                
                if tentative_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_score
                    f_score = tentative_score + self.heuristic[neighbor]
                    heapq.heappush(pq, (f_score, neighbor))    
        return []
    
def main():
    graph = Graph()
    
    n = int(input("Enter the number of edges: "))
    
    for i in range(n):
        u, v, cst = map(int, input(f"Enter edge {i+1} (u, v, cost): ").split())
        graph.add_edge(u, v, cst)

    graph.take_heuristic_input()

    start_node = int(input("Enter the starting node: "))
    goal_node = int(input("Enter the goal node: "))

    path = graph.astar(start_node, goal_node)

    if path:
        print(f"Path from {start_node} to {goal_node}: {path}")
    else:
        print(f"No path found from {start_node} to {goal_node}")
        
if __name__ == "__main__":
    main()
