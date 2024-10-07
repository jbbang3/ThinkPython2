"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card import Hand, Deck


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        self.ranks = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False
    
    def has_pair(self):
        """Returns True if the hand has a flush, False otherwise.
     
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False
    
    def has_twopair(self):
        self.suit_hist()
        c=0
        for val in self.ranks.values():
            if val >= 2:
                c+=1
            if c>=2:
                return True
        return False

    def has_three(self):
        self.suit_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False

    def has_straight(self):
        self.suit_hist()
        handrank=tuple(self.ranks.keys())
        handrank=sorted(handrank)
        c=0
        for i in range(len(handrank)-1):
            if handrank[i+1]-handrank[i] ==1:
                c+=1
        if c==4 and handrank[-1]==13 and handrank[0]==1:
            return True
        elif c==5:
            return True
        return False
    
    def has_full(self):
        self.suit_hist()
        c=0
        d=0
        for val in self.ranks.values():
            if val == 2:
                c+=1
            elif val>2:
                d+=1
        if c>=1 and d>=1:
            return True
        return False
    
    def has_four(self):
        self.suit_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False
    
    def has_strflush(self):
        if self.has_flush and self.has_straight:
            return True
        return False
    
    def high_card(self):
        self.suit_hist()
        handrank=tuple(self.ranks.keys())
        handrank=sorted(handrank, reverse=True)
        if handrank[-1]==1:
            self.label='Ace'
        else:
            self.label=str(handrank[0])
    
    def high_card2(self):
        self.cards.sort(key=lambda x: x[1])
        print(self.cards)
        if self.cards[0][1]==1:
            self.label='Ace'
        elif self.cards[-1][1]==11:
            self.label='Jack'
        elif self.cards[-1][1]==12:
            self.label='Queen'
        elif self.cards[-1][1]==13:
            self.label='King'
        else:
            self.label=str(self.cards[-1][1])
    
    def classify(self):
        if self.has_strflush():
            self.label='straight flush'
        if self.has_four():
            self.label='four of a kind'
        elif self.has_full():
            self.label='full house'
        elif self.has_flush():
            self.label='flush'
        elif self.has_straight():
            self.label='straight'
        elif self.has_three():
            self.label='three of a kind'
        elif self.has_twopair():
            self.label='two pair'
        elif self.has_pair():
            self.label='one pair'
        else:
            self.label='high card'

def count_prob(n,m):
    """ n= number of times to repeat. 
    m= size of hand
    """
    prob={}
    for i in range(n):
        deck=Deck()
        deck.shuffle()

        #shuffle card and deal:
        hand=PokerHand()
        deck.move_cards(hand,5)
        hand.classify()
        #print(hand)
        prob[hand.label]=prob.get(hand.label, 0) + 1
    return prob

if __name__ == '__main__':
    prob=count_prob(999,5)

    total=sum(prob.values())

    print("{:<20}{:<10}".format('hand', 'probability (%)'))
    print("="*30)
    for k,v in prob.items():
        print("{:<20}: {:.3f}%".format(k, v/total*100))


