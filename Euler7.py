import math

def primesLessN(maxn):
  primes = [0,0]+[1]*(maxn-1)
  for k in range(2,int(math.sqrt(maxn))+1):
    if primes[k] == 1:
      ki = k*k
      while ki <= maxn:
        primes[ki] = 0
        ki += k
  return primes

primeslist = primesLessN(1000000)
count = 0
for i in range(len(primeslist)):
  if primeslist[i] == 1:
    count += 1
  if count == 10001:
    print i
    break
