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
    def test_potega(self):
        self.assertEqual(calculate("2^3"), 8)

    def test_pierwiastek(self):
        self.assertEqual(calculate("math.sqrt(9)"), 3.0)

    def test_procent(self):
        self.assertEqual(calculate("50%"), 0.5)

    def test_procent_dodawanie(self):
        self.assertEqual(calculate("200+10%"), 220.0)

    def test_procent_odejmowanie(self):
        self.assertEqual(calculate("200-10%"), 180.0)

    def test_dzielenie_przez_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate("5/0")

    def test_nieprawidlowe(self):
        with self.assertRaises(ValueError):
            calculate("abc")

    def test_nawiasy(self):
        self.assertEqual(calculate("(2+3)*4"), 20)

if __name__ == "__main__":
    unittest.main()
