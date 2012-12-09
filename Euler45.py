# hexagonal number reffered to in problem i H(143) so:
start = 144
stop = 50000

# hexagonal numbers
h = [n*(2*n-1) for n in range(start,stop)]
# pentagonal numbers
p = [n*(3*n-1)/2 for n in range(start,3*stop/2)]
# triangle numbers
t = [n*(n+1)/2 for n in range(start,2*stop)]

for el in h:
  if (el in p) and (el in t):
    print el
    break
