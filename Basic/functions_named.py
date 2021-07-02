# def full_name(first, last):
#   print(f'{first} {last}')


# full_name('Kristine', 'Hudgens')
# full_name(first = 'Kristine', last = 'Hudgens')
# full_name(last = 'Hudgens', first = 'Kristine')

def named_arguments_practice(sequence):
    sequence(first, fifth, fourth, third, second)

print(named_arguments_practice(first=1, second=2, third =3, forth=4, fifth=5))