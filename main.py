import random
player_in = True
dealer_in = True

#deck of cards
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
player_hand = []
dealer_hand = []

#deal the cards
def deal_card(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

#hand value (o ÁS está sendo calculado sempre com o primeiro valor atribuido a ela, você não consegue mudar o valor do Ás entre 1 e 11 depois que receber outra carta).
def total(turn):
    total_value = 0
    face = ['J', 'K', 'Q']
    for card in turn:
        if card in range(1, 11):
            total_value += card
        elif card in face:
            total_value += 10
        else:
            if total_value >= 11:
                total_value += 1
            else:
                total_value += 11
    return total_value

#check winner
def reveal_dealer_hand():
    if len(dealer_hand) == 2:
        return dealer_hand[0]
    elif len(dealer_hand) > 2:
        return dealer_hand

#gameloop
for _ in range(2):
    deal_card(dealer_hand)
    deal_card(player_hand)

while player_in or dealer_in:
    print(f"Dealer has {reveal_dealer_hand()}")
    print(f"You have {player_hand} for a total of {total(player_hand)}")
    if player_in:
        stay_or_hit = input("1: Stay\n2: Hit\n")
    if total(dealer_hand) > 16 or total(dealer_hand) >= total(player_'hand):
        dealer_in = False
    else:
        deal_card(dealer_hand)
    if stay_or_hit == '1':
        player_in = False
    elif stay_or_hit == '2':
        deal_card(player_hand)
    else:
        print('Try 1 for Stay and 2 for Hit')
    if total(player_hand) >= 21:
        break
    elif total(dealer_hand) >= 21:
        break
if total(player_hand) == 21:
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("BLACKJACK YOU WIN!")
elif total(player_hand) > 21:
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("YOU BUST, YOU LOSE!")
elif total(player_hand) == total(dealer_hand):
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("ITS A DRAW")
elif total(dealer_hand) > 21 and total(player_hand) <= 21:
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("DEALER BUSTS YOU WIN!!")
elif total(player_hand) > total(dealer_hand):
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("YOU WIN!!")
elif total(dealer_hand) > total(player_hand):
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("YOU LOSE")