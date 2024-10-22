from collections import defaultdict, deque

class BidirectionalSearch:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, queue, visited, parent):
        current_node = queue.popleft()
        for neighbor in self.graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current_node
                queue.append(neighbor)

    def is_intersecting(self, visited_from_start, visited_from_goal):
        for node in visited_from_start:
            if node in visited_from_goal:
                return node
        return None

    def construct_path(self, intersect_node, parent_from_start, parent_from_goal, start, goal):
        path = []
        node = intersect_node
        while node is not None:
            path.append(node)
            node = parent_from_start.get(node)

        path = path[::-1]  

        node = parent_from_goal[intersect_node]
        while node is not None:
            path.append(node)
            node = parent_from_goal.get(node)

        return path

    def bidirectional_search(self, start, goal):
        queue_from_start = deque([start])
        queue_from_goal = deque([goal])

        visited_from_start = {start}
        visited_from_goal = {goal}

        parent_from_start = {start: None}
        parent_from_goal = {goal: None}

        while queue_from_start and queue_from_goal:
            self.bfs(queue_from_start, visited_from_start, parent_from_start)
            self.bfs(queue_from_goal, visited_from_goal, parent_from_goal)

            # Check for intersection
            intersect_node = self.is_intersecting(
                visited_from_start, visited_from_goal)
            if intersect_node:
                return self.construct_path(intersect_node, parent_from_start, parent_from_goal, start, goal)

        return None

def main():   
    graph = BidirectionalSearch()
    n = int(input("enter the number of edges: "))
    for i in range(n):
        u,v = input("enter u and v: ").split(" ")
        graph.add_edge(u, v)
    

    start_node = input("enter the starting node: ")
    goal_node = input("enter the goal node: ")

    path = graph.bidirectional_search(start_node, goal_node)
    if path:
        print(f"Path between {start_node} and {goal_node}: {path}")
    else:
        print(f"No path found between {start_node} and {goal_node}")

if __name__ == "__main__":
    main()