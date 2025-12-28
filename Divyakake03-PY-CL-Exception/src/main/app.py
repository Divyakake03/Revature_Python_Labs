# app.py

from lab import Lab

def main():
    lab = Lab()
    try:
        lab.must_throw()
    except Exception as e:
        print("Exception caught:", e)

if __name__ == "__main__":
    main()
