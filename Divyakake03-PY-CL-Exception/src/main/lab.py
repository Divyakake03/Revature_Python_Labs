class Lab:
    """
    An exception is an unexpected event that occurs during our program.
    Most likely, you have already encountered an Exception (ArrayIndexOutOfBounds, etc).
    In order for our program to compile, Python needs to be prepared for how to handle an exception -
    for instance, you could use a try/except block to prepare some code in an 'except' for the event that an exception
    fires, or you can let the exception propagate to the calling code.
    (if an exception is unhandled, Python will crash.) Correctly managing and throwing exceptions actually
    makes our application more robust as we can't expect operations on files, databases, or the internet to always
    succeed. For instance, if the development of a new method would require a FileNotFoundError to be raised in
    a certain situation, the line raise FileNotFoundError().
    
    

    This also means that you should NOT write a try/except block in this method, as the tests are expecting to have
    an exception raised. A try/except block would handle the exception within the method.
    """

    """
    Write a method called "must_throw" that raises an Exception. Notice also that
    this method has a return type of None - it doesn't need to return anything since the 
    test cases are just checking for a raised exception!
    """
    def must_throw(self):
        raise Exception("This is a custom exception message.")