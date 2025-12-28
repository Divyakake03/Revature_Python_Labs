import unittest
from src.main.lab import Car, Vehicle

class TestVehicle(unittest.TestCase):
    def test_vehicle_display_info(self):
        vehicle = Vehicle("Toyota", "Camry", 2022)
        self.assertEqual(vehicle.display_info(), "2022 Toyota Camry")

    def test_vehicle_start(self):
        vehicle = Vehicle("Toyota", "Camry", 2022)
        self.assertIsNone(vehicle.start())

class TestCar(unittest.TestCase):
    def test_car_inheritance(self):
        self.assertTrue(issubclass(Car, Vehicle), "Car class should inherit from Vehicle class")

    def test_car_drive(self):
        car = Car("Toyota", "Camry", 2022, "Gasoline")
        self.assertIsNone(car.drive())

    def test_car_refuel(self):
        car = Car("Toyota", "Camry", 2022, "Gasoline")
        self.assertIsNone(car.refuel())

if __name__ == '__main__':
    unittest.main()
