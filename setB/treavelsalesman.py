class GreedyTSP:
    def __init__(self, num_cities):
        self.graph = [[0] * num_cities for _ in range(num_cities)]
        self.num_cities = num_cities

    def add_edge(self, u, v, cost):
        self.graph[u][v] = cost
        self.graph[v][u] = cost

    def tsp(self, start):
        visited = [False] * self.num_cities
        visited[start] = True
        current_city = start
        total_cost = 0

        for _ in range(self.num_cities - 1):
            nearest_city = None
            nearest_cost = float('inf')

            for city in range(self.num_cities):
                if not visited[city] and self.graph[current_city][city] < nearest_cost:
                    nearest_city = city
                    nearest_cost = self.graph[current_city][city]

            visited[nearest_city] = True
            total_cost += nearest_cost
            current_city = nearest_city

        # Return to the start city
        total_cost += self.graph[current_city][start]
        return total_cost



num_cities = int(input("Enter the number of cities: "))
tsp_solver = GreedyTSP(num_cities)

edges = int(input("Enter the number of edges: "))
for _ in range(edges):
    u, v, cost = map(int, input("Enter two cities and the cost between them: ").split())
    tsp_solver.add_edge(u, v, cost)

start_city = int(input("Enter the starting city: "))
optimal_cost = tsp_solver.tsp(start_city)
print(f"The total cost for the Greedy TSP starting from city {start_city} is: {optimal_cost}")

# Example usage
# num_cities = 4
# tsp_solver = GreedyTSP(num_cities)
# print(tsp_solver.graph)
# # Add edges (city1, city2, cost)
# tsp_solver.add_edge(0, 1, 10)
# tsp_solver.add_edge(0, 2, 15)
# tsp_solver.add_edge(0, 3, 20)
# tsp_solver.add_edge(1, 2, 35)
# tsp_solver.add_edge(1, 3, 25)
# tsp_solver.add_edge(2, 3, 30)


# start_city = 0  # Starting city
# optimal_cost = tsp_solver.tsp(start_city)
# print(f"The total cost for the Greedy TSP starting from city {start_city} is: {optimal_cost}")
