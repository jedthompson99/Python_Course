tags = [
    'python',
    'development',
    'tutorials',
    'code',
    'programming',
]

# slice_obj = slice()


print(tags[1:4:2])

slice_obj = slice(1, 4, 2)

print(slice_obj.start)
print(slice_obj.stop)
print(slice_obj.step)

print(tags[slice_obj])
