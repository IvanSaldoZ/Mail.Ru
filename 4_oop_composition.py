# https://www.coursera.org/learn/diving-in-python/lecture/Zdqzy/kompozitsiia-klassov-primier
# Композиция вместо наследования
import json

class PetExport:
    '''Общий интерфейс для экспорта информации о питомце'''
    def export(self):
        raise NotImplementedError


class ExportJSON(PetExport):
    '''Реализация интерфейса для экспорта информации о питомце в JSON'''
    def export(self, dog):
        return json.dumps( {
            "name": dog.name,
            "breed": dog.breed,
        })


class ExportXML(PetExport):
    '''Реализация интерфейса для экспорта информации о питомце в XML'''
    def export(self, dog):
        return """<?xml version="1.0" encoding="utf-8"?>
                    <dog>
                        <name>{0}</name>        
                        <breed>{1}</breed>        
                    </dog>
        """.format(dog.name, dog.breed)


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


class ExDog(Dog):
    """Собака, которая использует композицию, а не миксин по наследованию"""
    def __init__(self, name, breed=None, exporter=None):  # Экспортер задаем при инициализации ExDog
        super().__init__(name, breed=breed)  # Не забываем про инициализации дочернего элемента
        self._exporter = exporter or ExportJSON  # По умолчанию передаем в экспортер JSON
        # Проверяем, инстанс не соответствует нашему интерфейсу экспортера
        if not isinstance(self._exporter, PetExport):
            raise ValueError

    def export(self):
        return self._exporter.export(self)


dog = ExDog("Шарик", "Дворняга", exporter=ExportXML())
print(dog.export())

dog2 = ExDog("Тузик", "Мопс", exporter=ExportJSON())
print(dog2.export())