import random

class CUBE(object):

    def __init__(self):
        self.FRONT=[[ random.randint(0, 6) for i in range(3)] for i in range(3) ]
        self.BACK= [[ 2 for i in range(3)] for i in range(3) ]
        self.UP=   [[ 3 for i in range(3)] for i in range(3) ]
        self.DOWN= [[ 4 for i in range(3)] for i in range(3) ]
        self.LEFT= [[ 5 for i in range(3)] for i in range(3) ]
        self.RIGHT=[[ 6 for i in range(3)] for i in range(3) ]
        


    def Turn_Сounterclockwise(self, flag=False):
        if flag:
            self.DOWN[0].reverse
            self.UP[2].reverse
            self.UP[2], self.DOWN[0] = self.DOWN[0], self.UP[2]
            for i in range(3):
                self.UP[2][i], self.RIGHT[i][0] = self.RIGHT[i][0], self.UP[2][i]
                self.DOWN[0][i], self.LEFT[i][2] = self.LEFT[i][2], self.DOWN[0][i]

        return [ [self.FRONT[j][i] for j in range(3) ]for i in range(3) ]



    def Turn_Clockwise(self, flag=False):
        
        self.FRONT.reverse()
        

        if flag:
            self.DOWN[0].reverse
            self.UP[2].reverse
            self.UP[2], self.DOWN[0] = self.DOWN[0], self.UP[2]
            for i in range(3):
                self.UP[2][i], self.LEFT[i][2] = self.LEFT[i][2], self.UP[2][i]
                self.DOWN[0][i], self.RIGHT[i][0] = self.RIGHT[i][0], self.DOWN[0][i]

        return [ [self.FRONT[j][i] for j in range(3) ]for i in range(3) ]
        


    def output(self):
        N="         "
        for i in range(3):
            print(N, self.UP[i], N, N)
        for i in range(3):
            print(self.LEFT[i], self.FRONT[i], self.RIGHT[i], self.BACK[i])
        for i in range(3):
            print(N, self.DOWN[i], N, N)


    def NewForward(self, NewF):
        pass

if __name__ == "__main__":
    a=CUBE()
    a.output()
    a.Turn_Clockwise()
    a.output()

    