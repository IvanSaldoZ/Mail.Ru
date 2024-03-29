# https://www.coursera.org/learn/diving-in-python/lecture/wAe6e/itieratory
# Свой итератор
class SquareIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration

        result = self.current ** 2
        self.current += 1
        return result

for num in SquareIterator(1,4):
    print(num)


# Другой вариант написания итератора
class IndexIterable:
    def __init__(self, obj):
        self.obj = obj

    def __getitem__(self, index):
        return self.obj[index]

for letter in IndexIterable('str'):
    print(letter)