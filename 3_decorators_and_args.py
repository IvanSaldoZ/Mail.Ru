
def logger(filename):
    def decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'w') as f:
                f.write(str(result))
            return result
        return wrapped
    return decorator


@logger('3_decor.txt')
def summator(num_list):
    return sum(num_list)

# the same:
summator = logger('3_decor2.txt')(summator)
print(summator.__name__)


print(summator([1,2,3,4,5,6]))

