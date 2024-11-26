class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def __str__(self):
        return f"Triangle with sides: {self.side1}, {self.side2}, {self.side3}"

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

triangle = Triangle(side1, side2, side3)
print(triangle)
print(f"Perimeter: {triangle.perimeter()}")
print(f"Area: {triangle.area()}")
