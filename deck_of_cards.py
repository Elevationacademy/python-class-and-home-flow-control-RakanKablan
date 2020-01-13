import random

class Card:
    def __init__(self, number, type):
        self.number = number
        self.type = type

    def show(self):
        print(f"{self.number} - {self.type}")


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for i in ["red", "blue", "green", "yellow"]:
            for j in range(1,11):
                self.cards.append(Card(i,j))

    def show(self):
        for i in self.cards:
            i.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1,0,-1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def deal(self):
        return self.cards.pop()

    def __iter__(self):
        return self

    def __next__(self):
        if self.cards:
            return self.cards.pop()
        else:
            raise StopIteration

    def iteration(self,i):
        if i > len(self.cards):
            i = len(self.cards)
        print("Cards which are popped during the iteration are:")
        while(i > 0):
            r = self.cards.pop()
            r.show()
            i -= 1

mydeck = Deck()
mydeck.shuffle()
card = mydeck.deal()
card.show()
for i in mydeck:
    i.show()
#mydeck.iteration(7)
print("check if empty")
mydeck.show()
