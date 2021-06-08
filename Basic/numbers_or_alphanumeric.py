api_data = '5'
greeting = 'Hi there'

# all elements have to be alphanumeric... spaces will cause it to reutrn "false," even if other characters are letters

print(api_data.isalpha())
print(greeting.isalpha())

print(api_data.isnumeric())
print(greeting.isnumeric())
