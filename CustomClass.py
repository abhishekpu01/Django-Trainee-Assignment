class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Return a generator that yields the length and width in the specified format
        yield {'length': self.length}
        yield {'width': self.width}

# Example Usage
rect = Rectangle(length=5, width=3)
for dimension in rect:
    print(dimension)
