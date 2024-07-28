import math

def calculate_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def calculate_contribution(area, total_area):
    return (area / total_area) * 100


a1 = float(input("Enter the first side of the first triangle: "))
b1 = float(input("Enter the second side of the first triangle: "))
c1 = float(input("Enter the third side of the first triangle: "))


a2 = float(input("Enter the first side of the second triangle: "))
b2 = float(input("Enter the second side of the second triangle: "))
c2 = float(input("Enter the third side of the second triangle: "))


area1 = calculate_area(a1, b1, c1)
area2 = calculate_area(a2, b2, c2)


total_area = area1 + area2


print(f"The area of the first triangle is: {area1}")
print(f"The area of the second triangle is: {area2}")
print(f"The total area enclosed by both triangles is: {total_area}")

