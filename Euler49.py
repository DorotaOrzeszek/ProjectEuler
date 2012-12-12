import math
import copy

def primesLessN(maxn):
  primes = [0,0]+[1]*(maxn-1)
  for k in range(2,int(math.sqrt(maxn))+1):
    if primes[k] == 1:
      ki = k*k
      while ki <= maxn:
        primes[ki] = 0
        ki += k
  return primes

def primesLessNList(n):
  primeslessn = primesLessN(n)
  primesLessNList = []
  for i in range(n):
    if primeslessn[i] == 1:
      primesLessNList.append(i)
  return primesLessNList

n = 10000
primes = primesLessNList(n)
primes4dig = copy.copy(primes)
for el in primes:
  if el < 1000:
    primes4dig.remove(el)
    
potentials = []
for a1 in primes4dig:
  a1digits = set(str(a1)) 
  for c in range(2,9000,2):
    a3 = a1 + 2*c
    if a3 > 9999:
      break
    a2 = a1 + c
    if set(str(a2)) == a1digits and set(str(a3)) == a1digits and (a2 in primes4dig) and (a3 in primes4dig):
      potentials.append((a1,a2,a3))

potentials.remove((1487, 4817, 8147))

ans = str(potentials[0][0]) + str(potentials[0][1]) + str(potentials[0][2])
print ans
