import functools

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('3_res_file.txt', 'w') as f:
            f.write(str(result))

        return result
    return wrapper

@logger
def summator(num_list):
    return sum(num_list)


print(summator([1,2,3,4,5]))

with open('3_res_file.txt', 'r') as f:
    print(f.read())

print(summator.__name__)