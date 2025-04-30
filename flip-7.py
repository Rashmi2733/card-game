import numpy as np
from random import shuffle

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def create_cards(num):
    num_vals = num * [num]
    return num_vals

card_deck = []
for num in nums:
    card_deck.extend(create_cards(num))

shuffle(card_deck)

players = {f'player_{i+1}': [] for i in range(3)}

player_state = {f'player_{i+1}': False for i in range(3)}
player_state['player_1']

final_copy = card_deck.copy()
for i in range(30):
    if player_state['player_1'] == False: 
        if final_copy[0] not in players['player_1']:
            players['player_1'].append(final_copy[0])
            # print("one:", player1)        
        else:
            print("Game over for player one:", final_copy[0])
            player_state['player_1'] = True
            final_copy.pop(0)
            continue
    else:
        pass

    final_copy.pop(0)

    if player_state['player_2'] == False:
        if final_copy[0] not in players['player_2']:
            players['player_2'].append(final_copy[0])
            # print("two:", player2)        
        else:
            print("Game over for player two:", final_copy[0])
            player_state['player_2'] = True
            final_copy.pop(0)
            continue
    else:
        pass

    final_copy.pop(0)

    if player_state['player_3'] == False:
        if final_copy[0] not in players['player_3']:
            players['player_3'].append(final_copy[0])
            # print("three:", player3)        
        else:
            print("Game over for player three:", final_copy[0])
            player_state['player_3'] = True
            final_copy.pop(0)
            continue
    else:
        pass
    
    final_copy.pop(0)
    
    if player_state['player_1'] == True & player_state['player_2'] == True & player_state['player_3'] == True:
        print("GAME OVER")
        break
    
print("one:", players['player_1'])
print("two:", players['player_2'])
print("three:", players['player_3'])