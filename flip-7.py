import numpy as np
from random import shuffle

ones = 1 * [1]
twos = 2 * [2]
threes = 3 * [3]
fours = 4 * [4]
fives = 5 * [5]
sixes = 6 * [6]
sevens = 7 * [7]
eights = 8 * [8]
nines = 9 * [9]
tens = 10 * [10]
elevens = 11 * [11]
twelves = 12 * [12]

final = ones + twos + threes + fours + fives + sixes + sevens + eights + nines +tens+elevens+twelves

shuffle(final)

player1 = []
player2 = []
player3 = []

player1_end = False
player2_end = False
player3_end = False

final_copy = final.copy()
for i in range(30):
    if player1_end == False: 
        if final_copy[0] not in player1:
            player1.append(final_copy[0])
            # print("one:", player1)        
        else:
            print("Game over for player one:", final_copy[0])
            player1_end = True
            final_copy.pop(0)
            continue
    else:
        pass

    final_copy.pop(0)

    if player2_end == False:
        if final_copy[0] not in player2:
            player2.append(final_copy[0])
            # print("two:", player2)        
        else:
            print("Game over for player two:", final_copy[0])
            player2_end = True
            final_copy.pop(0)
            continue
    else:
        pass

    final_copy.pop(0)

    if player3_end == False:
        if final_copy[0] not in player3:
            player3.append(final_copy[0])
            # print("three:", player3)        
        else:
            print("Game over for player three:", final_copy[0])
            player3_end = True
            final_copy.pop(0)
            continue
    else:
        pass
    
    final_copy.pop(0)
    
    if player1_end == True & player2_end == True & player3_end == True:
        print("GAME OVER")
        break
    
print("one:", player1)
print("two:", player2)
print("three:", player3)