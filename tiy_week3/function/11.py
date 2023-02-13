def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    '''
    6 + (5) = 21
    5 + (4) = 15 
    4 + (3) = 10
    3 + (2) = 6
    2 + (1) = 3
    1 + 0 = 1
    '''
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)