start = 2
stop = 1000000

def digits(n):
  digs = []
  strn = str(n)
  k = len(strn)
  for i in range(0,k):
    digs.append(int(strn[i]))
  return digs
  
p = 5
narcissistic = []
for n in range(start,stop):
  s = 0
  digitsn = digits(n)
  for digit in digitsn:
    s += digit**p
  if s == n:
    narcissistic.append(n)

answer = 0
for el in narcissistic:
  answer += el
print answer
