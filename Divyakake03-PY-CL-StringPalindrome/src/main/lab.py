def is_palindrome(s):
    """
    Instead of returning None, this method should Check if a string is a palindrome
    and return True or False accordingly.
    
    :param s: The string to check.
    :return: True if the string is a palindrome, False otherwise.
    """
    # Convert the string to lowercase and remove non-alphanumeric characters
    s = ''.join(char.lower() for char in s if char.isalnum())
    r=s[::-1]
    # Compare the string with its reverse


    return s==r
