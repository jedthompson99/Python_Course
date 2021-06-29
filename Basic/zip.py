positions = ['2b', '3b', 'ss', 'dh']
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

scoreboard = zip(positions, players)

print(list(scoreboard))


#if you don't convert to a list, this returns a "zip object with a random number string"
# <zip object at 0x104b657c0>
