from lab import Dog, Cat, Duck

def main():
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    duck = Duck("Donald")

    animals = [dog, cat, duck]

    for animal in animals:
        print(f"{animal.name} says: {animal.make_sound()}")

if __name__ == "__main__":
    main()
