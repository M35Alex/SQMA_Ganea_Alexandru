import unittest

class TestCase1(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(1 + 1, 2)

if __name__ == "__main__":
    unittest.main()
