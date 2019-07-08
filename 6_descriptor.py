# https://www.coursera.org/lecture/diving-in-python/dieskriptory-3QrPI
class Descriptor:
    def __get__(self, instance, owner):
        print('get')

    def __set__(self, instance, value):
        print('set')

    def __delete__(self, instance):
        print('delete')

class Class:
    attr = Descriptor()

instance = Class()


instance.attr

instance.attr = 10

del instance.attr

# ------------------------------

class Value:
    def __init__(self):
        self.value = None

    @staticmethod
    def _prepare_value(value):
        return value * 10

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = self._prepare_value(value)

class Class2:
    attr = Value()

instance = Class2()
instance.attr = 10

# Выведится не 10, а 100
print(instance.attr)


# ------------------------------

class ImportantValue:
    def __init__(self, amount):
        self.amount = amount

    def __get__(self, instance, owner):
        return self.amount

    def __set__(self, instance, value):
        with open('log.txt', 'a') as f:
            f.write(str(value))
        self.amount = value


class Account:
    amount = ImportantValue(100)


bobs_account = Account()
bobs_account.amount = 200

with open('log.txt') as f:
    print(f.read())



# ------------------------------
# На самом деле функция в Python - это дискриптор

class Class3:
    def method(self):
        pass

obj = Class3()

print(obj.method)
print(Class3.method)  # Дескриптор переопределяет поведение метода, если он был вызван прямо через класс, а не объект


# ------------------------------
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


amy = User('Amy', 'Jones')

print(amy.full_name)  # Здесь возвращается как и нужно
print(User.full_name)  # А здесь - объект propery (т.е. дескриптор переопределил поведение)


# ------------------------------
# Вот как реализован property-декоратор внутри Python
class Property:
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, instance, owner=None):
        if instance is None:
            return self

        return self.getter(instance)

class Class4:
    @property
    def original(self):
        return 'original'

    @Property
    def custom_sugar(self):
        return 'custom sugar'

    def custom_pure(self):
        return 'custom pure'

    custom_pure = Property(custom_pure)

obj = Class4()
print(obj.original)
print(obj.custom_sugar)
print(obj.custom_pure)



# ------------------------------
# Вот как реализован static и класс декораторы внутри Python
class StaticMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner=None):
        return self.func

class ClassMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner=None):
        if owner is None:
            owner = type(instance)

        def new_func(*args, **kwargs):
            return self.func(owner, *args, **kwargs)

        return new_func



# ------------------------------
# slots - жестко задает атрибуты в классе (без вомзожности их последующего изменения)
class Class5:
    __slots__ = ['anakin']

    def __init__(self):
        self.anakin = 'the chosen one'

obj = Class5()
#obj.luke = 'the chosen too'  # ERROR! Мы задали ещё один атрибут, что недопустимо
