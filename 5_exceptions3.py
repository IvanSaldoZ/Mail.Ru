# https://www.coursera.org/learn/diving-in-python/lecture/OIlRg/iskliuchieniia-v-requests-primier
import requests
#print(requests.__file__)  # Где находится файл
import sys
url = sys.argv[1]

try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
except requests.Timeout:
    print("Слишком долго ждали", url)
except requests.HTTPError as err:
    code = err.response.status_code
    print("Ошибка url: {0}, code {1}".format(url, code))
except requests.RequestException:
    print("Ошибка скачивания url: ", url)
else:
    print(response.content)
