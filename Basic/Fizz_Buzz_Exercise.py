def FizBuzz(x):
    list = range(1, x+1)
    for number in list:
        if (number % 3 == 0) and (number % 5 == 0):
            print('FizzBuzz')
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
FizBuzz(35)