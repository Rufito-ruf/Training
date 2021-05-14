from cmath import sqrt

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

d = b**2 - 4*a*c
d = sqrt(d)

x1 = (-b-d)/(2*a)
x2 = (-b+d)/(2*a)

print("The solutions are {0} and {1}".format(x1, x2))
