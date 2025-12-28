import unittest
from src.main.lab import count_digits

class TestCountDigits(unittest.TestCase):
    
    def test_positive_numbers(self):
        self.assertEqual(count_digits(123), 3)
        self.assertEqual(count_digits(456789), 6)
        
    def test_negative_numbers(self):
        self.assertEqual(count_digits(-987), 3)
        self.assertEqual(count_digits(-123456), 6)
        
    def test_single_digit_number(self):
        self.assertEqual(count_digits(0), 1)
        self.assertEqual(count_digits(7), 1)

if __name__ == '__main__':
    unittest.main()