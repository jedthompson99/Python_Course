# def greeting(first, last):
#   def full_name():
#     return f'{first} {last}'

#   print(f'Hi {full_name()}!')


# greeting('Kristine', 'Hudgens')


#CODING EXERCISE

def greeting(name):
    def persons_name():
        return f'{name}'
    
    return(f'Hello, {persons_name()}')

greeting('Jordan')