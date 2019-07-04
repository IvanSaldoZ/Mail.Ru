# https://www.coursera.org/learn/diving-in-python/lecture/zFsUc/mietody-chast-1
class Human:

    def __init__(self, name, age=0):
        self._name = name
        self._age = age

    def _say(self, text):
        print(text)

    def say_name(self):
        self._say(f"Hello, I am {self._name}")

    def how_old(self):
        self._say(f"I am {self._age} years old")




class Planet:

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []

    def add_human(self, human):
        print(f"Welcome to {self.name}, {human._name}!")
        self.population.append(human)


mars = Planet("Mars")
bob = Human("Bob")
mars.add_human(bob)



Norman = Human("Norman", 29)
Norman.say_name()
Norman.how_old()


#------------------------------
def extract_description(user_string):
    return "Чемпионат мира по футболу"

def extract_date(user_string):
    return date(2018, 6, 14)


class Event:

    def __init__(self, description, event_date):
        self.description = description
        self.date = event_date

    def __str__(self):
        return f"Event \"{self.description}\" at {self.date}"

    @classmethod                       # classmethd - это метод класса, а не экземпляра
    def from_string(cls, user_input):  # Принимает не не экземпляр класса, а сам класс
        description = extract_description(user_input)
        date = extract_date(user_input)
        return cls(description, date)   # И вот теперь мы инициализируем класс и возвращаем экземпляр класса

from datetime import date
event_description = "Международная летняя школа"
event_date = date.today()

event = Event(event_description, event_date)
print(event)

event = Event.from_string("Добавить в мой календарь открытие чемпионата мира по футболу 14 июня 2018 года")
print(event)