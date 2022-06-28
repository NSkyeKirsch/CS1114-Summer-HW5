import random

class Bleh:
    def __init__(self, name):
        self.name = name
        self.num = random.randint(1, 3)

    def __str__(self):
        return self.name

    def get_num(self):
        return self.num


lst = []
dino = ['cat', 'dog', '1', 'epic', 'meow', 'small']

for i in range(5):
    new_bleh = Bleh(dino[i])
    lst.append(str(new_bleh))

if 'meow' in lst:
    print(lst)
