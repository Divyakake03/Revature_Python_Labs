# app.py
from lab import count_digits

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    total_digits = count_digits(num)
    print(f"The total number of digits in {num} is: {total_digits}")
