def factors(n): 
# returns list of factors
  factors = []
  for i in range(2,n+1):
    for j in range(1,n+1):
      if n % i**j == 0:
        if i not in factors:
          factors.append(i)
  return factors

def primefactors(n):
# returns list of prime factors
  i = 2
  factors = []
  while i<= n:
    if n%i == 0:
      factors.append(i)
      n = n/i
    else:
      i += 1
  return factors

def GCD(a,b):
# returns greatest common divisor of list
  aprimes = primefactors(a)
  bprimes = primefactors(b)
  commons = []
  if len(aprimes) < len(bprimes):
    for el in aprimes:
      if el in bprimes:
        #print 'adding', el, 'to commons'
        commons.append(el)
        bprimes.remove(el)
  else:
    for el in bprimes:
      if el in aprimes:
        commons.append(el)
  #print commons
  gcd = 1
  for el in commons:
    gcd *= el
  return gcd

def LCM(l):
# returns least common multiple of list
  if len(l) == 1:
    lcm = l[0]
  if len(l) == 2:
    lcm = (l[0]*l[1])/(GCD(l[0],l[1]))
  else:
    lcm = LCM([l[0],LCM(l[1:])])
  return lcm

n = 20
numberlist = range(1,n+1)
print LCM(numberlist)

