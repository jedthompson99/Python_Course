# start, stop, step can be used in a range, but there is also a slice() function. It's like a knife you can then apply to any list.

tags = ['python', 'development', 'tutorials',
        'code', 'programming', 'computer science']


# tag_range = tags[1:-1:2]

# print(tag_range)


tag_range2 = slice(2, 6, 2)

print(tag_range2)
print(tag_range2.start)
print(tag_range2.stop)
print(tag_range2.step)

print(tags[tag_range2])
