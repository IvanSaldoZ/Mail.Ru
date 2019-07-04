# https://www.coursera.org/learn/diving-in-python/lecture/urODp/primier-na-klassy
import pprint
import requests


class WeatherService:
    '''Класс для работы с погодным сервисом'''

    def __init__(self):
        self._city_cache = {}  # Кэш погоды в конкретном городе

    def get_today_temp(self, city):
        '''Получаем погоду для конкретного города'''
        if city in self._city_cache:
            print("Retrieving data from cache....")
            return self._city_cache[city]

        app_id = ""
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(city, app_id)
        print("Retrieving data from Weather Service....")
        data = requests.get(url).json()
        temp_cel = data["main"]["temp"]
        self._city_cache[city] = temp_cel  # Сохраняем в кэш полученное значение погоды
        return temp_cel


class CityInfo:
    '''Класс для получения погоды конкретного города'''
    def __init__(self, city, temp=None):
        self.city = city
        self._temp = temp or WeatherService()

    def weather_forecast(self):
        '''Получение температуры в конкретном городе'''
        return self._temp.get_today_temp(self.city)


def _main():
    '''Основная функция приложения'''
    temp_class = WeatherService()
    for i in range(5):
        city_info = CityInfo("Moscow", temp=temp_class)
        forecast = city_info.weather_forecast()
        pprint.pprint(forecast)


if __name__ == '__main__':
    '''Основное содержание приложения'''
    _main()
