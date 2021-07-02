# def greeting(name = 'Guest'):
#   print(f'Hi {name}!')

# greeting()
# greeting('Kristine')

# Nope
def some_function(collection = []):
  collection.append(1)
  print(id(collection))
  return collection


print(some_function())
print(some_function())

def counter(initial_count=0):
    return initial_count + 1
print(counter(5))