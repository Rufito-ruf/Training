from math import floor
num = int(input("Enter the number to check it: "))

sum = 0
check_num = num

while num > 0:
  digit = num % 10
  num //= 10
  sum += digit**3

if (sum == check_num):
  print("It is an Armstrong number")
else:
  print("It is not an Armstrong number")
