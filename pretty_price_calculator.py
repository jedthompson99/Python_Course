def pretty_price(gross_price, extension):
    if isinstance(extension, int):
        extension = extension * .01
    return int(gross_price) + extension


print(pretty_price(3.5, .95))
print(pretty_price(3.5, 95))
