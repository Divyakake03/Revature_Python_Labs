# lab_test.py

import unittest
import os
from src.main.lab import Lab

class TestLab(unittest.TestCase):
    def setUp(self):
        self.lab = Lab()
        self.file_path = os.path.join(os.path.dirname(__file__), '..', 'main', 'example.txt')

    def test_read_existing_file(self):
        # Load expected content from the file
        with open(self.file_path, 'r') as file:
            expected_content = file.read().strip()  # Strip leading and trailing whitespace

        # Read content using Lab class method
        content = self.lab.read_file(self.file_path)
        
        # Assert that content matches expected content
        self.assertEqual(content.strip(), expected_content)  # Strip leading and trailing whitespace

    def test_read_nonexistent_file(self):
        filename = 'nonexistent.txt'  # Change this if needed
        content = self.lab.read_file(filename)
        self.assertIsNone(content)

if __name__ == "__main__":
    unittest.main()
