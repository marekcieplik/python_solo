import unittest
import Functional_Programming as f_P


class MyTestCase(unittest.TestCase):
    def test_multiple(self):
        self.assertEqual(f_P.multiple(2), 4)  # add assertion here

    def test_multiple_twice(self):
        self.assertEqual((f_P.multiple_twice(fp.multiple, 2)), 64)


if __name__ == '__main__':
    unittest.main()
