# Poker Game Engine
# Willam Carpenter
# April 2024


import numpy as np
import random

# class Deck - a deck of cards 
# class Pot - represents the game pot ... 
# class Dealer - deals out cards from a deck  
# class Player - one poker player that will have a given hand, etc. 
# class Game - this will be a interesting program ... simulates a game and keeps all the game history (each hand, what the players played, bet, won, etc. lots of data)
# class Rankings - hand rankings 
# use tuples to create the deck

card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(card, category) for category in card_categories for card in cards_list]

newdeck = deck.random.shuffle()

#%%

class Deck:
    
    '''
    Poker Deck 
    '''

    def __init__(self):

        self.cards = self.create_deck()
        self.size  = self.deck_size()

    def create_deck(self):
        # create the initial version of a deck
        
        card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        
        cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        
        deck = [(card, category) for category in card_categories for card in cards_list]
        
        return deck
    
    def __str__(self):
        s = ""
        for c in self.cards:
            s += "%s\n" % c
        return s    
    
    
    def deck_size(self):
        return len(self.cards)  # should return 52 cards unless deck is smaller
  
    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.cards)
    
    def card(self):
        return self.cards.pop() 
        
    def hand(self):
        # deal a two-card hand to a player
        pass    

def main():
    
    # creates a fresh deck of 52 cards, not shuffled 
    game_deck = Deck()
    
    print(game_deck.cards)
    print("   ")
    
    print(type(game_deck.cards))
    
    print(game_deck.deck_size())
    print("   ")
    
    game_deck.shuffle()
    
    print(game_deck.cards)
    
    card = game_deck.card()
    print("   ")
    print(card)
    

if __name__ == "__main__":

    main()


