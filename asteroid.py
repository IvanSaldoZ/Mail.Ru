#https://www.coursera.org/learn/diving-in-python/lecture/dxGwU/tiestirovaniie

import requests

class Asteroid:
    API_KEY = 'NFji3u8VfjUeVZqhhXFYCPxkiVdgMcNEGg1uWi8T'
    BASE_API_URL = 'https://api.nasa.gov/neo/rest/v1/neo/{}?api_key='+API_KEY

    def __init__(self, spk_id):
        self.api_url = self.BASE_API_URL.format(spk_id)

    def get_data(self):
        return requests.get(self.api_url).json()

    @property
    def name(self):
        return self.get_data()['name']

    @property
    def diameter(self):
        return int(self.get_data()['estimated_diameter']['meters']['estimated_diameter_max'])




apophis = Asteroid(2099942)
print(f'Name: {apophis.name}')
print(f'Diameter: {apophis.diameter}m')
