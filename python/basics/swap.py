a = input("Waiting for an input: ")
b = input("Waiting again: ")

print("Before swap: {0} and {1}".format(a, b))
a, b = b, a
print("After swap: {0} and {1}".format(a, b))

print("Let's swap again using another method")

temp = a
a = b
b = temp

print("After swap: {0} and {1}".format(a, b))
