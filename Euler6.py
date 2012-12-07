import math
n = 100

sum1 = 0
for i in range(1,n+1):
  sum1 += i**2
sumofsquares = sum1
sum2 = 0
for j in range(1,n+1):
  sum2 += j
squareofsum = sum2**2

d = max(sumofsquares, squareofsum)-min(sumofsquares, squareofsum)

print d
