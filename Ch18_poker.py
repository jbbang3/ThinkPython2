import random

class Card:
    """Represent a standard playing card
    spade --> 3
    heards --> 2
    diamonds --> 1
    clubs --> 0
    """

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
              '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '{} of {}'.format(Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

class Deck:
    
    def __init__(self):
        self.cards =[]
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()
    
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
    
    def deal_hands(self, num_hand=5, num_cards=10):
        hands=[[]]
        for i in range(num_hand):
            istr=str(i)
            handlabel='_'.join(['hand',istr])
            c=Hand(handlabel)
            self.move_cards(c,num_cards)
            hands.append(c)
        return hands


class Hand(Deck):
    """Represents a hand of plyaing cards."""

    #Hand will run this init function, NOT the one in Deck.
    def __init__(self, label=''):
        self.cards = []
        self.label = label
    
    def __str__(self):
        return f'{self.label}: ' + ', '.join(str(card) for card in self.cards)

def find_defining_class(obj, meth_name):
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty

def main():
    card1 = Card(2, 11)
    deck=Deck()
    hands=deck.deal_hands(3, 5)

    for h in hands:
        print(h)


if __name__=="__main__":
    main()