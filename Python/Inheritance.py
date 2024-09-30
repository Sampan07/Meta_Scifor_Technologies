class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return f"{self.name} is Barking"
class Cat(Animal):
    def sound(self):
        return f"{self.name}: Meow"

dog = Dog("Dog")
print(dog.sound())
cat = Cat("Cat")
print(cat.sound())