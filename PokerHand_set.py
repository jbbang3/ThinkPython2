"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card import Hand, Deck

class Hist(dict):

    def __init__(self, seq=[]):
        for x in seq:
            self.count(x)
    
    def count(self,x, f=1):
        self[x]=self.get(x,0)+f
        if self[x]==0:
            del self[x]

class PokerHand(Hand):
    """Represents a poker hand."""

    all_labels = ['straightflush', 'fourkind', 'fullhouse', 'flush',
                  'straight', 'threekind', 'twopair', 'pair', 'highcard']

    def make_histogram(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = Hist()
        self.ranks = Hist()

        for c in self.cards:
            self.suits.count(c.suit)
            self.ranks.count(c.rank)

        self.sets=list(self.ranks.values())
        self.sets.sort(reverse=True)

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        for val in self.suits.values():
            if val >= 5:
                return True
        return False
    
    def check_sets(self, *z):
        for need, have in zip(z,self.sets):
            if need>have:
                return False
        return True

    def has_pair(self):
        """ has a pair  """
        return self.check_sets(2)
    
    def has_twopair(self):
        return self.check_sets(2,2)

    def has_threekind(self):
        return self.check_sets(3)

    def has_straight(self):
        ranks=self.ranks.copy()
        ranks[14]=ranks.get(1,0)

        return self.in_a_row(ranks,5)
    
    def in_a_row(self, ranks, n=5):
        c=0
        for i in range(1,15):
            if ranks.get(i,0):
                c+=0
                if c==n:
                    return True
            else:
                c=0
        return False

    def has_fullhouse(self):
        return self.check_sets(3,2)
    
    def has_fourkind(self):
        return self.check_sets(4)
    
    def has_straightflush(self):
        if self.has_flush and self.has_straight:
            return True
        return False
    
    def has_highcard(self):
        return len(self.cards)

    #def high_card(self):
    #    self.suit_hist()
    #    handrank=tuple(self.ranks.keys())
    #    handrank=sorted(handrank, reverse=True)
    #    if handrank[-1]==1:
    #        self.label='Ace'
    #    else:
    #        self.label=str(handrank[0])
    
    #def high_card(self):
    #    self.cards.sort(key=lambda x: x[1])
    #    print(self.cards)
    #    if self.cards[0][1]==1:
    #        self.label='Ace'
    #    elif self.cards[-1][1]==11:
    #        self.label='Jack'
    #    elif self.cards[-1][1]==12:
    #        self.label='Queen'
    #    elif self.cards[-1][1]==13:
    #        self.label='King'
    #    else:
    #        self.label=str(self.cards[-1][1])
    
    def classify(self):
        
        self.make_histogram()
        self.labels =[]
        for label in PokerHand.all_labels:
            f=getattr(self, "has_"+label)
            if f():
                self.labels.append(label)


class PokerDeck(Deck):

    def deal_hands(self, num_cards=5, num_hands=10):
        hands=[]
        for i in range(num_hands):
            hand = PokerHand()
            self.move_cards(hand, num_cards)
            hand.classify()
            hands.append(hand)
        return hands

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

def main():
    lhist=Hist()    #label history

    n=10000
    for i in range(n):
        if i*1000 ==0:
            print(i)
        
        deck=PokerDeck()
        deck.shuffle()

        hands=deck.deal_hands(7,7)
        for hand in hands:
            for label in hand.labels:
                lhist.count(label)

    total=7.0*n
    print(total, 'hand_dealt: ')

    for label in PokerHand.all_labels:
        freq=lhist.get(label,0)
        if freq ==0:
            continue
        p=total/freq
        print('{} happens one time in {:.2f}'.format(label,p))



if __name__ == '__main__':
    main()