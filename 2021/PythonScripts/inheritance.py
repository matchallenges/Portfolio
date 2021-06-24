class Adult():
    def __init__(self, name, height, weight, eye_color):
        self.name = name
        self.height = height
        self.weight = weight
        self.eye_color = eye_color

    def print_name(self):
        print(self.name)

class Kid(Adult):
    def add(self, x, y):
        return x + y
        



adult_1 = Adult('Mathieu', 6, 150, 'brown') 

print(adult_1.eye_color)

kid_1 = Kid('Kelly', 6, 150, 'brown')

print(kid_1.add(1, 2))
print(kid_1.height)