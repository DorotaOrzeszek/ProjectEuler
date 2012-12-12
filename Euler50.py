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

def primesLessNList(primeslessn):
  primesLessNList = []
  for i in range(n):
    if primeslessn[i] == 1:
      primesLessNList.append(i)
  return primesLessNList
  
n = 1000000
primesraw = primesLessN(n)
primes = primesLessNList(primesraw)
lenp = len(primes)
potentials = {}
maxterms = 0

for i in range(lenp/2):
  psum = primes[i]
  terms = 1
  for j in range(i+1,lenp-i):
    if psum > n:
      break
    psum += primes[j]
    terms += 1
    if (terms > maxterms) and (psum <= n) and (primesraw[psum] == 1):
      potentials[terms] = psum

maxkey = max(potentials.keys())
print potentials[maxkey]
