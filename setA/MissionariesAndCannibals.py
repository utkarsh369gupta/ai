from collections import deque

class MissionariesAndCannibals:
    def __init__(self):
        self.start_state = (3, 3, 1) 
        self.goal_state = (0, 0, 0)  
        self.visited = set()         
        self.parent = {}       

    def is_valid(self, state):
        M_left, C_left, _ = state
        M_right, C_right = 3 - M_left, 3 - C_left
        
        if M_left < 0 or C_left < 0 or M_right < 0 or C_right < 0:
            return False       
        if M_left > 0 and M_left < C_left:
            return False
        if M_right > 0 and M_right < C_right:
            return False
        
        return True

    def get_neighbors(self, state):
        M_left, C_left, boat_pos = state
        moves = []
        
        if boat_pos == 1: 
            for M_move, C_move in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
                new_state = (M_left - M_move, C_left - C_move, 0)
                if self.is_valid(new_state):
                    moves.append(new_state)
        else:  
            for M_move, C_move in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
                new_state = (M_left + M_move, C_left + C_move, 1)
                if self.is_valid(new_state):
                    moves.append(new_state)
        
        return moves

    def bfs(self):
        q = deque([self.start_state])
        self.visited.add(self.start_state)
        self.parent[self.start_state] = None
        
        while q:
            current_state = q.popleft()
            
            if current_state == self.goal_state:
                return self.reconstruct_path(current_state)
            
            for neighbor in self.get_neighbors(current_state):
                if neighbor not in self.visited:
                    self.visited.add(neighbor)
                    self.parent[neighbor] = current_state
                    q.append(neighbor)
        
        return None

    def reconstruct_path(self, state):
        path = []
        while state:
            path.append(state)
            state = self.parent[state]
        return path[::-1]

def main():
    problem = MissionariesAndCannibals()
    solution = problem.bfs()

    if solution:
        print("Solution found!")
        for step in solution:
            print(step)
    else:
        print("No solution exists!")
        
if __name__ == "__main__":
    main()
