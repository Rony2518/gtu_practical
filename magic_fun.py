
class Example:
    def __init__(self):
        self.name = "Pickup"
        
    def __len__(self):
        return len(self.name)
    
    def __str__(self):
        return f"Good Mornog {self.name}"
    # def __repr__(self):
    #     return f"{type(self).__name__} name={self.name!r}"
print(Example().name)
print(len(Example().name))
print(Example())
# print(repr(Example()))