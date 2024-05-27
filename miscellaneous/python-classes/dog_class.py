class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return 'WOOF!'

dog = Dog('Spike')

# print(dog.name)
# print(dog.kind)

# barking_function = dog.bark
# print(f"Barking function: {barking_function}")

# print(f"Using Dog class: {Dog.bark(dog)}")
# print(f"Using Dog class method: {Dog.bark}")
# print(f"Using dog class instance: {dog.bark()}")
# print(f"Using barking_function variable: {barking_function()}")
