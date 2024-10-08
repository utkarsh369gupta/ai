from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        q = deque([start])
        visited = [start]
        while q:
            curr = q.popleft()
            print(curr, end=" ")
            for node in self.graph[curr]:
                if node not in visited:
                    visited.append(node)
                    q.append(node)


graph = Graph()

graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(3, 9)
graph.add_edge(3, 10)
graph.add_edge(4, 12)
graph.add_edge(4, 15)

graph.bfs(1)
