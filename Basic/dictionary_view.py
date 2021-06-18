players = {
    "ss": "Correa",
    "2b": ["Altuve", "jacob", "name"],
    "3b": "Bregman",
    "DH": "Gattis",
    "OF": "Springer",
}

# print(players.items())
# print(players.keys())
# print(players.values())

# print(list(players.values())[2])

# print(list(players.keys())[2])

# print(list(players.items())[3])

# Copy_Player_Dict_Values = list(players.copy().values())

# print(Copy_Player_Dict_Values)

Copy_Player_Dict_Values = list(players.copy().items())

print((Copy_Player_Dict_Values)[1][1][1])


# print(list(players.values())[3])

# player_names = list(players.copy().values())

# teams = {
#     "astros": ["Altuve", "Correa", "Bregman"],
#     "angels":  ["Trout", "Pujols"],
#     "yankees": ["Judge", "Stanton"],
#     "red sox": ["Price", "Betts"],
# }

# team_groupings = teams.items()

# """
# [
#   ('astros', ['Altuve', 'Correa', 'Bregman']),
#   ('angels', ['Trout', 'Pujols']),
#   ('yankees', ['Judge', 'Stanton']),
#   ('red sox', ['Price', 'Betts'])
# ]
# """

# print(list(team_groupings)[1][1][0])
