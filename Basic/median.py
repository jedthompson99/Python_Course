"""
Tools: 
- math library
- sorted function
- list slicing
- computations

"""
# import math


# sale_prices = [
#     100,
#     83,
#     220,
#     40,
#     100,
#     400,
#     10,
#     1,
#     3
# ]

# sorted_sale_prices = sorted(sale_prices)

# print(sorted_sale_prices)

# length_sale_prices = len(sale_prices)

# print(length_sale_prices)

# half_prices = length_sale_prices // 2

# print(half_prices)

# median_number = half_prices + 1

# print(median_number)

median_number = sorted_sale_prices[half_prices]

print(median_number)

"""
"""
Tools:
- math library
- sorted function
- list slicing
- computations


sale_prices = [
    100,
    83,
    220,
    40,
    100,
    400,
    10,
    1,
    3
]

sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)
half_slice = math.floor(num_of_sales/2)
first_sales_items = sorted_list[:half_slice]
last_sales_items = sorted_list[-(half_slice):]
median = sorted_list[half_slice:(half_slice + 1)]

print(sorted_list)
print(num_of_sales)
print(first_sales_items)
print(last_sales_items)
print(median)
