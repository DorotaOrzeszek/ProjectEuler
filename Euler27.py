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

def isprime(n):
  if primeslist[n] == 1:
    return True
  else:
    return False

ans = []

bvals = []
for i in range(1000):
  if primeslist[i] == 1:
    bvals.append(i)

avals = range(-999,1000)
maxn = 0
product = 0

for a in avals:
  for b in bvals:
    n = 0
    while True:
      p = (n**2)+(a*n)+b
      if isprime(p):
        n += 1
      else:
        if n >= 39:
          if n > maxn:
            maxn = n
            product = a*b
          ans.append((a,b,n))
        break

print product
