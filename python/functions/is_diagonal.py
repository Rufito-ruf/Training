def is_diagonal(matrix):
  n = len(matrix[0])
  result = True
  for i in range(n):
    for j in range(n):
      if (i != j) and (matrix[i][j] != 0):
        result = False
        break
  return result

diag = [
[1, 0, 0],
[0, 1, 0],
[0, 0, -1]
]

not_diag = [
[1, 1, 0],
[0, 1, 0],
[0, 1, -1]
]

print("Is this matrix", diag, "diagonal? -> ", is_diagonal(diag))
print("Is this matrix", not_diag, "diagonal? ->", is_diagonal(not_diag))
