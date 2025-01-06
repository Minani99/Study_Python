import math


class Circle:
    def __init__(self,radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise TypeError("길이는 양의 숫자")
        self.__radius = value


print("고")
circle = Circle(10)
print("반지름:", circle.radius)
circle.radius = 2
print(circle.radius)