print(int)
print(dict)
num = 13
print(type(num))
print(isinstance(num, int))
print(isinstance(num, float))

class Human:
    pass

class Robot:
    '''Класс, который пока ничего не делает'''

print(Robot)
print(dir(Robot)) # Какие есть методы?



class Planet:

    count = 0

    def __init__(self, name):  # При инициализации
        self.name = name

    def __str__(self): # При попытке вызвать метод print
        return self.name

    def __repr__(self):  # Внутреннее представление (даже внутри списков)
        return self.name


earth = Planet("Earth")

print(earth.name)
print(earth)


solar_sytem = []

planet_names = [
    'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune',
]

for name in planet_names:
    planet = Planet(name)
    solar_sytem.append(planet)

print(solar_sytem)