class Planet:
    '''Этот класс служит для описание планет'''

    count = 0

    def __new__(cls, *args, **kwargs):
        print('__new__ called')
        obj = super().__new__(cls)  # Делаем то же самое, что делает Python обычно при создании класса
        return obj


    def __init__(self, name, population=None):  # При инициализации
        print('__init__ called')
        self.name = name
        self.population = population
        Planet.count += 1



earth = Planet("Earth")
mars = Planet("Mars")
print(Planet.count)
print(mars.count)

print(earth.__dict__)

earth.mass = 5.97e24
print(earth.__dict__)
print(Planet.__dict__)

print(Planet.__doc__)
print(mars.__doc__)
print(dir(Planet))
print(earth.__class__)
