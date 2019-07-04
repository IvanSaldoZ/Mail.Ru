def first_decor(func):
    def wrapped():
        print('inside first')
        return func()
    return wrapped

def second_decor(func):
    def wrapped():
        print('inside second')
        return func()
    return wrapped


@first_decor
@second_decor
def decorated():
    print('Final....')

decorated()

# -----------------------------

def bold(func):
    def wrapped():
        return '<b>' + func() + '</b>'
    return wrapped


def italic(func):
    def wrapped():
        return '<i>' + func() + '</i>'
    return wrapped


@bold
@italic
def show():
    return "hello world!"

print(show())