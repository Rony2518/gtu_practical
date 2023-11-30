class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

    def __repr__(self):
        return f"{type(self).__name__}('{self.name}', {self.age})"

obj = MyClass("John", 25)
print(obj)  # Calls __str__
print(repr(obj))  # Calls __repr__
