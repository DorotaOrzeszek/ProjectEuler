import math
def divsum(n):
  dssum = -n
  sq = math.sqrt(n)
  if math.floor(sq) == sq:
    dssum += sq
    end = int(sq)
  else:
    end = int(sq)+1
  for i in range(1,end):
    if n % i == 0:
      dssum += i
      dssum += n/i
  return dssum

def nrtype(n):
  if n == divsum(n):
    return 'p' # n is perfect'
  elif n > divsum(n):
    return 'd' # n is deficient'
  else:
    return 'a' # n is abundant

maxnr = 28123
abundants = set()
for i in range(1,maxnr+1):
  if i < divsum(i):
    abundants.add(i)

sums = []
for a in range(1,maxnr+1):
  for b in abundants:
    if b > a:
      break
    if (a-b) in abundants:
      sums.append(a)
      break
notsums = range(1,maxnr+1)
for el in sums:
  notsums.remove(el)
answer = 0
for number in notsums:
  answer += number
print answer
