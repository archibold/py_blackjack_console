import random

user_card = []
computer_card = []


def print_summary():
    """ Print summary of actual status of game """
    print(f"Your cards {user_card} and this is: {sum(user_card)}")
    print(f"Computer cards {computer_card} and this is: {sum(computer_card)}")


def print_winner(player):
    """ function is printing winner of the game"""
    if player == 'USER':
        print('YOU WIN')
    else:
        print('YOU LOSE')


def init_game():
    """ beginning initialisation of the game"""
    for _ in range(2):
        user_card.append(draw_card())
    computer_card.append(draw_card())
    print_summary()
    if sum(user_card) == 21:
        return 'USER'


def draw_card():
    """ drawing card from deck of card
        [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    """
    return random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])


def user_turn():
    user_card.append(draw_card())
    if sum(user_card) == 21:
        return 'USER'
    elif sum(user_card) > 21:
        return 'COMPUTER'
    return None


def computer_turn():
    computer_card.append((draw_card()))
    if sum(computer_card) == 21 or sum(computer_card) == sum(user_card):
        return 'COMPUTER'
    elif sum(computer_card) > 21:
        return 'USER'
    elif sum(computer_card) > sum(user_card):
        return 'COMPUTER'
    return None


def game():
    decision = 'H'
    winner = init_game()

    while not winner and decision == 'H':
        decision = input(f'"H" for hit or something else for pass: ').capitalize()
        if decision == 'H':
            winner = user_turn()
            print_summary()

    while not winner:
        winner = computer_turn()
        print_summary()
    print_winner(winner)


game()
