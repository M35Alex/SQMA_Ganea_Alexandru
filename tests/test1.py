import unittest

class TestCase1(unittest.TestCase):
    def test_example1(self):
        print("test 1")
        self.assertEqual(1 + 1, 2)

if __name__ == "__main__":
    unittest.main()
