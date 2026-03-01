import abc

class Animal(abc.ABC):
    """Abstract base class for animals that can speak."""

    @abc.abstractmethod
    def speak(self) -> str:
        """
        Returns the sound the animal makes.
        This method must be implemented by concrete animal classes.
        """
        pass

class Dog(Animal):
    """Represents a dog."""
    def speak(self) -> str:
        """Returns the sound a dog makes."""
        return "Bark"

class Cat(Animal):
    """Represents a cat."""
    def speak(self) -> str:
        """Returns the sound a cat makes."""
        return "Meow"

class Cow(Animal):
    """Represents a cow, demonstrating easy extensibility."""
    def speak(self) -> str:
        """Returns the sound a cow makes."""
        return "Moo"

def make_sound(animal: Animal) -> None:
    """
    Makes the given animal speak and prints its sound.

    Args:
        animal: An object that inherits from Animal and implements the speak method.
                Type hinting helps ensure correct usage at development time,
                and runtime error handling adds robustness for unexpected inputs.
    """
    try:
        print(animal.speak())
    except AttributeError:
        # This catches cases where the object passed, despite type hints,
        # does not have a 'speak' method at runtime (e.g., if a non-Animal object
        # was passed, or an Animal subclass that didn't implement speak was somehow instantiated
        # or dynamically modified).
        print(f"Error: Object of type '{type(animal).__name__}' does not have a 'speak' method defined.") 
    except Exception as e:
        # Catch any other unexpected errors during the speak() call
        print(f"An unexpected error occurred while making '{type(animal).__name__}' speak: {e}")

# Example usage with corrected code:
dog1 = Dog()
cat1 = Cat()
cow1 = Cow()

print("--- Demonstrating correct usage ---")
make_sound(dog1)
make_sound(cat1)
make_sound(cow1)

print("\n--- Demonstrating error handling with an invalid object ---")

# An object that does not inherit from Animal and lacks a speak method
class Rock:
    def roll(self):
        return "Thud"

rock1 = Rock()
make_sound(rock1) # This will now be handled gracefully by the 'except AttributeError' block

# Passing primitive types (which also lack a speak method)
make_sound("This is a string")
make_sound(123)

# Note: Python's ABCs prevent instantiation of a class that inherits from Animal
# but does not implement its abstract methods. For example:
# class IncompleteAnimal(Animal):
#     pass
# incomplete_animal = IncompleteAnimal() # This would raise a TypeError at instantiation.
# Therefore, the primary runtime concern for make_sound's robustness is arbitrary, non-Animal objects.    