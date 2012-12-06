f = [1,1,2,6,24,120,720,5040,40320,362880]
numbers = range(3,10000000)
curious = []
for el in numbers:
  sumf = 0
  strn = str(el)
  for char in strn:
    sumf += f[int(char)]
  if el == sumf:
    curious.append(el)
sumc = 0
for elem in curious:
  sumc += elem
print sumc
