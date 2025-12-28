import unittest
from src.main.lab import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        # Create a BankAccount instance for testing
        self.account = BankAccount("1234567890", 1000)

    def test_initial_balance(self):
        # Test the initial balance of the account
        self.assertEqual(self.account.get_balance(), 1000, "Initial balance should be 1000")

    def test_deposit(self):
        # Test depositing funds into the account
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500, "Balance after deposit should be 1500")

    def test_withdraw(self):
        # Test withdrawing funds from the account
        self.account.withdraw(200)
        self.assertEqual(self.account.get_balance(), 800, "Balance after withdrawal should be 800")

    def test_account_number(self):
        # Test getting the account number
        self.assertEqual(self.account.get_account_number(), "1234567890", "Account number should match")

if __name__ == '__main__':
    unittest.main()
