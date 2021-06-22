# extend is used to add to an existing list. It changes the list.

tags = ['python', 'development', 'tutorials', 'code', 3, 4, 5, 6]

tags.extend(['jed', 'aaron', 'nobody'])

print(tags)

# without the ['jed'] brackets, it would add 'j', 'e', 'd' . . .


# If you want to add to a list without changing the initial list(make a new list),

new_tags = tags + ['programming']

print(new_tags)
