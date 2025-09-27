import math

def circle_area(radius):
    return math.pi * radius ** 2

def circle_circumference(radius):
    return 2 * math.pi * radius

def geometry_report(radius):
    area = circle_area(radius)
    circumference = circle_circumference(radius)
    print("Circle with radius", radius)
    print("Area =", area)
    print("Circumference =", circumference)

