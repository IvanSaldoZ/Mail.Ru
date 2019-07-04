# https://www.coursera.org/learn/diving-in-python/lecture/jBkB6/mietody-chast-2
class Human:

    def __init__(self, name, age=0):
        self._name = name
        self._age = age


    @staticmethod               # Если не оперирует ни экземпляром класса ни его методами
    def is_age_valid(age):
        return 0 < age < 150


bob = Human("Bob")
print(Human.is_age_valid(50))
print(bob.is_age_valid(250))


class Robot:

    def __init__(self, power):
        self.power = power

    def set_power(self, power):
        if power < 0:
            self.power = 0
        else:
            self.power = power

wall_e = Robot(100)
wall_e.power = 200
print(wall_e.power)

wall_e.power = -20

wall_e.set_power(-20)
print(wall_e.power)



class RobotProp:

    def __init__(self, power):
        self._power = power  # Реальная мощность теперь скрыта от внешнего влияния

    power = property()  # Атрибут power оставляем таким же, но переобозначаем как свойство

    @power.setter
    def power(self, value):  # Переопределяем поведение при указании значения power-свойства
        self._power = value if value > 0 else 0

    @power.getter
    def power(self):
        return self._power

    @power.deleter
    def power(self):
        print("Make Robot useless")
        del self._power


wall_e2 = RobotProp(100)
wall_e2.power = 200
print(wall_e2.power)

wall_e2.power = -20
print(wall_e2.power)


# ------------------------------------------------
class RobotShort:

    def __init__(self, power):
        self._power = power  # Реальная мощность теперь скрыта от внешнего влияния

    @property
    def power(self):  # Переопределяем поведение при взаимодействии со свойством
        # Здесь могут идти полезные действия
        return self._power



wall_e3 = RobotShort(100)
print(wall_e3.power)
