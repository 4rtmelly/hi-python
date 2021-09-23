import random
import sys
# 1 = rock
# 2 = paper 
# 3 = scissors
def rps():
    moveAlea = str(random.randint(1,3))
    movePlayer = (input('Choisissez un nombre qui détermine votre choix : ').strip())
    while movePlayer!="1" and movePlayer!="2" and movePlayer!="3" :
        movePlayer = (input('Choisissez un nombre qui détermine votre choix : ').strip())

    while movePlayer == moveAlea : 
        print("Egalité")
        movePlayer = (input('Choisissez un nombre qui détermine votre choix : ').strip())
        moveAlea = str(random.randint(1,3))
        
    print('Le choix du Bot était : ', moveAlea)
    if (movePlayer == '2' and moveAlea == '1') or (movePlayer == '1' and moveAlea == '3') or (movePlayer == '3' and moveAlea == '2'): 
        print("Gagné")
    #elif movePlayer == moveAlea:
    #    print('Egalité !')
    else :
        print("Perdu")

if __name__ == '__main__':
    print('# 1 = rock \n# 2 = paper \n# 3 = scissors')
    rps()
    test = False
    while test==False:
        newGame = (str(input('Voulez vous faire une partie : o/n \n').strip()))
        while newGame!='o' and newGame!='n' :
            newGame = (str(input('Voulez vous faire une partie : o/n \n').strip()))
        if  newGame == 'o':
            rps()
        if  newGame == 'n':
            test = True
            print("A la prochaine !")

