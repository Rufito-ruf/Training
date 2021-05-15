
import math

low = int(input("Enter the lower bound: "))
up = int(input("Enter the upper bound: "))

print("Prime numbers in range [lower, upper]: ", end = "")

for num in range(low, up+1):
  if (num == 2):
    print(num, end = " ")
  else:
    # It is enough to check till this number
    t = math.ceil(math.sqrt(num))

    for i in range(2, t+1):
      if (num % i == 0):
        break
    else:
      print(num, end = " ")

print()
