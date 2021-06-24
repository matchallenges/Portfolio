class Fruit:
    def __init__(self, weight, colour, orange_type):
        self.weight = weight
        self.colour = colour
        self.orange_type = orange_type

class Orange(Fruit):   
    def peel(self):
        return self.weight + 100
    

my_orange = Orange(50, 'orange', 'navel')

print(my_orange.peel())