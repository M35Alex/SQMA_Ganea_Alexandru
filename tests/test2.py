import unittest

class TestCase2(unittest.TestCase):
    def test_example2(self):
        self.assertEqual(2 * 2, 4)

if __name__ == "__main__":
    unittest.main()
