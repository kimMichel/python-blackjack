import utils

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print("Welcome to Blackjack!")

computer_cards = utils.getRandomCards(cards)
player_cards = utils.getRandomCards(cards)

print(f'Computer cards [*, {computer_cards[1]}]')

while True:
    print(f'Your cards {player_cards}')
    choose = input('Do you want to "hit" or "stand": ')

    if choose == 'stand':
        break
    
    if choose == 'hit':
        player_cards.append(utils.getCard(cards))

    if sum(player_cards) > 21:
        print(player_cards)
        print('You loose!')
        break

    if sum(player_cards) == 21:
        print(player_cards)
        print('You win!')
        break


if sum(player_cards) < sum(computer_cards):
    print(f'Computer cards: {computer_cards}')
    print(f'Your cards: {player_cards}')
    print('You loose!')
elif sum(player_cards) == sum(computer_cards):
    print(f'Computer cards: {computer_cards}')
    print(f'Your cards: {player_cards}')
    print('Its draw!')
elif sum(player_cards) > sum(computer_cards):
    print(f'Computer cards: {computer_cards}')
    print(f'Your cards: {player_cards}')
    print('You win!')
