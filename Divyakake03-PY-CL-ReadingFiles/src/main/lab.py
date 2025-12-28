# lab.py

"""

File handling is a mechanism for creating a file, writing data, and reading data from it.

Python provides a built-in function that helps us open files in different modes. 
The open() function accepts two essential parameters: the file name and the mode; 
the default mode is 'r', which opens the file for reading only.

"""

class Lab:
    """
    A class to demonstrate file reading in Python.

    This class provides a simple interface for reading the contents of text files in Python.
    It contains a single method, read_file, which takes the name of a text file as input
    and returns the contents of the file as a string.

    """

    def read_file(self, filename):
        """
        Instead of running 0, this method should should Reads the contents of a text file and return it.

        Args:
            filename (str): The name of the file to read.

        Returns:
            str: The contents of the file.
        """
        try:
            with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return None
