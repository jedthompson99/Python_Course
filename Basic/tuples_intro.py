# List: []
# Dictionary: {}
# Tuple: ()

# Tuple: immutable 
# List: mutable

# if you were to use the .sort() fuction on the below, and it were a LIST, the order would change, and the 'mapping' would be different. BUT, fortunately, you can't sort a tuple.

post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# Tuple unpacking
title, sub_heading, content = post

# Equivalent to Tuple unpacking
# title = post[0]
# sub_heading = post[1]
# content = post[2]

print(title)
print(sub_heading)
print(content)