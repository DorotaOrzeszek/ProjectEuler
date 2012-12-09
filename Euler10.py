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

n = 2000000
primessum = 0
primeslist = primesLessN(n)
for i in range(n):
  currentelement = primeslist[i]
  if currentelement == 1:
    primessum += i

print primessum
