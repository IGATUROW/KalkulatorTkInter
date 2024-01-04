class Rectangle:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def get_area(self):
        return self.length1 * self.length2

def co_tu_mam(rectangles):
    for rectangle in rectangles:
        lengths = rectangle.length1, rectangle.length2
        area = rectangle.get_area()
        print(f"Długości boków: {lengths}, Pole powierzchni: {area}")

def z_listy(rectangles):
    for rectangle in rectangles:
        area = rectangle.get_area()
        print(area)


s1 = Rectangle(2,3)
s2 = Rectangle(3,4)
s3 = Rectangle(4,5)

rectangles = [s1,s2,s3]

print(s1.get_area())
print(s2.get_area())
print(s3.get_area())

z_listy(rectangles)
co_tu_mam(rectangles)