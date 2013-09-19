#!/usr/bin/env python
# deck of cards
# by Adam Cotenoff (@acotenoff)
# 18 September 2013

import random

def deck():
    deck = []
    for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
        for num in range(2,15):
            deck.append([num, suit])
    return deck

def card_name(card):
    if card == 11:
        return 'Jack'
    elif card == 12:
        return 'Queen'
    elif card == 13:
        return 'King'
    elif card == 14:
        return 'Ace'
    else:
        return str(card)

#def shuffles(deck):
#    shuffledDeck = random.shuffle(deck)
 #   return shuffledDeck
 
def view_cards():
    deck2 = deck()
    for i in range(0, len(deck2)):
        print card_name(deck2[i][0]) + ' of ' + str(deck2[i][1])

def main():
    view_cards()

if __name__ == '__main__':
    main()