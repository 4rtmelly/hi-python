import random

def GuessingGame(nbAlea):
    guess = 0
    while guess != nbAlea:
        guess = int(input("Devinez le nombre mystère : "))
        if guess > nbAlea:
            print(" Le nombre mystère est plus petit")
        elif guess < nbAlea:
            print(" Le nombre mystère est plus grand")
    print("Felicitations !")

if __name__ == '__main__':

    nbAlea = random.randint(0,10)
    GuessingGame(nbAlea)


