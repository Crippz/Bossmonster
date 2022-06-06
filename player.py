from pile import Pile

class Player:
    def __init__(self, name, boss):
        self.name = name
        self.boss = boss
        self.dungeon = [None] * 6
        self.dungeon[0] = boss
        self.lives = 5
        self.souls = 0
        self.rooms = Pile()
        self.spells = Pile()

    def draw(self, pile):
        n_pile = pile
        card = n_pile.pop()
        if(card.type == 'Spell'):
            self.spells.add(card)
        else:
            self.rooms.add(card)

    def draw_n(self, pile, number):
        n_pile = pile
        cards = n_pile.pop(number)
        if(cards[0].type == 'Spell'):
            for c in cards:
                self.spells.add(c)
        else:
            for c in cards:
                self.rooms.add(c)        


    def draw_specific(self, pile, number, type):
        pile.display(type)
        i = int(input())
        card = pile[i]
        pile.remove(i)
        pile.shuffle()
        if(type == 'Spellcard'):
            self.spells.add(card)
        else:
            self.rooms.add(card)

        