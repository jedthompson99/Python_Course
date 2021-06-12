import random


def play():
    user = input("Input Rock (R), Paper (P), or Scissors (S)")
    computer = random.choice(['R', 'P', 'S'])

    if user == computer:
        return "It\'s a tie!!"

    if is_win(user, computer):
        return 'You Won!'

    return 'You Lost!'


def is_win(player, opponent):
    if (player == 'R' and opponent == 'S') or (player == 'P' and opponent == 'R') or (player == 'S' and opponent == 'P'):
        return True
