terms = int(input("How many terms do you want: "))

first = 1
second = 1
count = 2

if terms == 1:
  print(first, end=" ")
elif terms == 2:
  print(first, second, end=" ")
else:
  print(first, second, end=" ")
  while (count < terms):
    next = second + first
    first = second
    second = next
    print(next, end=" ")
    count+=1

print()
