import unittest
import Functional_Programming as fp

class MyTestCase(unittest.TestCase):
    def test_multiple(self):
        self.assertEqual(fp.multiple(2), 4)  # add assertion here
    def test_multiple_twice(self):
        self.assertEqual((fp.multiple_twice(fp.multiple, 2)), 64)


if __name__ == '__main__':
    unittest.main()
