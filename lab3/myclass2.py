class Edge():
    

    def __init__(self, a, weight):
        self.a, self.weight= int(a), int(weight)

    def __lt__ (self, other):
        if self.weight < other.weight:
            return True
        return False

