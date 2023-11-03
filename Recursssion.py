from random import choice

CARD_NUMBER = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
CARD_SUIT = ["H", "D", "S", "C"]

random_card_number = choice(CARD_NUMBER)
random_card_suit = choice(CARD_SUIT)

print('Welcome to the game, random player!')
print('I generate a random card, you guess the color of its suit')


def play_game():

    player_answer = input('Guess the color: red or black:  ')

    if not player_answer.lower() in ['red', 'black']:
        print('Are you kidding me? Red or Black only!!! ')
        play_game()
    elif player_answer.lower() == 'red' and random_card_suit in ['H', 'D']:
        print('Correct! the generated  card was ' + random_card_number + random_card_suit)
        play_game()
    elif player_answer.lower() == 'black' and random_card_suit in ['S', 'C']:
        print('Correct! the generated  card was ' + random_card_number + random_card_suit)
        play_game()
    else:
        print('Incorrect! the generated  card was ' + random_card_number + random_card_suit)
        play_game()


play_game()
