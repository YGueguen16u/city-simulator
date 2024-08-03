# src/tests/test_helpers.py
import unittest
from src.utils.helpers import haversine_distance

class TestHaversineDistance(unittest.TestCase):
    def test_haversine_distance(self):
        # Known coordinates
        A = (45.75194444, 4.83305556)
        B = (45.76166667, 4.83388889)
        C = (45.76138889, 4.84777778)
        D = (45.75250000, 4.84750000)

        # Expected distances in kilometers
        expected_AB = 1.083
        expected_BC = 1.078
        expected_CD = 0.989
        expected_DA = 1.122

        # Calculated distances
        calculated_AB = haversine_distance(A, B) / 1000
        calculated_BC = haversine_distance(B, C) / 1000
        calculated_CD = haversine_distance(C, D) / 1000
        calculated_DA = haversine_distance(A, D) / 1000

        # Assertions with a tolerance for floating-point arithmetic
        self.assertAlmostEqual(calculated_AB, expected_AB, places=3)
        self.assertAlmostEqual(calculated_BC, expected_BC, places=3)
        self.assertAlmostEqual(calculated_CD, expected_CD, places=3)
        self.assertAlmostEqual(calculated_DA, expected_DA, places=3)

if __name__ == '__main__':
    unittest.main()
