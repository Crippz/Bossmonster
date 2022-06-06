class Card:

  def __init__(self, name, type):
    self.name = name
    self.type = type


class BossMonster(Card):
    def __init__(self, name, treasure, xp, power):
        self.treasure = treasure
        self.xp = xp
        self.power = power
        super().__init__(name, 'BossMonster')

    def display(self):
        print(f'Name: {self.name}, Type: {self.type}, XP: {self.xp} \nPower: {self.power}' )

class Hero(Card):
    def __init__(self, name, type, health, treasure):
        self.health = health
        self.treasure = treasure
        super().__init__(name, type)
    
    def display(self):
        print(f'Name: {self.name}, Type: {self.type}, Health: {self.health}, Treasure: {self.treasure}' )    


class Room(Card):
    def __init__(self, name, type, treasure, damage, effect):
        self.treasure = treasure
        self.damage = damage
        self.effect = effect
        super().__init__(name, type)
    
    def display(self):
        print(f'Name: {self.name}, Type: {self.type}, Damage: {self.damage}, Treasure: {self.treasure} \nEffect: {self.effect}' )            


class MonsterRoom(Room):
    def __init__(self, name, type, treasure, damage, effect):
        super().__init__(name, type, treasure, damage, effect)

class AdvancedMonsterRoom(MonsterRoom):
    def __init__(self, name, type, treasure, damage, effect):
        super().__init__(name, type, treasure, damage, effect)

class TrapRoom(Room):
    def __init__(self, name, type, treasure, damage, effect):
        super().__init__(name, type, treasure, damage, effect)

class AdvancedTrapRoom(TrapRoom):
    def __init__(self, name, type, treasure, damage, effect):
        super().__init__(name, type, treasure, damage, effect)

class SpellCard(Card):
    def __init__(self, name, phase, effect):
        self.phase = phase
        self.effect = effect
        super().__init__(name, 'SpellCard')

    def display(self):
        print(f'Name: {self.name}, Phase: {self.phase}, \nEffect: {self.effect}' )    


