n = 600851475143

def primefactors(n):
  i = 2
  factors = []
  while i <= n:
    if n % i == 0:
      factors.append(i)
      n = n / i
    else:
      pass
    i += 1
  return factors
  
primefactors = primefactors(n)
print max(primefactors)
