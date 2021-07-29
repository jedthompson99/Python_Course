# class Garage:
#       # Add your constructor here

#   def open_door(self):
#     return "The door opens"
    
# home = Garage() # instantiate with a garage size here


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



