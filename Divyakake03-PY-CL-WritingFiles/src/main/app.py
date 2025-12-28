# app.py

from lab import Lab

def main():
    lab_instance = Lab()
    filename = "example.txt"  # Replace with the path to your file
    content = input("Enter the content that you want to write to the file: \n")

    success = lab_instance.write_to_file(filename, content)
    if success:
        print(f"Content successfully written to {filename}")
    else:
        print("Failed to write content to file.")

if __name__ == "__main__":
    main()
