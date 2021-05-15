num = int(input("You want a multiplication table of: "))

for i in range(1, 11):
  print("{0} x {1} = {2}".format(num, i, num*i))
