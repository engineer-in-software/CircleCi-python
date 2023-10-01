import unittest
from main import to_upper


class MyTestCase(unittest.TestCase):
    def test_to_upper(self):
        name = "small to capital"
        upper_name = to_upper(name)
        self.assertEqual(upper_name, "SMALL TO CAPITAL")


if __name__ == '__main__':
    unittest.main()