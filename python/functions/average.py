def average(l):
  result = 0
  length = len(l)
  for i in range(length):
    result += l[i]
  
  average = result / length
  return average

example = [1, 2, 3]

print("The average of the list", example, "equals", average(example))

