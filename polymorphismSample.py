class Dog:
    def speak(self):
        return "Bark"

class Cat:
    def speak(self):
        return "Meow"

def make_sound(animal):
    print(animal.speak())

dog1  = Dog()
cat1 = Cat()
make_sound(dog1)
make_sound(cat1)
