import math
def triangle(n):
  tri = 0
  for k in range(1,n+1):
    tri += k
  return tri

def divisors(n):
  ds = 0
  sq = math.sqrt(n)
  if math.floor(sq) == sq:
    ds += 1
    end = int(sq)
  else:
    end = int(sq)+1
  for i in range(1,end):
    if n % i == 0:
      ds += 1
  ds *= 2
  return ds

def primefactors(n):
  pfactors = []
  sq = math.sqrt(n)
  if math.floor(sq) == sq:
    end = int(sq)
  else:
    end = int(sq)+1
  for i in range(2,end):
    while n % i == 0:
      pfactors.append(i)
      n = n / i
  return pfactors

def nrfactors(n):
  pfactorsnrep = primefactors(n)
  powers = []
  for el in set(pfactorsnrep):
    nr = pfactorsnrep.count(el)
    powers.append(nr)
  pfactorsn = list(set(pfactorsnrep))
  nrfactors = 1
  for power in powers:
    nrfactors *= power+1
  #print n, pfactorsnrep,'nrfactors', nrfactors
  return nrfactors

n = 1
tri = 0
while True:
  tri = tri + n
  nrfactorstri = nrfactors(tri)
  if nrfactorstri >= 500:
    print tri
    break
  n += 1
