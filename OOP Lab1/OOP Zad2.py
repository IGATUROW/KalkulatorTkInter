class Square:
    def __init__(self,length):
        self.length = length

    def get_area(self):
        return self.length * self.length


s1 = Square(2)
s2 = Square(3)
s3 = Square(4)

print(s1.get_area())
print(s2.get_area())
print(s3.get_area())
