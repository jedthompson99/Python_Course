class Invoice:
    
    def __init__(self, client, total):
        self.client=client
        self.total=total

    def formatter(self):
        return f'{self.client} owes: ${self.total}'

google = Invoice('Goodle', 100)
snapchat = Invoice("Snapchat", 200)

print(google.formatter())
print(snapchat.formatter())


# Starter code
class Garage:
  def __init__(self, size):
    self.size = size
    self.cars = ["Ram", "Model 3"]

  def open_door(self):
    return "The door opens"
    
home = Garage(2)
home.cars = []

get_cars = home.cars



