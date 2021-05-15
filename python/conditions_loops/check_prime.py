import math

num = int(input("Enter the number: "))

# It is enough to check till this number
t = math.ceil(math.sqrt(num))

if (num == 2):
  print("It is a prime number")
else:
  for i in range(2, t+1):
    if (num % i == 0):
      print("It is not a prime number")
      break
  else:
    print("It is a prime number")





