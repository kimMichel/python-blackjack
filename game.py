import random

class Game:
    def getRandomCards(self, cards):
        return [random.choice(cards) for _ in range(2)]

    def getCard(self, cards):
        return random.choice(cards)