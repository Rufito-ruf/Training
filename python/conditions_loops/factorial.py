num = int(input("Input the number: "))

result = 1

if num < 0:
  print("The number is negative")
elif num == 0:
  print("{0}! equals {1}".format(num, result))
else:
  for i in range(2, num+1):
    result *= i
  print("{0}! equals {1}".format(num, result))

