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

def main():
    graph = Graph()
    n = int(input("enter the number of edges: "))
    for i in range(n):
        u, v = input("enter the edges: ").split(" ")
        graph.add_edge(u, v)
    start = input("enter the starting node: ")
    graph.bfs(start)
    
if __name__ == "__main__":
    main()


