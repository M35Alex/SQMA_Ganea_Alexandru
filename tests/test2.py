import unittest

class TestCase2(unittest.TestCase):
    def test_example2(self):
        print("test 1")
        self.assertEqual(2 * 2, 4)

if __name__ == "__main__":
    unittest.main()
