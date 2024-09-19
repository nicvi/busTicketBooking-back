import unittest
from unittest.mock import MagicMock

from core.src.use_cases.get_cities import GetCities


class TestGetCities(unittest.TestCase):
    def setUp(self):
        self.mock_city_repository = MagicMock()
        self.get_cities = GetCities(city_repository=self.mock_city_repository)

    def test_execute(self):
        expected_cities = ['New York', 'Los Angeles', 'Chicago']
        self.mock_city_repository.get_available_cities.return_value = expected_cities

        result = self.get_cities.execute()

        self.mock_city_repository.get_available_cities.assert_called_once()
        self.assertEqual(result, expected_cities)

if __name__ == '__main__':
    unittest.main()
