from abc import ABC, abstractmethod
from math import pi

# interface 2D object
class I2dobj(ABC):
    @abstractmethod
    def calculateArea(self):
        pass

    @abstractmethod
    def calculateCircumference(self):
        pass 

class Rectangle(I2dobj):
    def setLength(self, a: float) -> None:
        try: 
            self.__length = float(a)
        except ValueError:
            print("Input type must be float.")

    def getLength(self):
        return self.__length
    
    def setWidth(self, b: float) -> None:
        try:
            self.__width = float(b)
        except ValueError:
            print("Input type must be float.")
    
    def getWidth(self):
        return self.__width

    def calculateArea(self):
        return self.__length * self.__width
    
    def calculateCircumference(self):
        return 2 * self.__length + 2 * self.__width


class Circle():
    def setRadius(self, r: float) -> None:
        try:
            self.__radius = float(r)
            return "Successfully changed radius to {self.radius}"
        except ValueError:
            print("Input type must be float.")

    def getRadius(self):
        return self.__radius

    def calculateArea(self):
        return pi * self.__radius**2

    def calculateCircumference(self):
        return 2 * pi * self.__radius 


rec1 = Rectangle()
rec1.setLength(5)
rec1.setWidth(7)
rec2 = Rectangle()
rec2.setLength(10)
rec2.setWidth(2)
cir1 = Circle()
cir1.setRadius(6)
cir2 = Circle()
cir2.setRadius(9)

print("\nRectangle 1:")
print("Area:", rec1.calculateArea())
print("Circumference:", rec1.calculateCircumference())
print("Length:", rec1.getLength())
print("Width:", rec1.getWidth())
print("\nRectangle 2:")
print("Area:", rec2.calculateArea())
print("Circumference:", rec2.calculateCircumference())
print("\nCircle 1:")
print("Area:",cir1.calculateArea())
print("Circumference:",cir1.calculateCircumference())
print("\nCircle 2:")
print("Area:",cir2.calculateArea())
print("Circumference:",cir2.calculateCircumference())
print("\nCircle 1 (Radius: 5):")
cir1.setRadius(5)
print("Area:",cir1.calculateArea())
print("Circumference:",cir1.calculateCircumference())
print("Radius:", cir1.getRadius())
print("\ntest ValueError:")
cir1.setRadius("hi")
print("Test successful")