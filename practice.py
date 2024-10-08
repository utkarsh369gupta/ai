

class cansm:
    def __init__(self):
        self.start = (3, 3, 1)
        self.goal = (0, 0, 0)
        self.visited = set()
        self.parent = {}

    def is_valid(self, state):
        ml, cl, _ = state
        mr, cr = 3-ml, 3-cl

        if ml < 0 or cl < 0 or mr < 0 or cr < 0:
            return False
        if ml > 0 and ml < cl:
            return False
        if mr > 0 and mr < cr:
            return False
        return True

    def get_neighbors(self, state):
        ml, cl, b = state
        move = []

        if b == 1:
            for mm, cm in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
                nm = (ml-mm, cl-cm, 0)
                if self.is_valid(nm):
                    move.append(nm)
        else:
            for mm, cm in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
                nm = (ml+mm, cl+cm, 1)
                if self.is_valid(nm):
                    move.append(nm)
                    
        return move
    
    def bfs(self):
        q = deque([self.start])
        self.visited.add(self.start)
        self.parent[self.start] = None
        
        while q:
            curr = q.popleft()
            if curr == self.goal:
                return cnt(curr)
        
