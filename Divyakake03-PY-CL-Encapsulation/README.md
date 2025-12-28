# PY-CL-Encapsulation


## Overview

This project implements a simple bank account class (`BankAccount`) in Python. The `BankAccount` class provides basic operations such as depositing funds, withdrawing funds, and retrieving account information.

## Files

### lab.py

The `lab.py` file contains the implementation of the `BankAccount` class. It includes methods for initializing a bank account, depositing funds, withdrawing funds, and retrieving account information (balance and account number). The class also demonstrates encapsulation by encapsulating the account number and balance as private attributes.

### lab_test.py

The `lab_test.py` file contains unit tests for the `BankAccount` class. It includes test cases to verify the functionality of the `BankAccount` methods, such as depositing funds, withdrawing funds, and retrieving account information.

## Project Structure

- src/
  - main/
    - lab.py
  - test/
    - lab_test.py

## Getting Started

1. Open the `src/main/lab.py` file to view the implementation of the `BankAccount` class.
2. Review the methods provided by the `BankAccount` class, including `__init__`, `deposit`, `withdraw`, `get_balance`, and `get_account_number`.
3. Open the `src/test/lab_test.py` file to view the unit tests for the `BankAccount` class.
4. Run the `lab_test.py` file to execute the unit tests and ensure that the `BankAccount` class functions as expected.

## Encapsulation

Encapsulation is a fundamental principle of object-oriented programming (OOP) that focuses on bundling the data (attributes) and methods (functions) that operate on the data into a single unit called a class. In this `BankAccount` class, the account number and balance are encapsulated as private attributes (`_account_number` and `_balance`), which can only be accessed and modified through the defined methods (`deposit`, `withdraw`, `get_balance`, `get_account_number`). This ensures data integrity and prevents direct manipulation of the internal state of the object.

## Testing

1. Open the `src/test/lab_test.py` file.
2. Review the test cases provided for the `BankAccount` class methods.
3. Run the `lab_test.py` file to execute the unit tests and verify the correctness of the `BankAccount` class implementation.

## Conclusion

This project demonstrates the implementation of a simple bank account class in Python, highlighting the principles of encapsulation in object-oriented programming. By encapsulating the account data and providing controlled access through methods, the `BankAccount` class ensures data integrity and provides a secure interface for interacting with bank account objects.

Happy Coding!
