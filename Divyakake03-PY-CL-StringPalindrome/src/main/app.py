from lab import is_palindrome

def main():
    user_input = input("Enter a string: ")
    if is_palindrome(user_input):
        print("The string is a palindrome.")
    elif is_palindrome(user_input)==None:
        print("It is still returning None")
    else:
        print("The string is not a palindrome")

if __name__ == "__main__":
    main()
