class Lab:
    """
    A class to demonstrate file writing in Python.
    """

    def write_to_file(self, filename, content):
        """
        Writes content to a file.

        Args:
            filename (str): The name of the file to write to.
            content (str): The content to write to the file.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        try:
            with open(filename, 'w') as file:
                file.write(content)
                
                # Write your code here so that you should be able to write the content into the file
        
                # Check if anything was actually written to the file
                if file.tell() > 0:
                    return True
                else:
                    return False
        except Exception as e:
            print(f"Error writing to file '{filename}': {e}")
            return False
