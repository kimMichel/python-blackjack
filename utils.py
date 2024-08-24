import random

def getRandomCards(cards):
    return [random.choice(cards) for _ in range(2)]

def getCard(cards):
    return random.choice(cards)