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

def isprime(n):
  if primeslist[n] == 1:
    return True
  else:
    return False

start = 1
stop = 1000000
primeslist = primesLessN(stop)
count = 0

for n in range(start,stop):
  strn = str(n)
  rotations = [n]
  i = 1
  while i < len(strn):
    rotation = strn[1:]+strn[0]
    rotations.append(int(rotation))
    strn = rotation
    i += 1
  for el in rotations:
    if isprime(el)==False:
      c = 0 # n not circular
      break
    else:
      c = 1
  if c == 1:
    count += 1
    
print count
