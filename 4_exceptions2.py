# https://www.coursera.org/learn/diving-in-python/lecture/oF2h7/gienieratsiia-iskliuchienii
# Исключения 2

# Инструкция assert

assert True
# assert 1 == 0
# assert 1 == 0, "1 не равен 0"

def get_user_by_id(id):
    assert isinstance(id, int), "id должен быть целым числом"
    print("Выполняем поиск")



def tryis():
    # насколько дороги исключения
    my_dict = {"foo", 1}
    for _ in range(1000):
        try:
            my_dict["bar"]
        except KeyError:
            pass


get_user_by_id("foo")