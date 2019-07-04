'''

def stringify(func):
  return str(func)


@stringify
def multiply(a, b):
  return a * b
'''


def logger(func):
    def wrapper(num_list):
        result = func(num_list)
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