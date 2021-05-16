def list_sum(l):
  length = len(l)
  result = 0
  for i in range(length):
    result += l[i]
  return result

example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Sum of the example list equals", list_sum(example))

