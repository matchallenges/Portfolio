class Orange:
    print("Orange created!")

    def __init__(self, weight, color):
        self.weight=weight
        self.color=color

orange=Orange(10, 'purple')


print(orange.weight)
print(orange.color)