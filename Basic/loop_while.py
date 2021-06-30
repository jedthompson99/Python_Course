# nums = list(range(1, 100))

# while len(nums) > 0:
#   print(nums.pop())

# def guessing_game():
#   while True:
#     print('What is your guess?')
#     guess = input()

#     if guess == '42':
#       print('You correctly guessed it!')
#       return False
#     else:
#       print(f"No, {guess} isn't the answer, please try again\n")

# guessing_game()


# CODING EXERCISE

def loop_using_while():

    doghouse = ['red', 'pat', 'rover', 'sushi']
    iterator_value = 0
    while iterator_value < 4:
        print(doghouse[iterator_value])
        iterator_value += 1
    return [doghouse,iterator_value]

loop_using_while()