# lab.py
def count_digits(num):
    """
    Counts the total number of digits in a given number using a while loop.

    To count the digits in a number, we repeatedly divide the number by 10 until it becomes 0,
    incrementing a counter variable each time. This process continues until there are no more digits
    left in the number.

    :param num: The number for which to count the digits.
    :return: The total number of digits in the given number.
    """
    # Take the absolute value of the number to handle negative input gracefully
    num = abs(num)

    # Initialize a counter to keep track of the number of digits
    

    # Handle the case of 0 separately
    if num == 0:
        return 1

    # Iterate while the number is not 0
        # Increment the counter for each digit
        # Remove the last digit by dividing the number by 10

    # Enter you code here   
    count=0
    while num>0:
        count+=1
        num=num//10


    # Return the total count of digits
    return count
