# https://www.coursera.org/learn/diving-in-python/lecture/pJanf/nasliedovaniie-v-python
# Про наследование
import json


class ExportJSON:
    '''Класс для экспорта в JSON, mixin для класса собаки'''
    def to_json(self):
        return json.dumps(
            {
                "name": self.name,
                "breed": self.breed
            }
        )


class Pet:
    '''Класс "Животное"'''
    def __init__(self, name=None):
        self.name = name


class Dog(Pet):
    """Класс собаки, как подкатегории Животного"""
    def __init__(self, name, breed=None):
        super().__init__(name)  # Вызываем метод инит родительского класса специально
        self.breed = breed  # Ну и ещё добавляем дочернему классу породу собаки

    def say(self):
        return "{0}: waw".format(self.name)


dog = Dog("Шарик", "Доберман")
print(dog.name)
print(dog.say())


# Расширяем класс Dog классом ExportJSON для сохранения данных в JSON
class ExDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        # Вызов метода по MRO
        super().__init__(name, breed)
        # super(ExDog, self).__init__(name)


dog = ExDog("Белка", breed="Дворняга")
print(dog.to_json())


# ----------------------------
# Определяем наследуется ли класс от определенного объекта / класса (все наследуются от объекта в Питоне)
print(issubclass(int, object))
print(issubclass(Dog, object))
print(issubclass(Dog, Pet))
print(issubclass(Dog, int))

# Определяем является ли объект экземпляром класса
print(isinstance(dog, Dog))
print(isinstance(dog, Pet))
print(isinstance(dog, object))


# ----------------------------
# Порядок поиска атрибутов и методов объекта, линеаризация класса
print(ExDog.__mro__)


# ----------------------------
# Использование super, нарушение MRO
class WoolenDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        # Явное указание метода конкретного класса
        super(Dog, self).__init__(name)
        self.breed = "Шерстяная собака породы {0}".format(breed)

dog = WoolenDog("Жучка", breed="Такса")
print(dog.breed)
print(dog.name)

# --------------------------------

class PrivDog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.__breed = breed

    def say(self):
        return "{0}: waw!".format(self.name)

    def get_breed(self):
        return self.__breed


class ExPrivDog(PrivDog, ExportJSON):
    def get_breed(self):
        # Получаем закрытый атрибут родителя __breed добавлением перед ним префикса названия класса-родителя
        return "порода: {0} - {1}".format(self.name, self._PrivDog__breed)


dog = ExPrivDog("Тузик", "Питбуль")
print(dog.get_breed())
print(dog.__dict__)