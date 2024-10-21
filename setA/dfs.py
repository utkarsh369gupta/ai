from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self, u, v):
        self.graph[u].append(v)
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        
        visited.add(start) 
        print(start, end=" ")

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)


# Example usagedef main():
    graph = Graph()
    n = int(input("enter the number of edges: "))
    for i in range(n):
        u, v = input("enter the edges: ").split(" ")
        graph.add_edge(u, v)
    start = input("enter the starting node: ")
    graph.dfs(start)
    
if __name__ == "__main__":
    main()