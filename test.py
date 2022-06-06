class Pile:
    def __init__(self):
        self.letters = ['a','b','c']

    def drop(self):
        n = self.nums.pop()
        print(n)

    def display(self):
        print(self.nums)


def lol(m):
    m.drop()

p = Pile()

for index, letter in enumerate(p.letters):
    print(index, letter)

