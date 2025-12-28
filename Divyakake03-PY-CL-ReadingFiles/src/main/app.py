# app.py

from lab import Lab

def main():
    lab_instance = Lab()
    filename = "example.txt"  # Replace with the path to your file
    content = lab_instance.read_file(filename)
    if content is not None:
        print("File content:")
        print(content)

if __name__ == "__main__":
    main()
