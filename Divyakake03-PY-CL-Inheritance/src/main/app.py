from lab import Car

def main():
    # Test the Car class
    car = Car("Toyota", "Camry", 2022, "Gasoline")

    print(car.display_info())
    car.start()
    car.drive()
    car.refuel()

if __name__ == "__main__":
    main()
