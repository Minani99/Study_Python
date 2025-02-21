import math


class Circle:
    def __init__(root,radius):
        root.__radius = radius

    @property
    def radius(root):
        return root.__radius

    @radius.setter
    def radius(root, value):
        if value <= 0:
            raise TypeError("길이는 양의 숫자")
        root.__radius = value


print("고")
circle = Circle(10)
print("반지름:", circle.radius)
circle.radius = 2
print(circle.radius)