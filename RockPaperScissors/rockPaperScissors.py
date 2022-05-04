import random

global pPlayer 
global pComputer 
pPlayer = 0
pComputer = 0
pdif = 0
lessLikely = False

options =	[(-9999, 'r'),(-9999,'p'),(-9999,'s')] 

print ("-----------------------------------ROCK PAPER SCISSORS   V1.0----------------------------------------------")
print("___________________________________ROCíO PERALES VALDES________________________________________________________")
print("\n The game ends if the point difference is of 4 or more, good luck! ")


def valid(cPlayer):
    stop = False
    while stop == False:
        if cPlayer == "r" or cPlayer == "p" or cPlayer == "s":
            stop = True
        else:
            cPlayer = input("Please enter a valid input: \n - r for rock \n - p for paper  \n - s for scissors \n")
    return(cPlayer)

def bestOp(options):  # this function will give back the best choice for the machine to take. It does this by giving the cancee to be random or by using a reasoning in which the machine chooses to play the one it has lost the least at (if the machine has never lost when using scissor, it will use scissor)
    decisionMaker = random.random()
    if(decisionMaker < (1/8)):
        return('r')
    elif(decisionMaker < (2/8)):
        return('p')
    elif(decisionMaker < (3/8)):
        return('s')
    else:
        return(options[0][1])



def winGame(pl, c):
    if(pl == c):
        return(2)
    if (pl == "r" and c == "s" or pl == "p" and c == "r" or pl == "s" and c == "p"):
        return(1)
    else:
        return(0)


while(pdif < 4):
    cPlayer = input("\n ♫ Rock, paper, scissors ♫ (r/p/s): ")
    cPlayer = valid(cPlayer)
    cComputer = bestOp(options)
    print(cPlayer, "vs", cComputer)
    if(winGame(cPlayer,cComputer)==1):
        print("WIN")
        pPlayer +=1
        for i in range(3):
            if (options[i][1]== cComputer):
                y = list(options[i])
                y[0] += 1
                options[i] = tuple(y)
                options = sorted(options)
    elif(winGame(cPlayer,cComputer)==0):
        print("LOSE")
        pComputer +=1
        for i in range(3):
            if (options[i][1]== cComputer):
                y = list(options[i])
                y[0] -= 1
                options[i] = tuple(y)
                options = sorted(options)
    else:
        print("TIE")
    
    print("\n    S\u0332C\u0332O\u0332R\u0332E\u0332B\u0332O\u0332A\u0332R\u0332D\u0332: ")
    print(f"You: {pPlayer} || Computer {pComputer}")
    pdif = abs(pPlayer-pComputer)

if(pPlayer > pComputer):
    print("The game has ended, well done you won!")
else:
    print("The game has ended, unfortunately you lost!")