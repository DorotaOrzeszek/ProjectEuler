import math
dict = {}
n = 1000
for i in range(0,1001):
  dict[i] = 0
for a in range(1,n+1):
  for b in range(1,n+1):
    c = math.sqrt(a**2+b**2)
    if c == int(c):
      p = int(a + b + c)
      if p <= 1000:
        dict[p] += 1
for j in range(0,1000):
  if dict[j] > 12:
    print j,
