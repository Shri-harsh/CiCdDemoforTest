import unittest 
from calculator import add, multi

class TestCalculator (unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3), 5)

    def test_multi(self):
        self.assertEqual (multi(4,5), 0)
if __name__ =='__main__':
    unittest.main()

