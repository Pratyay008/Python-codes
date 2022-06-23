# Write a class calculator capable of finding square, cube, and the square root of a number.

class calculator():
    def __init__(self, value ):
        self.value=value
        
    def square(self):
        print(f"Square of the number is {self.value**2}")
    def cube(self):
        print(f"Cube of the number is {self.value**3} ")
    def square_root(self):
        print(f"Square root of the number is {self.value**0.5} ")


input=calculator(4)
input.square()
input.cube()
input.square_root()