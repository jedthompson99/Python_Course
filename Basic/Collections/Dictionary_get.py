teams = {
    'astros': ['Altuve', 'Correa', 'Bregman', 'Guy', 'Guy2'],
    'ss': 'George',
    'angels': ['trout', 'trujlos', 'stanton'],
}

# teams['red sox'] = ['price', 'bets']

# print(teams['red sox'])

# featured_team = teams['astros']

# featured_teams = teams['mets']

# featured_team = teams.get('dodgers', 'No featured team')

query = teams.get('ss', 'no featured team')

print(query)

# print(teams['mets', 'no featured_team'])
