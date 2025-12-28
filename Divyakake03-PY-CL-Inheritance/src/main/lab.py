class Vehicle:
    def __init__(self, make, model, year):
        """
        Initialize a Vehicle object.

        Parameters:
        - make (str): The make of the vehicle.
        - model (str): The model of the vehicle.
        - year (int): The manufacturing year of the vehicle.
        """
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """
        Display information about the vehicle.

        Returns:
        - str: A string containing the year, make, and model of the vehicle.
        """
        return f"{self.year} {self.make} {self.model}"

    def start(self):
        """
        Start the vehicle.

        Prints:
        - str: "Engine started"
        """
        print("Engine started")


    # To do: Create a Python class named Car that inherits from the Vehicle class.
    """
    Complete the Car class by filling in the constructor (__init__) and methods 
    (drive and refuel) as described below:

        * Implement the __init__ method to initialize the make, model, year, and fuel_type attributes of the car.

            
                - Initialize a Car object.

                Parameters:
                - make (str): The make of the car.
                - model (str): The model of the car.
                - year (int): The manufacturing year of the car.
                - fuel_type (str): The type of fuel the car uses.
        * Implement the drive method to print "Car is moving" when called.
                - Prints:
                - str: "Car is moving"

        * Implement the refuel method to print "Car is refueling" when called.
                - Prints:
                - str: "Car is refueling"
    """
class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
    def drive(self):
        print("Car is moving")
    def refuel(self):
        print("Car is refuelling")

        

