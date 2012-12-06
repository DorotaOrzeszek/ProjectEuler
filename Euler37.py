def isprime(n):
  prime = True
  for i in range(2,n/2):
    if n % i == 0:
      prime = False
      break
    else:
      continue
  return prime

def primeLessN(n):
  primes = [2]
  for i in range(3,n+1,2):
    if isprime(i) == True:
      primes.append(i)
  return primes

# calculated solutions:
ans = [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]

s = 0
for el in ans:
  s += el
print ans, s
