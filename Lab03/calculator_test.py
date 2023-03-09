from unittest import TestCase
from calculator import Calculator


class ApplicationTest(TestCase):

    def test_add(self):
        valid_params = {(0, 1): 1, (1, 2): 3, (0, -1): -1, (-1, -2): -3, (1, -1): 0}
        for key, value in valid_params.items():
            with self.subTest():
                self.assertEqual(Calculator.add(key[0], key[1]), value)
        self.assertRaises(TypeError, Calculator.add, 1, "")

    def test_divide(self):
        valid_params = {(0, 1): 0, (2, 1): 2, (3, 2): 1.5, (4, -1): -4, (0, -1): 0}
        for key, value in valid_params.items():
            with self.subTest():
                self.assertEqual(Calculator.divide(key[0], key[1]), value)
        self.assertRaises(ZeroDivisionError, Calculator.divide, 1, 0)

    def test_sqrt(self):
        valid_params = {0: 0, 1: 1, 4: 2, 121: 11, 169: 13}
        for key, value in valid_params.items():
            with self.subTest():
                self.assertEqual(Calculator.sqrt(key), value)
        self.assertRaises(ValueError, Calculator.sqrt, -1)

    def test_exp(self):
        valid_params = {0: 1, 1: 2.718281828459045, 2: 7.38905609893065,
                        -1: 0.36787944117144233, -2: 0.1353352832366127}
        for key, value in valid_params.items():
            with self.subTest():
                self.assertEqual(Calculator.exp(key), value)
        self.assertRaises(OverflowError, Calculator.exp, 1000)
