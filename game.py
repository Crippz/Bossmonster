from player import Player 
from cards import Boss
import random
import json

rooms = ['Trap_Room_1', 'Monster_Room_1', 'Monster_Room_2', 'Trap_Room_2']
players = []

def setupPhase():
    x = int(input())
    y = random.sample(range(7), x)
    file = open('bosses.json')
    bosses = json.load(file)
#    print(bosses[0]['name'])

## init players
    for p in range(x):
        name = f"Player_{p}"
        boss = bosses[y[p]]['name']
        boss = Boss(bosses[y[p]]['name'], bosses[y[p]]['treasure'], bosses[y[p]]['xp'], bosses[y[p]]['power'] )
        players.append(Player(name, boss))

##    def __init__(self, name, treasure, xp, power):


def buildPhase():
    x = int(input())
    y = rooms[x]
    print(y)

def battlePhase():
    print("battle")


# while (True):
#     buildState()


setupPhase()
for player in players:
    print(player.name, player.boss)