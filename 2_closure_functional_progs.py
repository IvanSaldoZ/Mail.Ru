# https://www.coursera.org/learn/diving-in-python/lecture/BadUu/funktsional-noie-proghrammirovaniie



def get_multiplier():
    def inner(a, b):
        return a * b
    return inner


mult = get_multiplier()
print(mult(10, 11))

print(mult.__name__)


# Замыкание
def get_multiplier(number):
    def inner(a):
        return a * number
    return inner

mult2 = get_multiplier(3)
print(mult2)
print(mult2(10))




# Функциональное программирование
def squar(a):
    return a**2
print(list(map(squar, range(10))))

def positive_hey(a):
    return a > 2
print(list(filter(positive_hey, range(10))))



# Lambda Fuctions
print(list(map(lambda x: x**2, range(10))))


print(list(filter(bool, range(3))))
print([x for x in range(3) if x])

print(list(zip(
  filter(bool, range(3)),
  [x**2 for x in range(3)]
)))