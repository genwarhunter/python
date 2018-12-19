import msvcrt
import turns, Cube


def main():
    
    kub=Cube.CUBE()
    kub.output()

    l='start'
    while l!='quit':
        l=input('way: ')
        
        if l=='up':
            pass

        elif l == 'down':
            pass
        elif l== 'left':
            pass

        elif l=='right':
            pass

        elif l=='onclock':
            kub.Turn_Clockwise(True)
        elif l=='overclock':
            kub.Turn_Сounterclockwise(True)

        kub.output()
        

        

if __name__ == "__main__":
    main()