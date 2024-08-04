# src/tests/test_city.py

import unittest
from datetime import datetime, timedelta
from src.simulation.city import City
from src.simulation.person import Person


class TestCity(unittest.TestCase):

    def setUp(self):
        """Set up test variables"""
        self.city = City(id=1, population=0, coordinates_area=[
            (45.75194444, 4.83305556),
            (45.76166667, 4.83388889),
            (45.76138889, 4.84777778),
            (45.75250000, 4.84750000)
        ], gdp=0)

    def test_initialization(self):
        """Test if the city is initialized correctly"""
        self.assertEqual(self.city.id, 1)
        self.assertEqual(self.city.population, 0)
        self.assertEqual(len(self.city.coordinates_area), 4)
        self.assertEqual(self.city.gdp, 0)
        self.assertEqual(self.city.area, 0)
        self.assertEqual(len(self.city.inhabitants_list), 0)
        self.assertEqual(len(self.city.building_list), 0)

    def test_compute_area(self):
        """Test the computation of the city area"""
        area = self.city.compute_area()
        expected_area_m2 = 1.13931020  # Expected area in square kilometers
        self.assertAlmostEqual(area, expected_area_m2, places=2)

    def test_add_inhabitants(self):
        """Test adding new inhabitants to the city"""
        initial_population = self.city.population
        self.city.new_inhabitants(10)
        self.assertEqual(self.city.population, initial_population + 10)
        self.assertEqual(len(self.city.inhabitants_list), 10)

    def test_string_representation(self):
        """Test the string representation of the city"""
        self.city.new_inhabitants(10)
        self.city.compute_area()
        city_str = str(self.city)
        self.assertIn("1", city_str)
        self.assertIn("10", city_str)
        self.assertIn(str(self.city.area), city_str)
        self.assertIn(str(self.city.gdp), city_str)


if __name__ == "__main__":
    unittest.main()
