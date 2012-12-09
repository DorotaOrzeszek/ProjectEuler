import math
import itertools

def isprime(n):
  prime = True
  for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
      prime = False
      break
    else:
      continue
  return prime

def maxpandigital(string):
  pandigitals = []
  p = itertools.permutations(string)
  P = list(p)
  for line in P:
    number = ''.join(list(line))
    pandigitals.append(int(number))
  pandigitals.reverse()
  for el in pandigitals:
    if isprime(el) == True:
      maxpandigital = el
      return maxpandigital

biggestpandigital = 0

k = 1
while k < 10:
  digits = ''
  for j in range(1,k+1):
    digits += str(j)
  currentmaxpandigital = maxpandigital(digits)
  if currentmaxpandigital > biggestpandigital:
    biggestpandigital = currentmaxpandigital
  k += 1
print biggestpandigital
