import random

class Pile:
    def __init__(self):
        self.cards = []

    def __init__(self, cards):
        self.cards = cards
    
    def shuffle(self):
        for i in range(len(self.cards) -1, 0, -1 ):
            j = random.randint(0, i+1)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def add(self, card):
        self.cards.append(card)

    def count(self):
        return len(self.cards)
    
    def display(self):
        for index, card  in enumerate(self.cards):
            print(index)
            card.display()

    def display(self, type):
        for index, card  in enumerate(self.cards):
            if(card.type == type):
                print(index)
                card.display()
                