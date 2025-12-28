import unittest
from src.main.lab import is_palindrome

class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("Python"))

if __name__ == "__main__":
    unittest.main()
