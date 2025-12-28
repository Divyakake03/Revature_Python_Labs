# lab_test.py

import unittest
from src.main.lab import Lab

class TestLab(unittest.TestCase):
    def test_must_throw(self):
        lab = Lab()
        with self.assertRaises(Exception):
            lab.must_throw()

    def test_must_throw_exists(self):
        lab = Lab()
        self.assertTrue(hasattr(lab, 'must_throw'), "must_throw() method does not exist.")


if __name__ == "__main__":
    unittest.main()
