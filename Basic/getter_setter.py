class Invoice:
    
    def __init__(self, client, total):
        self.client = client
        self.total = total

    def formatter(self):
        return f'{self.client} owes: ${self.total}'


google = Invoice('Google', 100)

print(google.client)

google.client = 'Yahoo'

print(google.client)


#  coding exercise

class Garage:
    def __init__(self, size, cars):
    self.size = size
    self.cars = ["Ram", "Model 3"]

  def open_door(self):
    return "The door opens"
    
home = Garage(2)
# End of starter code

# Setter goes here

get_cars = # Getter goes here