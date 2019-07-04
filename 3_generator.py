# https://www.coursera.org/learn/diving-in-python/lecture/3Ufax/gienieratory
def even_range(start, end):
    current = start
    while current < end:
        yield current
        current += 2

for number in even_range(1, 10):
    print(number)


print(list(even_range(1, 10)))
print('--------------')



# Числа Фибоначчи
def fibonacci(number):
    a = b = 1
    for _ in range(number):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)



# Аккумулятор
def accumulator():
    total = 0
    while True:
        value = yield total
        print('Got {}'.format(value))
        if not value: break
        total += value

generator = accumulator()
print('--------------')
print(next(generator))
print('Accumulated: {}'.format(generator.send(1)))
print('Accumulated: {}'.format(generator.send(1)))
print('Accumulated: {}'.format(generator.send(1)))
print('Accumulated: {}'.format(generator.send(1)))
print('Accumulated: {}'.format(generator.send(1)))