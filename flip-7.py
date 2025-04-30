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

##getting number of players from user (between 3 and 8)

while True:
  try:
    num_players = input("Enter a number between 3 and 8: ")
    if num_players.isdigit():
       num_players=int(num_players)
    else:   
       raise ValueError()
    if 3 <= num_players <= 8:
        break
    raise ValueError()
  except ValueError:
    print("Input must be an integer between 3 and 8.")


players = {f'player_{i+1}': [] for i in range(num_players)}

player_state = {f'player_{i+1}': False for i in range(num_players)}

def give_card(deck, player_num):
    if player_state[player_num] == False: 
        if deck[0] not in players[player_num]:
            players[player_num].append(deck[0])
        else:
            print(f"Game over for {player_num}, repeated card:", deck[0])
            player_state[player_num] = True
            deck.pop(0)
            return deck
    
    deck.pop(0) 
    return deck

#Main game
deck_copy = card_deck.copy()
while len(deck_copy) > 0:
    for player in sorted(list(players.keys())):
        # print(player)
        give_card(deck_copy, player)
        if len(deck_copy) == 0: break

    if all(player_state.values()) == True:
        print("\nGAME OVER - All the players are out!")
        break
    elif len(deck_copy) == 0:
        print("\nCARDS FINISHED - Game over!")
        break

#Results of the game
print("\nFinal cards:")
for player, cards in players.items():
    print(f"{player}: {cards}")


total_points = []
for player, point in players.items():
    points = sum(point)
    total_points.append((points, player))

winner = max(total_points)[1]
winning_points = max(total_points)[0]
print(f'Winner of the game is {winner} with {winning_points} points.')

