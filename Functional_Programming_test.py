import unittest
import Functional_Programming as f_P


class MyTestCase(unittest.TestCase):
    def test_power(self):
        self.assertEqual(f_P.power(2), 4)  # def power(x) -> x * x

    def test_double_(self):
        self.assertEqual((f_P.double_(f_P.power, 2)), 8)  # def double_(func, arg) -> 2 * func(arg)


if __name__ == '__main__':
    unittest.main()
