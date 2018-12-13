class Edge():
    

    def __init__(self, a, b, weight):
        self.a = int(a)
        self.b = int(b)
        self.weight = int(weight)


    def __lt__ (self, other):
        if self.weight < other.weight:
            return True
        return False

