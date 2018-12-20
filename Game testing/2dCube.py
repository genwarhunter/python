import msvcrt
import turns, Cube


def main():
    
    kub=Cube.CUBE()
    kub.output()

    l='start'
    while l!='quit':
        l=input('way: ')
        if l!='onclock' and l!='overclock':
            edge=input('edge: ')
        if l=='up':
            if edge=='1':
                kub.NewForward(kub.LEFT)
                kub.Turn_Сounterclockwise(kub.FORWARD, True)
                kub.NewForward(kub.RIGHT)
            elif edge == '3':
                kub.NewForward(kub.RIGHT)
                kub.Turn_Clockwise(kub.FORWARD, True)
                kub.NewForward(kub.LEFT)

        elif l == 'down':
            if edge==1:
                kub.NewForward(kub.LEFT)
                kub.Turn_Clockwise(kub.FORWARD, True)
                kub.NewForward(kub.RIGHT)
            elif edge == 3:
                kub.NewForward(kub.RIGHT)
                kub.Turn_Сounterclockwise(kub.FORWARD, True)
                kub.NewForward(kub.LEFT)
        elif l== 'left':
            pass
        elif l=='right':
            pass
        elif l=='onclock':
            kub.FORWARD = kub.Turn_Clockwise(kub.FORWARD, True)
        elif l=='overclock':
            kub.FORWARD = kub.Turn_Сounterclockwise(kub.FORWARD, True)

        kub.output()
        

        

if __name__ == "__main__":
    main()