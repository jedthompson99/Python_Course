players = {
    "ss": "Correa",
    "2b": ["Altuve", "jacob", "name"],
    "3b": "Bregman",
    "DH": "Gattis",
    "OF": "Springer",
}

# Dictionary View Objects - returns tuples, which cannot be searched using index numbers, etc.


#using print statements
# print(players.items())
# print(players.keys())
# print(players.values())

#storing as new variables, and then printing
# list_keys = players.keys()
# print(list_keys)

# list_values = players.values()
# print(list_values)

# list_items = players.items()
# print(list_items)


#converting to lists and storing in variables, and printing

# list_players_values = list(players.values())
# print(list_players_values)

# list_players_keys = list(players.keys())
# print(list_players_keys)

# list_players_items = list(players.items())
# print(list_players_items)


# INDEX NUMBERS FROM CONVERTED LISTS

# print(list(players.values())[2])

# print(list(players.keys())[2])

# print(list(players.items())[1][2])


# MAKE A COPY - MAKES ANOTHER THREAD

# Copy_Player_Dict_Values = list(players.copy().values())
# print(Copy_Player_Dict_Values[4])

# Copy_Player_Dict_Keys = list(players.copy().keys())
# print(Copy_Player_Dict_Keys[4])

# Copy_Player_Dict_Items = list(players.copy().items())
# print(Copy_Player_Dict_Items[3])


teams = {
    "astros": ["Altuve", "Correa", "Bregman"],
    "angels":  ["Trout", "Pujols"],
    "yankees": ["Judge", "Stanton"],
    "red sox": ["Price", "Betts"],
}

# team_groupings = teams.items()
# print(team_groupings)

# """
# [
#   ('astros', ['Altuve', 'Correa', 'Bregman']),
#   ('angels', ['Trout', 'Pujols']),
#   ('yankees', ['Judge', 'Stanton']),
#   ('red sox', ['Price', 'Betts'])
# ]

# """

# print(list(team_groupings)[1][1])

