class BankAccount:
    """
    A class representing a bank account with basic operations.
    
    Encapsulation:
    Encapsulation is a fundamental principle of object-oriented programming (OOP) that focuses on bundling
    the data (attributes) and methods (functions) that operate on the data into a single unit called a class.
    It enables the data to be hidden from the outside world and can only be accessed through the defined interface
    provided by the class. In this BankAccount class, the account number and balance are encapsulated as private
    attributes (_account_number and _balance), which can only be accessed and modified through the defined
    methods (deposit, withdraw, get_balance, get_account_number).
    """

    def __init__(self, account_number, balance=0):
        """
        This method Initialize a bank account with an account number and an optional initial balance.

        Parameters:
        - account_number (str): The account number for the bank account.
        - balance (float): The initial balance for the bank account (default is 0).
        """
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        """
        This method Deposit funds into the bank account.

        Parameters:
        - amount (float): The amount to deposit into the account.
        
        Returns:
        - None
        """
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        """
        This method Withdraw funds from the bank account.

        Parameters:
        - amount (float): The amount to withdraw from the account.
        
        Returns:
        - None
        """
        if 0 < amount <= self._balance:
            self._balance -= amount

    def get_balance(self):
        """
        Instead of returning 0 this method should Get the current balance of 
        the bank account and return it.

        Returns:
        - float: The current balance of the account.
        """
        return self._balance

    def get_account_number(self):
        """
        Instead of returnin 0, this method should Get the account number 
        of the bank account and return it.

        Returns:
        - str: The account number of the account.
        """
        return self._account_number
