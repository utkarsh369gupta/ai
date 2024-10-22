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

def main():
    graph = Graph()
    n = input("enter the number of edges: ")
    for i in range(n):
        u,v = input("enter u and v: ")
        graph.add_edge(u, v)

    graph.take_heuristic_input()

    start_node = input("enter the starting node: ")
    goal_node = input("enter the goal node: ")

    path = graph.greedy_bfs(start_node, goal_node)

    if path:
        print(f"Path from {start_node} to {goal_node}: {path}")
    else:
        print(f"No path found from {start_node} to {goal_node}")

if __name__ == "__main__":
    main()