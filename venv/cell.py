class cell:
    def __init__(self, position:(), parent:()):
        # f = g + h
        self.position = position
        self.parent = parent
        self.f = 0 # Total distance
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to end node

    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position

    # Sort nodes
    def __lt__(self, other):
        return self.f < other.f

    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))
