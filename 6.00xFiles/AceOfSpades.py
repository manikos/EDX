#MAPPING OF CARDS (BASED ON RANK AND SUIT)

# A  2  3  4  5  6  7  8  9  10  J   Q  K
# 1  2  3  4  5  6  7  8  9  10 11  12  13

# Clubs  Diamonds  Hearts  Spades
#   0       1         2      3

class Card(object):
    suitList=['Clubs', 'Diamonds', 'Hearts', 'Spades'] #class variable
    rankList=['narf', 'Ace', '2', '3', '4', '5', '6',
              '7', '8', '9', '10', 'Jack', 'Queen', 'King'] #class variable

    def __init__(self, suit=0, rank=2):
        """suit=[0...3], rank=[1...13]"""
        self.suit=suit
        self.rank=rank

    def __str__(self):
        """Representation of each Card"""
        return self.rankList[self.rank] + ' of ' + self.suitList[self.suit]

    def __cmp__(self, other):
        """__cmp__ has two parameters, self and other.
        returns 1 if the first object is greater, -1 if
        the second object is greater, 0 if they are equal to each other."""
        #check the suits
        if self.suit>other.suit: return 1
        if self.suit<other.suit: return -1
        #suits are the same. Check ranks. Ace ranks first
        if self.rank==1 and other.rank!=1: return 1
        if self.rank!=1 and other.rank==1: return -1
        if self.rank>other.rank: return 1
        if self.rank<other.rank: return -1
        #ranks are the same. It's a tie
        return 0

class Deck(object):
    def __init__(self):
        """Fills up the Deck with Cards
        When init finishes, it will include a
        list of Card instances (objects)"""
        self.cards=[]
        for suit in range(len(Card.suitList)):
            for rank in range(1, len(Card.rankList)):
                self.cards.append(Card(suit,rank))

    def __str__(self):
        """Representation of the Deck"""
        s=''
        for i in range(len(self.cards)):
            s=s+ ' '*i + str(self.cards[i]) + '\n'
        return s

    def shuffle(self):
        """shuffles the deck"""
        import random
        nCards=len(self.cards)
        for i in range(nCards):
            j=random.randrange(i, nCards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def removeCard(self, card):
        """takes a Card object as an argument and removes it
        returns True if the card was in the deck and False otherwise"""
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def popCard(self):
        """removes each time the last Card object (aka a suit/rank pair)
        from the list (aka Deck)"""
        return self.cards.pop()

    def isEmpty(self):
        """checks if Deck is empty or not
        returns True or False"""
        return len(self.cards)==0

    def deal(self, hands, nCards=52):
        """Assumes hands (a list of Hand instances) is already defined"""
        nHands=len(hands)
        for i in range(nCards):
            if self.isEmpty():
                break
            card=self.popCard() #card variable is an object of type Card
            hand=hands[i%nHands] #modular arithmetic. wraps over and over through number of players (hands)
            hand.addCard(card)

    
class Hand(Deck):
    def __init__(self, name=""):
        """Name of player"""
        self.name=name
        self.cards=[]

    def __str__(self):
        s= self.name + "'s hand "
        if self.isEmpty():
            return s + 'is empty\n'
        else:
            return s + 'contains:\n' + Deck.__str__(self)

    def addCard(self, card):
        """Adds a specific Card (rank/value pair) to the player"""
        if card in self.cards:
            print 'The card <' + str(card) + '> is already owned'
            return
        self.cards.append(card)

class CardGame(object):
    def __init__(self):
        self.deck=Deck()
        self.deck.shuffle()
        

d=Deck()
d.shuffle()
nik=Hand('Nikolaras')
ira=Hand('Iraklis')
d.deal([nik,ira])
