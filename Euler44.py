import math
def ispentagonal(x):
  pent = False
  test = (math.sqrt(24*x+1)+1)/6.0
  if test == int(test):
    pent = True
  return pent
start = 1
stop = 100
p = [n*(3*n-1)/2 for n in range(start,stop)]
s = 0
d = 0
ans = [] # (a,b) that a+b, a-b are pentagonal
i = 1
var = True
while var:
  n = i*(3*i-1)/2
  for j in range(2,i-1):
    m = j*(3*j-1)/2
    if ispentagonal(n-m) and ispentagonal(n+m):
      print n-m
      var = False
      break
  i += 1
