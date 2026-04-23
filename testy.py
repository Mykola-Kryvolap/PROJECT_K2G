import unittest
from kalkulator import calculate

class TestKalkulator(unittest.TestCase):
    def test_dodawanie(self):
        self.assertEqual(calculate("2+2"), 4)

    def test_odejmowanie(self):
        self.assertEqual(calculate("10-3"), 7)

    def test_mnozenie(self):
        self.assertEqual(calculate("3*4"), 12)

    def test_dzielenie(self):
        self.assertEqual(calculate("10/2"), 5.0)
