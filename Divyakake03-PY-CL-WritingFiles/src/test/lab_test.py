import unittest
from src.main.lab import Lab

class TestLab(unittest.TestCase):
    def test_write_to_file(self):
        lab = Lab()
        filename = "test_output.txt"
        content = "This is a test content."
        
        # Call the write_to_file method
        success = lab.write_to_file(filename, content)
        
        # Assert that the operation was successful
        self.assertTrue(success, "Writing to file failed.")
        
        # Verify that the file has been written with the correct content
        with open(filename, 'r') as file:
            written_content = file.read()
        self.assertEqual(written_content, content, "Written content does not match expected content.")
        
        # Clean up: delete the test file
        import os
        os.remove(filename)

if __name__ == "__main__":
    unittest.main()
