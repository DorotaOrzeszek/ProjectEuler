import math
n = 1000
answer = 0
for a in range(1,n+1):
  for b in range(1,n+1):
    c2 = 1000**2 - 2000*a - 2000*b + 2*a*b + a**2 + b**2
    if a**2 + b**2 == c2:
      answer = a * b * int(math.sqrt(c2))
      break
  if answer > 0:
    print answer
    break
