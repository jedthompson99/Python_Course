post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

post = post + ('published',)

print(id(post))
print(id(post))

post += ('published',)

print(id(post))

# the ID is different because we have changed the tuple

# title, sub_heading, content, status = post

# print(title)
# print(sub_heading)
# print(content)
# print(status)