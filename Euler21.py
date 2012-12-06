def divisors(n):
  divisors = []
  for i in range(1,n/2+1):
    if n % i == 0:
      divisors.append(i)
  return divisors
def sumdivisors(divisors):
  sumdivisors = 0
  for number in divisors:
    sumdivisors += number
  return sumdivisors

n = 10000
dsums = [0]
for i in range(1,n+1):
  dsums.append(sumdivisors(divisors(i)))
amicable = []
for a in range(0,len(dsums)):
  try:
    b = dsums[a]
    if b != a and dsums[b] == a:
      amicable.append(a)
  except IndexError:
    continue

amicablesum = 0
for element in amicable:
  amicablesum += element
print amicablesum
