from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def bfs(self, start):
        queue = deque({start})
        visited = [start]
        
        while queue:
            curr = queue.popleft()
            for node in self.graph[curr]:
                if node not in visited:
                    print(node, end=" ")
                    queue.append(node)
                    visited.append(node)
                    
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.bfs(1)