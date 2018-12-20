import random

class CUBE(object):

    def __init__(self):
        self.FRONT=[[ random.randint(0, 6) for i in range(3)] for i in range(3) ]
        self.BACK= [[ 2 for i in range(3)] for i in range(3) ]
        self.UP=   [[ 3 for i in range(3)] for i in range(3) ]
        self.DOWN= [[ 4 for i in range(3)] for i in range(3) ]
        self.LEFT= [[ 5 for i in range(3)] for i in range(3) ]
        self.RIGHT=[[ 6 for i in range(3)] for i in range(3) ]
        


    def Turn_Сounterclockwise(self, edge, flag=False):
        if flag:
            self.DOWN[0].reverse
            self.UP[2].reverse
            self.UP[2], self.DOWN[0] = self.DOWN[0], self.UP[2]
            for i in range(3):
                self.UP[2][i], self.RIGHT[i][0] = self.RIGHT[i][0], self.UP[2][i]
                self.DOWN[0][i], self.LEFT[i][2] = self.LEFT[i][2], self.DOWN[0][i]

        return [ [edge[j][i] for j in range(3) ]for i in range(3) ]



    def Turn_Clockwise(self, edge, flag=False):
        
        edge.reverse()
        

        if flag:
            self.DOWN[0].reverse
            self.UP[2].reverse
            self.UP[2], self.DOWN[0] = self.DOWN[0], self.UP[2]
            for i in range(3):
                self.UP[2][i], self.LEFT[i][2] = self.LEFT[i][2], self.UP[2][i]
                self.DOWN[0][i], self.RIGHT[i][0] = self.RIGHT[i][0], self.DOWN[0][i]

        return [ [edge[j][i] for j in range(3) ]for i in range(3) ]
        


    def output(self):
        N="         "
        for i in range(3):
            print(N, self.UP[i], N, N)
        for i in range(3):
            print(self.LEFT[i], self.FRONT[i], self.RIGHT[i], self.BACK[i])
        for i in range(3):
            print(N, self.DOWN[i], N, N)


    def NewForward(self, NewF):
        #buff=[[ ' ' for i in range(3)]for i in range (3)]
        if NewF == self.LEFT:
            for i in range(3):
                for j in range(3):
                    self.RIGHT[i][j], self.FRONT[i][j] = self.FRONT[i][j], self.RIGHT[i][j]
                    self.BACK[i][j], self.FRONT[i][j] = self.FRONT[i][j], self.BACK[i][j]
                    self.LEFT[i][j], self.FRONT[i][j] = self.FRONT[i][j], self.LEFT[i][j]
            self.Turn_Clockwise(self.UP)
            self.Turn_Сounterclockwise(self.DOWN)

        elif NewF == self.RIGHT:
            for i in range(3):
                for j in range(3):
                    self.LEFT[i][j], self.FRONT[i][j] = self.FRONT[i][j], self.LEFT[i][j]
                    self.BACK[i][j], self.FRONT[i][j] = self.FRONT[i][j], self.BACK[i][j]
                    self.RIGHT[i][j], self.FRONT[i][j] = self.FRONT[i][j], self.RIGHT[i][j]
            self.Turn_Clockwise(self.DOWN)
            self.Turn_Сounterclockwise(self.UP)

        elif NewF == self.UP:
            for i in range(3):
                for j in range(3):
                    self.DOWN[i][j], self.FRONT[i][j] = self.FRONT[i][j], self.DOWN[i][j]
                    self.BACK[i][j], self.FRONT[i][j] = self.FRONT[i][j], self.BACK[i][j]
                    self.UP[i][j], self.FRONT[i][j] = self.FRONT[i][j], self.UP[i][j]
            self.Turn_Clockwise(self.LEFT)
            self.Turn_Сounterclockwise(self.RIGHT)

        elif NewF == self.DOWN:
            for i in range(3):
                for j in range(3):
                    self.UP[i][j], self.FRONT[i][j] = self.FRONT[i][j], self.UP[i][j]
                    self.BACK[i][j], self.FRONT[i][j] = self.FRONT[i][j], self.BACK[i][j]
                    self.DOWN[i][j], self.FRONT[i][j] = self.FRONT[i][j], self.DOWN[i][j]
            self.Turn_Clockwise(self.RIGHT)
            self.Turn_Сounterclockwise(self.LEFT)

        elif NewF == self.BACK:
            for i in range(2):
                for i in range(3):
                    for j in range(3):
                        self.LEFT[i][j], self.FRONT[i][j] = self.FRONT[i][j], self.LEFT[i][j]
                        self.BACK[i][j], self.FRONT[i][j] = self.FRONT[i][j], self.BACK[i][j]
                        self.RIGHT[i][j], self.FRONT[i][j] = self.FRONT[i][j], self.RIGHT[i][j]
            self.Turn_Clockwise(self.DOWN)
            self.Turn_Сounterclockwise(self.UP)


        

if __name__ == "__main__":
    a=CUBE()
    a.output()
    a.NewForward(a.BACK)
    a.output()

    