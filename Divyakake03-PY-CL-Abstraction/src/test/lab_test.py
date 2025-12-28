import unittest
from src.main.lab import *

class TestAnimal(unittest.TestCase):
    def test_dog_has_make_sound_method(self):
        self.assertTrue(hasattr(Dog, 'make_sound'), "Dog class should have a make_sound method")

    def test_cat_has_make_sound_method(self):
        self.assertTrue(hasattr(Cat, 'make_sound'), "Cat class should have a make_sound method")

    def test_duck_has_make_sound_method(self):
        self.assertTrue(hasattr(Duck, 'make_sound'), "Duck class should have a make_sound method")
    

    def test_dog_make_sound(self):
        dog = Dog("Buddy")
        self.assertEqual(dog.make_sound(), "Woof!")

    def test_cat_make_sound(self):
        cat = Cat("Whiskers")
        self.assertEqual(cat.make_sound(), "Meow!")

    def test_duck_make_sound(self):
        duck = Duck("Daffy")
        self.assertEqual(duck.make_sound(), "Quack!")

if __name__ == "__main__":
    unittest.main()