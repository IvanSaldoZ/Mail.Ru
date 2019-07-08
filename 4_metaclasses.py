# https://www.coursera.org/learn/diving-in-python/lecture/ED7oV/mietaklassy
# Метаклассы

class Class:
    ...

obj = Class()
print(type(obj))  # Тип obj - это Class
print(type(Class))   # А сам Class - это класс чего? это класс типа type - это метакласс, он создает другие классы
print(type(type))  # Рекурсивный просмотр, какого же типа сам type

print(issubclass(Class, type))  # type лишь создает класс, но Class не наследуется от type
print(issubclass(Class, object))  # При этом type - создает сам object, т.е. type - это базовый метакласс
print(issubclass(object, type))  # False, object - базовый класс, а type - базовый МЕТАкласс



# Как создаются классы

def dummy_factory():
    class Class:
        pass

    return Class

Dummy = dummy_factory()
print(Dummy() is Dummy())


# --------------------------------------------
# На самом деле, конечно, по-другому:
NewClass = type('NewClass', (), {})  # Создание класса с помощью метакласса type БЕЗ родителей и БЕЗ атрибутов
print(NewClass)
print(NewClass())



# --------------------------------------------
# На самом деле, конечно, всё сложнее:
class Meta(type):  # Наследуемс от type
    def __new__(cls, name, parents, attrs):
        print('Creating {}'.format(name))

        if 'class_id' not in attrs:
            attrs['class_id'] = name.lower()

        return super().__new__(cls, name, parents, attrs)

class A(metaclass=Meta):
    pass

# --------------------------------------------
class Meta2(type):

    '''
    def __init__(cls, name, bases, attrs):
        print('Initializing - {}'.format(name))

        if not hasattr(cls, 'registry'):
            cls.registry = {}
        else:
            cls.registry[name.lower()] = cls

        super.__init__(name, bases, attrs)
        '''
    pass

class Base(metaclass=Meta2): pass

class A2(Base): pass

class B2(Base): pass



# ----------------------------------
# Асбтрактные методы
from abc import ABCMeta,  abstractmethod

class Sender(metaclass=ABCMeta):
    @abstractmethod
    def send(self):
        '''Do smt
        Теперь дочерним классам обязательно нужно его определить, иначе ошибка
        '''


#class Child(Sender):
#   pass
#Child()  # Так нельзя, будет ошибка


class Child(Sender):
    def send(self):
        print('Sending')

print(Child())


# но лучше сделать проще:
class PythonWay:
    def send(self):
        raise NotImplementedError
