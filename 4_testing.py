#https://www.coursera.org/learn/diving-in-python/lecture/dxGwU/tiestirovaniie

import unittest

# Юниттесты
class TestPython(unittest.TestCase):
    def test_float_to_int_coercion(self):
        self.assertEqual(1, int(1.0))

    def test_get_empty_dict(self):
        self.assertIsNone({}.get('key'))

    def test_trueness(self):
        self.assertTrue(bool(10))


class TestDevision(unittest.TestCase):
    def test_integer_division(self):
        self.assertIs(10/5, 2)



# Тестируем астероидный класс
from asteroid import Asteroid
import json
from unittest.mock import patch


class TestAsteroid(unittest.TestCase):
    def setUp(self):
        self.asteroid = Asteroid(2029942)

    def mocked_get_data(self):
        with open('apophis_fixture.txt') as f:
            return json.loads(f.read())

    @patch('asteroid.Asteroid.get_data', mocked_get_data)
    def test_name(self):
        self.assertEqual(
            self.asteroid.name, '99942 Apophis (2004 MN4)'
        )

    @patch('asteroid.Asteroid.get_data', mocked_get_data)
    def test_diameter(self):
        self.assertEqual(self.asteroid.diameter, 682)
