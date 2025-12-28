# PY-CL-Abstraction

## Overview
This project demonstrates abstraction in Python using abstract classes and methods. Abstraction is a fundamental concept in object-oriented programming (OOP) that allows us to hide the implementation details of a class from the user and only expose the necessary interface. In this project, we define an abstract base class `Animal` with an abstract method `make_sound()`, and then create concrete subclasses `Dog`, `Cat`, and `Duck` that inherit from `Animal` and implement the `make_sound()` method with their specific sound.

## Files

### lab.py
The `lab.py` file contains the implementation of the `Animal`, `Dog`, `Cat`, and `Duck` classes. The `Animal` class is an abstract base class with an abstract method `make_sound()`, while the concrete subclasses `Dog`, `Cat`, and `Duck` inherit from `Animal` and provide their own implementations of the `make_sound()` method.

### lab_test.py
The `lab_test.py` file contains unit tests for the `Animal`, `Dog`, `Cat`, and `Duck` classes. It ensures that the `make_sound()` method behaves as expected for each subclass and that attempting to instantiate the abstract `Animal` class raises the appropriate `TypeError` exception.

## Project Structure
- src/
  - lab.py
  - test/
    - lab_test.py

## Getting Started
1. Open the `src/test/lab_test.py` file.
2. Run the `lab_test.py` file to execute the unit tests.
3. Ensure that all tests pass, indicating that the implemented classes and methods are working correctly.

## Conclusion
This project provides an example of abstraction in Python using abstract classes and methods. By defining abstract classes with abstract methods, we can enforce a consistent interface across different subclasses while allowing each subclass to provide its own implementation details.

Happy Coding!
