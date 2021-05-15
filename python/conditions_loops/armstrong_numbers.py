low = int(input("Enter the lower bound: "))
up = int(input("Enter the upper bound: "))

print("Armstrong number in range [low, up]: ", end = " ")

for num in range(low, up+1):
  sum = 0
  check_num = num

  while num > 0:
    digit = num % 10
    num //= 10
    sum += digit**3

  if (sum == check_num):
    print(check_num, end=" ")

print()
