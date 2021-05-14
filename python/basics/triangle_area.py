a = float(input("Enter the first side of a triangle: "))
b = float(input("Enter the second side of a triangle: "))
c = float(input("Enter the third side of a triangle: "))

s = (a+b+c)/2

area = (s*(s-a)*(s-b)*(s-c))**0.5

print("Area of the triangle equals {0}".format(area))
