from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        
    def dls(self, start, goal, limit):
        path = []
        if self.dls_recursion(start, goal, limit, path):
            return path
        return None
    
    def dls_recursion(self, node, goal, limit, path):
        path.append(node)
        
        if node == goal:
            return True
        
        if limit <= 0:
            path.pop()
            return False
        
        # if node in self.graph:
        for neighbor in self.graph[node]:
            if self.dls_recursion(neighbor, goal, limit-1, path):
                return True
        
        path.pop()
        return False
        
def main():
    graph = Graph()
    # v = int(input("enter number of vertex: "))
    e = int(input("enter number of edges: "))
    for _ in range(e):
        u, v = input("enter the connected vertexes: ").split(" ")
        graph.add_edge(u, v)
    start_vertex = input("enter the starting vertex: ")
    graph.dls(start_vertex)
    
if __name__ == "__main__":
    main()  
        

# def main():
#     graph = Graph()
    
#     # Adding edges to the graph
#     graph.add_edge('A', 'B')
#     graph.add_edge('A', 'C')
#     graph.add_edge('B', 'D')
#     graph.add_edge('B', 'E')
#     graph.add_edge('C', 'F')
#     graph.add_edge('C', 'G')
    
#     start_node = 'A'
#     goal_node = 'F'
#     depth_limit = 3
    
#     path = graph.dls(start_node, goal_node, depth_limit)
    
#     if path:
#         print(f"Goal node {goal_node} found within depth limit {depth_limit}.")
#         print("Path:", " -> ".join(path))
#     else:
#         print(f"Goal node {goal_node} not found within depth limit {depth_limit}.")
        

# if __name__ == "__main__":
#     main()
