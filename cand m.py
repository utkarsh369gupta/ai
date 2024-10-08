from collections import deque

class MissionariesAndCannibals:
    def __init__(self):
        self.start_state = (3, 3, 1)  # (Missionaries on left, Cannibals on left, boat position)
        self.goal_state = (0, 0, 0)   # (Missionaries on right, Cannibals on right, boat position)
        self.visited = set()          # To keep track of visited states
        self.parent = {}              # To reconstruct the path

    def is_valid(self, state):
        """ Check if the state is valid (missionaries are not outnumbered by cannibals) """
        M_left, C_left, _ = state
        M_right, C_right = 3 - M_left, 3 - C_left
        
        # Ensure no negative values of missionaries or cannibals on either side
        if M_left < 0 or C_left < 0 or M_right < 0 or C_right < 0:
            return False
        
        # No side should have more cannibals than missionaries (except when missionaries are 0)
        if M_left > 0 and M_left < C_left:
            return False
        if M_right > 0 and M_right < C_right:
            return False
        
        return True

    def get_neighbors(self, state):
        """ Generate all possible valid next states from the current state """
        M_left, C_left, boat_pos = state
        moves = []
        
        if boat_pos == 1:  # Boat on left side
            # Possible moves: (1,0), (2,0), (0,1), (0,2), (1,1)
            for M_move, C_move in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
                new_state = (M_left - M_move, C_left - C_move, 0)
                if self.is_valid(new_state):
                    moves.append(new_state)
        else:  # Boat on right side
            # Possible moves: (1,0), (2,0), (0,1), (0,2), (1,1)
            for M_move, C_move in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
                new_state = (M_left + M_move, C_left + C_move, 1)
                if self.is_valid(new_state):
                    moves.append(new_state)
        
        return moves

    def bfs(self):
        """ Breadth-first search to find the solution """
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
        
        return None  # No solution found

    def reconstruct_path(self, state):
        """ Reconstruct the path from the goal state back to the start state """
        path = []
        while state:
            path.append(state)
            state = self.parent[state]
        return path[::-1]

# Example usage
problem = MissionariesAndCannibals()
solution = problem.bfs()

if solution:
    print("Solution found!")
    for step in solution:
        print(step)
else:
    print("No solution exists!")
