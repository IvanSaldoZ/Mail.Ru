# SINGLETON
class Singleton:
    instance = None

    def __new__(cls):  # При создании объекта
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

a = Singleton()
b = Singleton()

print(a is b)

# ---------------------------------------------
# HASH
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __hash__(self):
        return hash(self.email)

    def __eq__(self, obj):
        return self.email == obj.email

jane = User("Jane Doe", "jdoe@mail.ru")
joe = User("Joe Doe", "jdoe@mail.ru")

print(jane == joe)

print(hash(jane))
print(hash(joe))

user_email_map = {user: user.name for user in [jane, joe]}

print(user_email_map)

# ---------------------------------------------
