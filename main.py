class Person:
    def __init__(self, name):
        self.name = name
        self.age = 1

    def display_info(self):
        print(f"Name: {self.name}    Age: {self.age}")


tom = Person("tommy")
tom.age = 18
tom.display_info()

class Cat:
    def __init__(self, name):
        self.name = name 
        self.colour = black
    
    def display_info(self):
        print(f"Name: {self.name}    Colour: {self.colour}")
