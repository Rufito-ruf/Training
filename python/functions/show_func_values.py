def f(x):
  if (-5 <= x) and (x <= 5):
    return x**2
  elif (x < -5):
    return 2*abs(x)-1
  else:
    return 2*x

def show_func_values():
  arguments = [i for i in range(-10, 11)]
  values = [f(i) for i in arguments] 
  
  return values

print(show_func_values())
  
